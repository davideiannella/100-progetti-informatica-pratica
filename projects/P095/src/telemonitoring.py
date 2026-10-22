"""Workflow tecnico con metriche fittizie: nessuna validazione o regola clinica."""
from dataclasses import dataclass
import copy
import json
import math

PERMISSIONS = {"ingestor": {"ingest"}, "viewer": {"view"},
               "reviewer": {"view", "close"}}


def _text(value, label, maximum=80):
    if type(value) is not str or not value.strip() or len(value) > maximum:
        raise ValueError(f"{label}: testo non vuoto, massimo {maximum} caratteri.")
    return value


def _finite(value):
    try:
        valid = type(value) in (int, float) and math.isfinite(value)
    except OverflowError:
        valid = False
    if not valid:
        raise ValueError("Valore numerico finito richiesto.")
    normalized = float(value)
    if type(value) is int and int(normalized) != value:
        raise ValueError("Intero non rappresentabile esattamente come float.")
    return normalized


@dataclass(frozen=True)
class VitalReading:
    patient_code: str
    metric: str
    value: float
    ts: int
    event_id: str
    unit: str = "demo_unit"

    def __post_init__(self):
        _text(self.patient_code, "patient_code")
        if not self.patient_code.startswith("SYN-") or len(self.patient_code) == 4:
            raise ValueError("Usare un codice sintetico con prefisso SYN-.")
        _text(self.metric, "metric")
        _text(self.event_id, "event_id")
        object.__setattr__(self, "value", _finite(self.value))
        if type(self.ts) is not int or self.ts < 0:
            raise ValueError("ts deve essere un intero non negativo, secondi simulati.")
        if self.unit != "demo_unit":
            raise ValueError("Si accetta soltanto l'unità artificiale demo_unit.")


class Monitor:
    def __init__(self, ranges, users):
        if type(ranges) is not dict or not ranges:
            raise ValueError("Configurare almeno una metrica fittizia.")
        self._ranges = {}
        for metric, bounds in ranges.items():
            _text(metric, "metric")
            if type(bounds) not in (tuple, list) or len(bounds) != 2:
                raise ValueError("Ogni intervallo richiede due estremi.")
            low, high = map(_finite, bounds)
            if low > high:
                raise ValueError("Intervallo invertito.")
            self._ranges[metric] = (low, high)
        if type(users) is not dict or not users:
            raise ValueError("Mappa esplicita utenti-ruoli richiesta.")
        self._users = {}
        for actor, role in users.items():
            _text(actor, "actor")
            if type(role) is not str or role not in PERMISSIONS:
                raise ValueError("Ruolo sconosciuto.")
            self._users[actor] = role
        self._events = {}
        self._readings = {}
        self._audit = []

    @property
    def audit(self):
        return copy.deepcopy(self._audit)

    def _authorize(self, actor, action):
        _text(actor, "actor")
        allowed = action in PERMISSIONS.get(self._users.get(actor), set())
        if not allowed:
            self._audit.append({"actor": actor, "action": action, "result": "denied"})
            raise PermissionError("Operazione non concessa dal ruolo simulato.")

    def ingest(self, reading, actor):
        self._authorize(actor, "ingest")
        if not isinstance(reading, VitalReading):
            raise ValueError("VitalReading richiesta.")
        if reading.metric not in self._ranges:
            raise ValueError("Metrica sconosciuta.")
        existing = self._readings.get(reading.event_id)
        if existing is not None:
            if existing != reading:
                raise ValueError("event_id riutilizzato con contenuto differente.")
            return copy.deepcopy(self._events[reading.event_id])
        low, high = self._ranges[reading.metric]
        status = "OK" if low <= reading.value <= high else "REVIEW"
        event = {"event_id": reading.event_id, "patient_code": reading.patient_code,
                 "metric": reading.metric, "value": float(reading.value),
                 "unit": reading.unit, "ts": reading.ts, "status": status,
                 "requires_human_review": status == "REVIEW",
                 "review_state": "PENDING" if status == "REVIEW" else "NOT_REQUIRED"}
        self._readings[reading.event_id] = reading
        self._events[reading.event_id] = event
        self._audit.append({"actor": actor, "action": "ingest", "event_id": reading.event_id,
                            "result": status})
        return copy.deepcopy(event)

    def view_events(self, actor):
        self._authorize(actor, "view")
        self._audit.append({"actor": actor, "action": "view", "result": "allowed"})
        return copy.deepcopy(list(self._events.values()))

    def close_review(self, event_id, actor, note):
        self._authorize(actor, "close")
        _text(event_id, "event_id")
        _text(note, "note", maximum=200)
        if event_id not in self._events:
            raise ValueError("Evento sconosciuto.")
        event = self._events[event_id]
        if event["status"] != "REVIEW":
            raise ValueError("L'evento non richiede revisione.")
        if event["review_state"] == "CLOSED":
            if event["reviewed_by"] != actor or event["review_note"] != note:
                raise ValueError("Revisione già chiusa con contenuto differente.")
            return copy.deepcopy(event)
        event.update(review_state="CLOSED", requires_human_review=False,
                     reviewed_by=actor, review_note=note)
        self._audit.append({"actor": actor, "action": "close", "event_id": event_id,
                            "result": "CLOSED"})
        return copy.deepcopy(event)


def demo():
    monitor = Monitor({"metric_a": (10, 20), "metric_b": (100, 200)},
                      {"service-demo": "ingestor", "viewer-demo": "viewer",
                       "reviewer-demo": "reviewer"})
    samples = [VitalReading("SYN-001", "metric_a", 15, 1, "e1"),
               VitalReading("SYN-001", "metric_a", 25, 2, "e2"),
               VitalReading("SYN-002", "metric_b", 100, 3, "e3")]
    before = [monitor.ingest(reading, "service-demo") for reading in samples]
    monitor.close_review("e2", "reviewer-demo", "Controllo tecnico dimostrativo concluso.")
    return {"synthetic_only": True, "clinical_validation": False,
            "artificial_ranges": {"metric_a": [10, 20], "metric_b": [100, 200]},
            "before_review": before, "after_review": monitor.view_events("viewer-demo"),
            "audit": monitor.audit}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2, allow_nan=False))
