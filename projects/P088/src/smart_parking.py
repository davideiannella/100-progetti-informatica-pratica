"""Eventi di parcheggio sintetici, stato locale e audit in memoria."""
from dataclasses import dataclass, asdict
import json
import math
import numbers


def _identifier(value):
    if (not isinstance(value, str) or not value.strip()
            or value != value.strip() or len(value) > 64):
        raise ValueError("identificativo non valido")
    return value


def _integer(value, name, low, high):
    if isinstance(value, bool) or not isinstance(value, numbers.Integral) or not low <= value <= high:
        raise ValueError(f"{name}: intero tra {low} e {high} richiesto")
    return int(value)


@dataclass(frozen=True)
class ParkingEvent:
    event_id: str
    kind: str
    timestamp_s: float
    spot: int
    vehicle_id: str


@dataclass(frozen=True)
class EventResult:
    event_id: str
    status: str
    reason: str
    occupied: int
    available: int
    dwell_s: float | None = None


class Parking:
    def __init__(self, capacity):
        self.capacity = _integer(capacity, "capacity", 1, 10000)
        self._spots = {i: None for i in range(1, self.capacity + 1)}
        self._entered = {}
        self._last_time = None
        self._events = {}
        self._results = {}
        self._audit = []

    @property
    def audit(self):
        return tuple(self._audit)

    def snapshot(self):
        return dict(self._spots)

    def available(self):
        return sum(value is None for value in self._spots.values())

    def _validate(self, event):
        if not isinstance(event, ParkingEvent):
            raise ValueError("atteso ParkingEvent")
        _identifier(event.event_id)
        _identifier(event.vehicle_id)
        if not isinstance(event.kind, str) or event.kind not in ("enter", "exit"):
            raise ValueError("kind deve essere enter o exit")
        _integer(event.spot, "spot", 1, self.capacity)
        if isinstance(event.timestamp_s, bool) or not isinstance(event.timestamp_s, numbers.Real):
            raise ValueError("timestamp_s numerico richiesto")
        try:
            timestamp = float(event.timestamp_s)
        except (OverflowError, ValueError) as exc:
            raise ValueError("timestamp_s non finito") from exc
        if not math.isfinite(timestamp) or timestamp < 0:
            raise ValueError("timestamp_s finito non negativo richiesto")

    def apply(self, event):
        self._validate(event)
        if event.event_id in self._events:
            if event != self._events[event.event_id]:
                raise ValueError("event_id riutilizzato con contenuto diverso")
            return self._results[event.event_id]
        reason, dwell = "ok", None
        occupant = self._spots[event.spot]
        if self._last_time is not None and event.timestamp_s < self._last_time:
            reason = "out_of_order"
        elif event.kind == "enter":
            if occupant is not None:
                reason = "spot_occupied"
            elif event.vehicle_id in self._spots.values():
                reason = "vehicle_already_inside"
        elif occupant is None:
            reason = "spot_empty"
        elif occupant != event.vehicle_id:
            reason = "vehicle_mismatch"
        if reason == "ok":
            if event.kind == "enter":
                self._spots[event.spot] = event.vehicle_id
                self._entered[event.spot] = event.timestamp_s
            else:
                dwell = event.timestamp_s - self._entered.pop(event.spot)
                self._spots[event.spot] = None
            self._last_time = event.timestamp_s
        free = self.available()
        result = EventResult(event.event_id, "accepted" if reason == "ok" else "rejected",
                             reason, self.capacity - free, free, dwell)
        self._events[event.event_id] = event
        self._results[event.event_id] = result
        self._audit.append((event, result))
        return result


def demo():
    parking = Parking(2)
    events = [ParkingEvent("e1", "enter", 0, 1, "auto-A"),
              ParkingEvent("e2", "enter", 10, 2, "auto-B"),
              ParkingEvent("e3", "enter", 20, 1, "auto-C"),
              ParkingEvent("e4", "exit", 70, 1, "auto-A"),
              ParkingEvent("e5", "exit", 80, 1, "auto-A"),
              ParkingEvent("e6", "enter", 60, 1, "auto-C"),
              ParkingEvent("e7", "enter", 90, 1, "auto-C")]
    results = [parking.apply(event) for event in events]
    same_result = parking.apply(events[0]) == results[0]
    return {"mode": "simulazione_locale", "capacity": parking.capacity,
            "results": [asdict(result) for result in results],
            "duplicate_same_result": same_result, "audit_events": len(parking.audit),
            "snapshot": parking.snapshot(), "available": parking.available()}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2, allow_nan=False))
