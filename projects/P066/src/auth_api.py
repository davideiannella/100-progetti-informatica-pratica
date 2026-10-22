"""Profilo JWT HS256 ristretto per laboratorio locale; non una libreria JOSE generale."""
import base64
from collections import deque
from fractions import Fraction
import hashlib
import hmac
import json
import math
import re
import time

ROLES = {"user": 1, "operator": 2, "admin": 3}
ISSUER = "p066-lab"
AUDIENCE = "p066-api"


def b64url(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def b64url_decode(text):
    if not isinstance(text, str) or not text or not re.fullmatch(r"[A-Za-z0-9_-]+", text):
        raise ValueError("Base64URL non valido")
    try:
        raw = base64.b64decode(text + "=" * ((4 - len(text) % 4) % 4), altchars=b"-_", validate=True)
    except (ValueError, base64.binascii.Error) as exc:
        raise ValueError("Base64URL non valido") from exc
    if b64url(raw) != text:
        raise ValueError("Base64URL non canonico")
    return raw


def _key(secret):
    if isinstance(secret, str):
        secret = secret.encode("utf-8")
    if not isinstance(secret, bytes) or not 32 <= len(secret) <= 4096:
        raise ValueError("chiave HS256: da 32 a 4096 byte")
    return secret


def _instant(now):
    if isinstance(now, bool) or not isinstance(now, (int, float)):
        raise ValueError("tempo numerico richiesto")
    # Gli int mantengono tutti i bit: convertirli in float perderebbe unità oltre 2**53.
    if now < 0 or (isinstance(now, float) and not math.isfinite(now)):
        raise ValueError("tempo finito >= 0 richiesto")
    return now


def _label(value):
    return isinstance(value, str) and 1 <= len(value) <= 128


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("claim JSON duplicato")
        result[key] = value
    return result


def _invalid_constant(_):
    raise ValueError("numero JSON non finito")


def _object(segment):
    try:
        result = json.loads(b64url_decode(segment).decode("utf-8"),
                            object_pairs_hook=_pairs, parse_constant=_invalid_constant)
    except (UnicodeDecodeError, json.JSONDecodeError, RecursionError) as exc:
        raise ValueError("JSON non valido") from exc
    if not isinstance(result, dict):
        raise ValueError("oggetto JSON richiesto")
    return result


def issue_token(user, role, secret, ttl=300, now=None, *, issuer=ISSUER, audience=AUDIENCE):
    key = _key(secret)
    instant = int(_instant(time.time() if now is None else now))
    if not _label(user) or not isinstance(role, str) or role not in ROLES:
        raise ValueError("identità o ruolo non valido")
    if not _label(issuer) or not _label(audience) or type(ttl) is not int or not 1 <= ttl <= 3600:
        raise ValueError("contesto o ttl non valido")
    header = b64url(b'{"alg":"HS256","typ":"JWT"}')
    payload = b64url(json.dumps({"sub": user, "role": role, "iss": issuer, "aud": audience,
                                "iat": instant, "nbf": instant, "exp": instant + ttl},
                               separators=(",", ":")).encode())
    message = f"{header}.{payload}".encode("ascii")
    signature = b64url(hmac.new(key, message, hashlib.sha256).digest())
    return f"{header}.{payload}.{signature}"


def verify_token(token, secret, now=None, *, issuer=ISSUER, audience=AUDIENCE):
    key = _key(secret)
    instant = _instant(time.time() if now is None else now)
    if not _label(issuer) or not _label(audience):
        raise ValueError("contesto atteso non valido")
    if not isinstance(token, str) or not 1 <= len(token) <= 4096 or token.count(".") != 2:
        raise ValueError("token non valido")
    header, payload, signature = token.split(".")
    if _object(header) != {"alg": "HS256", "typ": "JWT"}:
        raise ValueError("header non supportato")
    # Decodificare rigorosamente prima dell'encoding ASCII evita eccezioni spurie.
    supplied = b64url_decode(signature)
    b64url_decode(payload)
    message = f"{header}.{payload}".encode("ascii")
    expected = hmac.new(key, message, hashlib.sha256).digest()
    if not hmac.compare_digest(expected, supplied):
        raise ValueError("firma non valida")
    claims = _object(payload)
    if set(claims) != {"sub", "role", "iss", "aud", "iat", "nbf", "exp"}:
        raise ValueError("insieme claim non supportato")
    if not _label(claims["sub"]) or not isinstance(claims["role"], str) or claims["role"] not in ROLES:
        raise ValueError("identità o ruolo non valido")
    if claims["iss"] != issuer or claims["aud"] != audience:
        raise ValueError("issuer o audience inatteso")
    if any(type(claims[name]) is not int for name in ("iat", "nbf", "exp")):
        raise ValueError("date intere richieste dal profilo")
    issued, not_before, expires = claims["iat"], claims["nbf"], claims["exp"]
    if not 0 <= issued <= not_before < expires or expires - issued > 3600:
        raise ValueError("intervallo token non valido")
    if instant < not_before or instant < issued:
        raise ValueError("token non ancora valido")
    if instant >= expires:
        raise ValueError("token scaduto")
    return claims


def authorized(payload, required_role):
    if not isinstance(payload, dict) or not isinstance(required_role, str) or required_role not in ROLES:
        return False
    role = payload.get("role")
    return isinstance(role, str) and role in ROLES and ROLES[role] >= ROLES[required_role]


class RateLimiter:
    """Finestra (now-window_s, now], richieste ammesse; solo un processo/thread."""
    def __init__(self, limit, window_s, max_keys=1000):
        if type(limit) is not int or limit <= 0 or type(max_keys) is not int or max_keys <= 0:
            raise ValueError("limit e max_keys interi positivi")
        self.window_s = _instant(window_s)
        if self.window_s <= 0:
            raise ValueError("finestra positiva")
        self.limit, self.max_keys = limit, max_keys
        # Il tempo reale usa monotonic(); il parametro now è solo per simulazioni.
        self.events = {}
        self.last_time = None

    def allow(self, key, now=None):
        if not _label(key):
            raise ValueError("chiave client non valida")
        instant = _instant(time.monotonic() if now is None else now)
        if self.last_time is not None and instant < self.last_time:
            raise ValueError("clock regressivo")
        # La differenza esatta evita che now - window arrotondi a now, o oltre
        # un evento ancora valido. Fraction(float) conserva il valore ricevuto.
        cutoff = Fraction(instant) - Fraction(self.window_s)
        self.last_time = instant
        for existing in list(self.events):
            queue = self.events[existing]
            while queue and queue[0] <= cutoff:
                queue.popleft()
            if not queue:
                del self.events[existing]
        if key not in self.events:
            if len(self.events) >= self.max_keys:
                return False
            self.events[key] = deque()
        queue = self.events[key]
        if len(queue) >= self.limit:
            return False
        queue.append(instant)
        return True


class ProtectedAPI:
    """Pipeline locale con esiti interi, nessun listener HTTP."""
    def __init__(self, secret, limiter):
        self.secret = _key(secret)
        self.limiter = limiter

    def request(self, client_key, token, required_role, *, now, rate_now):
        # client_key deve provenire da una fonte server fidata, non dal payload non verificato.
        if not self.limiter.allow(client_key, now=rate_now):
            return 429
        try:
            claims = verify_token(token, self.secret, now=now)
        except ValueError:
            return 401
        return 200 if authorized(claims, required_role) else 403


def demo():
    # Chiave pubblica e fissa esclusivamente per questo esempio riproducibile.
    key = b"p066-laboratorio-chiave-pubblica-32-byte"
    token = issue_token("anna", "operator", key, ttl=60, now=1000)
    api = ProtectedAPI(key, RateLimiter(3, 10))
    print("Lettura:", api.request("client-lab", token, "user", now=1001, rate_now=1))
    print("Amministrazione:", api.request("client-lab", token, "admin", now=1002, rate_now=2))
    print("Token a exp:", api.request("client-lab", token, "user", now=1060, rate_now=3))
    print("Limite richieste:", api.request("client-lab", token, "user", now=1003, rate_now=4))


if __name__ == "__main__":
    demo()
