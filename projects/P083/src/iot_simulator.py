"""Telemetria locale: pub/sub in memoria, non protocollo MQTT."""

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import itertools
import json
import math
from numbers import Real
import random
import re
from typing import Callable

SCHEMA = "telemetry.v1"
FIELDS = {"schema", "device_id", "seq", "temperature_c", "humidity_pct", "timestamp"}
MAX_PAYLOAD = 32_000


def _device(value):
    if not isinstance(value, str) or re.fullmatch(r"[A-Za-z0-9_-]{1,64}", value) is None:
        raise ValueError("device_id richiede 1–64 lettere ASCII, cifre, _ o -.")
    return value


def _real(value, name, minimum, maximum):
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name}: serve un numero finito.")
    try:
        value = float(value)
    except (OverflowError, ValueError) as error:
        raise ValueError(f"{name}: valore non rappresentabile.") from error
    if not math.isfinite(value) or not minimum <= value <= maximum:
        raise ValueError(f"{name}: valore fuori intervallo.")
    return value


def _sequence(value):
    if type(value) is not int or value < 0:
        raise ValueError("seq richiede un intero non negativo, esclusi i booleani.")
    return value


def _timestamp(value):
    if not isinstance(value, str) or len(value) > 64:
        raise ValueError("timestamp richiede una stringa ISO 8601 UTC.")
    try:
        stamp = datetime.fromisoformat(value)
    except ValueError as error:
        raise ValueError("timestamp non interpretabile.") from error
    if stamp.tzinfo is None or stamp.utcoffset() != timedelta(0):
        raise ValueError("timestamp richiede un offset UTC esplicito.")
    return stamp.astimezone(timezone.utc).isoformat()


def _topic_device(topic):
    if not isinstance(topic, str):
        raise ValueError("Topic non valido.")
    match = re.fullmatch(r"devices/([A-Za-z0-9_-]{1,64})/telemetry", topic)
    if match is None:
        raise ValueError("Topic atteso: devices/<device_id>/telemetry.")
    return match.group(1)


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Chiave JSON duplicata.")
        result[key] = value
    return result


@dataclass(frozen=True)
class Telemetry:
    device_id: str
    seq: int
    temperature_c: float
    humidity_pct: float
    timestamp: str

    def __post_init__(self):
        _device(self.device_id)
        _sequence(self.seq)
        object.__setattr__(self, "temperature_c", _real(self.temperature_c, "temperature_c", -50, 80))
        object.__setattr__(self, "humidity_pct", _real(self.humidity_pct, "humidity_pct", 0, 100))
        object.__setattr__(self, "timestamp", _timestamp(self.timestamp))

    def to_json(self):
        return json.dumps({
            "schema": SCHEMA, "device_id": self.device_id, "seq": self.seq,
            "temperature_c": round(self.temperature_c, 2),
            "humidity_pct": round(self.humidity_pct, 2), "timestamp": self.timestamp,
        }, separators=(",", ":"), sort_keys=True, allow_nan=False)


class VirtualBroker:
    """Distribuzione sincrona per topic esatto: nessuna rete o garanzia MQTT."""
    def __init__(self):
        self._subs = {}
        self._online = True

    @property
    def online(self):
        return self._online

    @online.setter
    def online(self, value):
        if type(value) is not bool:
            raise ValueError("online richiede True oppure False.")
        self._online = value

    def subscribe(self, topic, callback):
        _topic_device(topic)
        if not callable(callback):
            raise ValueError("Il subscriber deve essere una funzione richiamabile.")
        callbacks = self._subs.setdefault(topic, [])
        if callback in callbacks:
            raise ValueError("Subscriber già registrato sul topic.")
        callbacks.append(callback)

    def publish(self, topic, payload):
        _topic_device(topic)
        if not isinstance(payload, str) or len(payload) > MAX_PAYLOAD:
            raise ValueError("Payload non valido o troppo lungo.")
        if not self.online:
            raise ConnectionError("Broker non disponibile")
        for callback in tuple(self._subs.get(topic, ())):
            callback(topic, payload)


class SensorSimulator:
    def __init__(self, device_id, broker, seed=42, clock: Callable[[], datetime] | None = None):
        self.device_id = _device(device_id)
        if not isinstance(broker, VirtualBroker) or type(seed) is not int:
            raise ValueError("Servono un VirtualBroker e un seed intero.")
        if clock is not None and not callable(clock):
            raise ValueError("clock deve essere richiamabile.")
        self.broker = broker
        self.rng = random.Random(seed)
        self.clock = clock if clock is not None else lambda: datetime.now(timezone.utc)
        self.seq = 0
        self.pending = []

    def sample(self):
        stamp = self.clock()
        if not isinstance(stamp, datetime):
            raise ValueError("clock deve restituire un datetime UTC.")
        timestamp = _timestamp(stamp.isoformat())
        phase = self.seq / 8.0
        temperature = 22.0 + 2.5 * math.sin(phase) + self.rng.uniform(-0.2, 0.2)
        humidity = 48.0 + 6.0 * math.cos(phase / 2) + self.rng.uniform(-0.5, 0.5)
        item = Telemetry(self.device_id, self.seq, temperature,
                         max(0.0, min(100.0, humidity)), timestamp)
        self.seq += 1
        return item

    def publish_once(self):
        self.pending.append(self.sample())
        try:
            self.flush_pending()
        except ConnectionError:
            return False
        return True

    def flush_pending(self):
        sent = 0
        topic = f"devices/{self.device_id}/telemetry"
        while self.pending:
            item = self.pending[0]
            self.broker.publish(topic, item.to_json())
            self.pending.pop(0)
            sent += 1
        return sent


class Collector:
    def __init__(self):
        self._messages = []
        self._seen = {}
        self._last_seq = {}

    @property
    def messages(self):
        return [item.copy() for item in self._messages]

    def on_message(self, topic, payload):
        device = _topic_device(topic)
        if not isinstance(payload, str) or len(payload) > MAX_PAYLOAD:
            raise ValueError("Payload non valido o troppo lungo.")
        try:
            data = json.loads(payload, object_pairs_hook=_unique_object)
        except (ValueError, RecursionError) as error:
            raise ValueError("JSON non valido o con chiavi duplicate.") from error
        if not isinstance(data, dict) or set(data) != FIELDS or data["schema"] != SCHEMA:
            raise ValueError("Campi o schema non supportati.")
        item = Telemetry(data["device_id"], data["seq"], data["temperature_c"],
                         data["humidity_pct"], data["timestamp"])
        if device != item.device_id:
            raise ValueError("device_id e topic non corrispondono.")
        normalized = {"schema": SCHEMA, "device_id": item.device_id, "seq": item.seq,
                      "temperature_c": item.temperature_c, "humidity_pct": item.humidity_pct,
                      "timestamp": item.timestamp}
        key = (item.device_id, item.seq)
        if key in self._seen:
            if self._seen[key] != normalized:
                raise ValueError("Stessa chiave evento con contenuto diverso.")
            return False
        if item.seq <= self._last_seq.get(item.device_id, -1):
            raise ValueError("Evento nuovo fuori ordine.")
        self._seen[key] = normalized.copy()
        self._last_seq[item.device_id] = item.seq
        self._messages.append(normalized)
        return True


def demo():
    broker, collector = VirtualBroker(), Collector()
    topic = "devices/S01/telemetry"
    broker.subscribe(topic, collector.on_message)
    ticks = itertools.count()
    start = datetime(2026, 10, 21, 12, 0, tzinfo=timezone.utc)
    sensor = SensorSimulator("S01", broker, seed=7,
                             clock=lambda: start + timedelta(seconds=next(ticks)))
    broker.online = False
    offline_results = [sensor.publish_once(), sensor.publish_once()]
    broker.online = True
    reconnected = sensor.publish_once()
    first_payload = json.dumps(collector.messages[0])
    duplicate_added = collector.on_message(topic, first_payload)
    return {"mode": "in_memory_pubsub", "offline_results": offline_results,
            "reconnected": reconnected, "pending": len(sensor.pending),
            "duplicate_added": duplicate_added, "messages": collector.messages}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2))
