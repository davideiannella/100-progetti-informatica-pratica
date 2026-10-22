"""Laboratorio locale: scrypt standard, TOTP RFC 6238, lockout e sessioni.

Nessun server HTTP. Secret MFA in chiaro nel database: usare solo dati sintetici.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone
from functools import lru_cache
import base64
import binascii
import hashlib
import hmac
import re
import secrets
import sqlite3
import struct


@dataclass(frozen=True)
class AuthResult:
    ok: bool
    message: str
    session_token: str | None = None


def _now(value=None):
    value = datetime.now(timezone.utc) if value is None else value
    if not isinstance(value, datetime) or value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("richiesto datetime con fuso orario")
    if value.timestamp() < 0:
        raise ValueError("tempo precedente all'epoca Unix")
    return value


class ScryptHasher:
    """Formato del record locale; la KDF è hashlib.scrypt, non un algoritmo nuovo."""
    N, R, P = 32768, 8, 3

    @staticmethod
    def _password(password):
        if not isinstance(password, str):
            raise ValueError("password testuale richiesta")
        try:
            raw = password.encode("utf-8")
        except UnicodeEncodeError as exc:
            raise ValueError("Unicode non valido") from exc
        if len(raw) > 1024:
            raise ValueError("password oltre 1024 byte UTF-8")
        return raw

    def _derive(self, raw, salt):
        return hashlib.scrypt(raw, salt=salt, n=self.N, r=self.R, p=self.P,
                              maxmem=64 * 1024 * 1024, dklen=32)

    def hash(self, password):
        raw = self._password(password)
        salt = secrets.token_bytes(16)
        digest = self._derive(raw, salt)
        return f"scrypt${self.N}${self.R}${self.P}${salt.hex()}${digest.hex()}"

    def verify(self, stored, password):
        try:
            raw = self._password(password)
            parts = stored.split("$")
            if len(parts) != 6 or parts[:4] != ["scrypt", str(self.N), str(self.R), str(self.P)]:
                return False
            if not re.fullmatch(r"[0-9a-f]{32}", parts[4]) or not re.fullmatch(r"[0-9a-f]{64}", parts[5]):
                return False
            salt, expected = bytes.fromhex(parts[4]), bytes.fromhex(parts[5])
            return hmac.compare_digest(self._derive(raw, salt), expected)
        except (ValueError, TypeError, AttributeError):
            return False


@lru_cache(maxsize=1)
def _dummy_hash():
    return ScryptHasher().hash(secrets.token_urlsafe(32))


class AuthService:
    def __init__(self, db_path=":memory:", max_failures=3, lock_minutes=5, session_minutes=30):
        for value in (max_failures, lock_minutes, session_minutes):
            if type(value) is not int or not 1 <= value <= 10000:
                raise ValueError("parametri interi positivi, massimo 10000")
        self.ph = ScryptHasher()
        self.dummy_hash = _dummy_hash()
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.max_failures, self.lock_minutes = max_failures, lock_minutes
        self.session_minutes = session_minutes
        self.sessions = {}
        self.audit = deque(maxlen=1000)
        self.conn.execute("""CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY, password_hash TEXT NOT NULL,
            totp_secret TEXT NOT NULL, failed_attempts INTEGER NOT NULL DEFAULT 0,
            locked_until REAL, last_totp_counter INTEGER NOT NULL DEFAULT -1)""")
        columns = {row[1] for row in self.conn.execute("PRAGMA table_info(users)")}
        if "last_totp_counter" not in columns:
            # Solo schema: hash Argon2 originali non vengono convertiti né indeboliti.
            self.conn.execute("ALTER TABLE users ADD COLUMN last_totp_counter INTEGER NOT NULL DEFAULT -1")
        self.conn.commit()

    def close(self):
        self.conn.close()
        self.sessions.clear()

    @staticmethod
    def _new_totp_secret():
        return base64.b32encode(secrets.token_bytes(20)).decode("ascii").rstrip("=")

    @staticmethod
    def _normalize_b32(secret):
        if not isinstance(secret, str) or not re.fullmatch(r"[A-Za-z2-7]{26,103}", secret):
            raise ValueError("secret Base32 non valido, senza padding")
        try:
            raw = base64.b32decode(secret.upper() + "=" * ((8 - len(secret) % 8) % 8))
        except (binascii.Error, ValueError) as exc:
            raise ValueError("secret Base32 non valido") from exc
        canonical = base64.b32encode(raw).decode().rstrip("=")
        if len(raw) < 16 or len(raw) > 64 or canonical != secret.upper():
            raise ValueError("secret richiesto: da 128 a 512 bit")
        return raw

    @staticmethod
    def _code(key, counter, digits):
        digest = hmac.new(key, struct.pack(">Q", counter), hashlib.sha1).digest()
        offset = digest[-1] & 0x0F
        binary = struct.unpack(">I", digest[offset:offset + 4])[0] & 0x7FFFFFFF
        return str(binary % (10 ** digits)).zfill(digits)

    @classmethod
    def totp_code(cls, secret, when=None, step=30, digits=6):
        when = _now(when)
        if type(step) is not int or step <= 0 or type(digits) is not int or digits not in (6, 8):
            raise ValueError("step positivo e digits 6 o 8")
        return cls._code(cls._normalize_b32(secret), int(when.timestamp()) // step, digits)

    @classmethod
    def _matching_counter(cls, secret, code, when, window=1):
        if type(window) is not int or not 0 <= window <= 2:
            raise ValueError("finestra TOTP da 0 a 2")
        if not isinstance(code, str) or re.fullmatch(r"[0-9]{6}", code) is None:
            return None
        key = cls._normalize_b32(secret)
        counter = int(_now(when).timestamp()) // 30
        matched = []
        for candidate in range(max(0, counter - window), counter + window + 1):
            if hmac.compare_digest(cls._code(key, candidate, 6), code):
                matched.append(candidate)
        return max(matched) if matched else None

    @classmethod
    def verify_totp(cls, secret, code, when=None, window=1):
        """Solo validità temporale; l'anti-replay persistente è in login()."""
        return cls._matching_counter(secret, code, _now(when), window) is not None

    @staticmethod
    def _username(username):
        if not isinstance(username, str) or not 1 <= len(username.strip()) <= 128:
            raise ValueError("username: da 1 a 128 caratteri")
        return username.strip()

    def register(self, username, password, *, totp_secret=None):
        username = self._username(username)
        self.ph._password(password)
        if len(password) < 12:
            raise ValueError("password: almeno 12 caratteri per il laboratorio")
        secret = self._new_totp_secret() if totp_secret is None else totp_secret
        self._normalize_b32(secret)
        try:
            with self.conn:
                self.conn.execute("INSERT INTO users(username,password_hash,totp_secret) VALUES(?,?,?)",
                                  (username, self.ph.hash(password), secret.upper()))
        except sqlite3.IntegrityError as exc:
            raise ValueError("utente già esistente") from exc
        return secret.upper()

    def _row(self, username):
        return self.conn.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()

    def password_hash_for(self, username):
        row = self._row(self._username(username))
        if row is None:
            raise KeyError(username)
        return row["password_hash"]

    def _failure(self, timestamp):
        self.audit.append({"event": "login", "ok": False, "time": timestamp})
        return AuthResult(False, "Credenziali o secondo fattore non validi")

    def login(self, username, password, totp, *, now=None):
        moment = _now(now)
        timestamp = moment.timestamp()
        try:
            username = self._username(username)
        except ValueError:
            return self._failure(timestamp)
        row = self._row(username)
        if row is None:
            self.ph.verify(self.dummy_hash, password)
            return self._failure(timestamp)
        locked = row["locked_until"]
        if locked is not None:
            # Gestione conservativa del vecchio campo ISO nei database originali.
            try:
                locked = float(locked)
            except ValueError:
                locked = datetime.fromisoformat(locked).timestamp()
            if timestamp < locked:
                return self._failure(timestamp)
        password_ok = self.ph.verify(row["password_hash"], password)
        counter = self._matching_counter(row["totp_secret"], totp, moment)
        if not password_ok or counter is None or counter <= row["last_totp_counter"]:
            failures = row["failed_attempts"] + 1
            locked_until = timestamp + 60 * self.lock_minutes if failures >= self.max_failures else None
            with self.conn:
                self.conn.execute("UPDATE users SET failed_attempts=?,locked_until=? WHERE username=?",
                                  (0 if locked_until else failures, locked_until, username))
            return self._failure(timestamp)
        with self.conn:
            updated = self.conn.execute("""UPDATE users SET failed_attempts=0,locked_until=NULL,
                last_totp_counter=? WHERE username=? AND last_totp_counter<?""", (counter, username, counter))
        if updated.rowcount != 1:
            return self._failure(timestamp)
        token = secrets.token_urlsafe(32)
        self.sessions[token] = (username, timestamp + 60 * self.session_minutes)
        self.audit.append({"event": "login", "ok": True, "time": timestamp})
        return AuthResult(True, "Accesso riuscito", token)

    def validate_session(self, token, *, now=None):
        timestamp = _now(now).timestamp()
        if not isinstance(token, str) or re.fullmatch(r"[A-Za-z0-9_-]{43}", token) is None:
            return False
        item = self.sessions.get(token)
        if item is not None and timestamp >= item[1]:
            self.sessions.pop(token)
            return False
        return item is not None

    def logout(self, token):
        if isinstance(token, str):
            self.sessions.pop(token, None)


def demo():
    auth = AuthService()
    try:
        # Solo fixture pubblica del laboratorio, non un segreto per utenti reali.
        secret = base64.b32encode(b"12345678901234567890").decode()
        now = datetime(2026, 10, 10, 12, 0, tzinfo=timezone.utc)
        auth.register("anna", "Frase-lunga-di-laboratorio", totp_secret=secret)
        code = auth.totp_code(secret, now)
        result = auth.login("anna", "Frase-lunga-di-laboratorio", code, now=now)
        print("Algoritmo password:", auth.password_hash_for("anna").split("$")[0])
        print("Primo login:", result.ok)
        print("Stesso TOTP riutilizzato:", auth.login("anna", "Frase-lunga-di-laboratorio", code, now=now).ok)
        print("Sessione valida:", auth.validate_session(result.session_token, now=now))
        auth.logout(result.session_token)
        print("Dopo logout:", auth.validate_session(result.session_token, now=now))
    finally:
        auth.close()


if __name__ == "__main__":
    demo()
