"""Capstone locale: metadati manuali, MAC HMAC e transazioni SQLite.

Non contiene classificatore ML, immagini, server HTTP, dashboard o cloud.
"""
from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib
import hmac
import json
import math
import numbers
import re
import secrets
import sqlite3


ALLOWED_CLASSES = {"carta", "plastica", "vetro", "metallo", "organico", "indifferenziato"}
FIELDS = {"event_id", "device_id", "event_type", "created_at", "waste_class", "confidence", "fill_pct"}


def _identifier(value):
    if not isinstance(value, str) or re.fullmatch(r"[A-Za-z0-9_-]{1,64}", value) is None:
        raise ValueError("identificativo non valido")
    return value


def _secret(value):
    if not isinstance(value, str) or len(value) < 32:
        raise ValueError("segreto di almeno 32 caratteri richiesto")
    return value


def _number(value, field_name, low, high):
    if isinstance(value, bool) or not isinstance(value, numbers.Real):
        raise ValueError(f"{field_name}: numero reale richiesto")
    try:
        value = float(value)
    except (OverflowError, ValueError) as exc:
        raise ValueError("numero fuori intervallo") from exc
    if not math.isfinite(value) or not low <= value <= high:
        raise ValueError(f"{field_name}: fuori intervallo")
    return value


def _validate_payload(payload):
    if not isinstance(payload, dict) or set(payload) != FIELDS:
        raise ValueError("schema: ammessi soltanto i sette campi dei metadati")
    _identifier(payload["device_id"])
    _identifier(payload["event_id"])
    if payload["event_type"] != "classification":
        raise ValueError("tipo evento non supportato")
    if not isinstance(payload["waste_class"], str) or payload["waste_class"] not in ALLOWED_CLASSES:
        raise ValueError("classe rifiuto non valida")
    _number(payload["confidence"], "confidence", 0, 1)
    _number(payload["fill_pct"], "fill_pct", 0, 100)
    timestamp = payload["created_at"]
    if not isinstance(timestamp, str) or len(timestamp) > 40:
        raise ValueError("timestamp non valido")
    try:
        instant = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("timestamp ISO 8601 richiesto") from exc
    if instant.tzinfo is None or instant.utcoffset() is None:
        raise ValueError("timestamp con fuso orario richiesto")
    return dict(payload)


@dataclass(frozen=True)
class Device:
    device_id: str
    secret: str = field(repr=False)


class DeviceRegistry:
    def __init__(self):
        self._devices = {}

    def register(self, device_id, secret=None):
        _identifier(device_id)
        if device_id in self._devices:
            raise ValueError("device già registrato")
        secret = secrets.token_hex(32) if secret is None else _secret(secret)
        device = Device(device_id, secret)
        self._devices[device_id] = device
        return device

    def get(self, device_id):
        _identifier(device_id)
        try:
            return self._devices[device_id]
        except KeyError as exc:
            raise PermissionError("device sconosciuto") from exc


class EventSigner:
    @staticmethod
    def canonical_payload(payload):
        if not isinstance(payload, dict) or any(not isinstance(k, str) for k in payload):
            raise ValueError("oggetto JSON con chiavi stringa richiesto")
        try:
            return json.dumps(payload, sort_keys=True, separators=(",", ":"),
                              ensure_ascii=False, allow_nan=False).encode("utf-8")
        except (TypeError, ValueError) as exc:
            raise ValueError("payload JSON finito richiesto") from exc

    @classmethod
    def sign(cls, payload, secret):
        _secret(secret)
        return hmac.new(secret.encode("utf-8"), cls.canonical_payload(payload), hashlib.sha256).hexdigest()

    @classmethod
    def verify(cls, payload, secret, signature):
        if not isinstance(signature, str) or re.fullmatch(r"[0-9a-f]{64}", signature) is None:
            return False
        return hmac.compare_digest(cls.sign(payload, secret), signature)


class EventStore:
    def __init__(self, db_path=":memory:"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript("""
            PRAGMA foreign_keys=ON;
            CREATE TABLE IF NOT EXISTS device_event(
                device_id TEXT NOT NULL, event_id TEXT NOT NULL,
                event_type TEXT NOT NULL CHECK(event_type='classification'),
                waste_class TEXT NOT NULL, confidence REAL NOT NULL CHECK(confidence BETWEEN 0 AND 1),
                fill_pct REAL NOT NULL CHECK(fill_pct BETWEEN 0 AND 100),
                created_at TEXT NOT NULL, payload_json TEXT NOT NULL,
                PRIMARY KEY(device_id,event_id)
            );
            CREATE TABLE IF NOT EXISTS alert(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                device_id TEXT NOT NULL, event_id TEXT NOT NULL,
                severity TEXT NOT NULL, message TEXT NOT NULL, created_at TEXT NOT NULL,
                UNIQUE(device_id,event_id),
                FOREIGN KEY(device_id,event_id) REFERENCES device_event(device_id,event_id)
            );
        """)
        self.conn.commit()

    def _create_alert(self, payload):
        self.conn.execute(
            "INSERT INTO alert(device_id,event_id,severity,message,created_at) VALUES(?,?,?,?,?)",
            (payload["device_id"], payload["event_id"], "warning",
             f"Contenitore al {float(payload['fill_pct']):.0f}%", payload["created_at"]),
        )

    def append(self, payload):
        payload = _validate_payload(payload)
        canonical = EventSigner.canonical_payload(payload).decode("utf-8")
        with self.conn:
            row = self.conn.execute(
                "SELECT payload_json FROM device_event WHERE device_id=? AND event_id=?",
                (payload["device_id"], payload["event_id"]),
            ).fetchone()
            if row is not None:
                if row["payload_json"] != canonical:
                    raise ValueError("event_id riutilizzato con contenuto diverso")
                return False
            self.conn.execute(
                """INSERT INTO device_event(device_id,event_id,event_type,waste_class,confidence,
                   fill_pct,created_at,payload_json) VALUES(?,?,?,?,?,?,?,?)""",
                (payload["device_id"], payload["event_id"], payload["event_type"], payload["waste_class"],
                 payload["confidence"], payload["fill_pct"], payload["created_at"], canonical),
            )
            if payload["fill_pct"] >= 80:
                self._create_alert(payload)
        return True

    def count_events(self):
        return self.conn.execute("SELECT COUNT(*) FROM device_event").fetchone()[0]

    def alerts(self):
        return [dict(row) for row in self.conn.execute("SELECT * FROM alert ORDER BY id")]

    def waste_counts(self):
        return {row["waste_class"]: row["n"] for row in self.conn.execute(
            "SELECT waste_class, COUNT(*) n FROM device_event GROUP BY waste_class ORDER BY waste_class")}

    def close(self):
        self.conn.close()


class SmartWastePlatform:
    ALLOWED_CLASSES = ALLOWED_CLASSES

    def __init__(self, registry, store):
        self.registry, self.store = registry, store

    def ingest(self, payload, signature):
        payload = _validate_payload(payload)
        device = self.registry.get(payload["device_id"])
        if not EventSigner.verify(payload, device.secret, signature):
            raise PermissionError("MAC HMAC non valido")
        inserted = self.store.append(payload)
        return {"accepted": True, "inserted": inserted}


def new_classification_event(device_id, event_id, waste_class, confidence, fill_pct, created_at=None):
    # Metadati forniti dal chiamante, non risultati di un modello eseguito qui.
    return _validate_payload({
        "event_id": event_id, "device_id": device_id, "event_type": "classification",
        "waste_class": waste_class, "confidence": confidence, "fill_pct": fill_pct,
        "created_at": datetime.now(timezone.utc).isoformat() if created_at is None else created_at,
    })


def demo():
    registry = DeviceRegistry()
    device = registry.register("BIN-001")
    store = EventStore()
    platform = SmartWastePlatform(registry, store)
    timestamp = "2026-10-21T10:00:00+00:00"
    first = new_classification_event("BIN-001", "E1", "carta", 0.92, 80, timestamp)
    second = new_classification_event("BIN-001", "E2", "vetro", 0.84, 35, timestamp)
    try:
        a = platform.ingest(first, EventSigner.sign(first, device.secret))
        b = platform.ingest(first, EventSigner.sign(first, device.secret))
        platform.ingest(second, EventSigner.sign(second, device.secret))
        return {"mode": "metadati_manuali_HMAC_SQLite", "first_inserted": a["inserted"],
                "retry_inserted": b["inserted"], "events": store.count_events(),
                "alerts": len(store.alerts()), "counts": store.waste_counts(), "storage": ":memory:"}
    finally:
        store.close()


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, sort_keys=True))
