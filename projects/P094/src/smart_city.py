"""Tre adattatori locali e indicatori di una città completamente sintetica."""
import copy
import json
import math
from statistics import mean


def _text(value, label):
    if type(value) is not str or not value.strip() or len(value) > 80:
        raise ValueError(f"{label}: testo non vuoto, massimo 80 caratteri.")
    return value


def _number(value, label):
    try:
        valid = type(value) in (int, float) and math.isfinite(value)
    except OverflowError:
        valid = False
    if not valid or value < 0:
        raise ValueError(f"{label}: numero finito non negativo richiesto.")
    return float(value)


def _mean(values):
    return mean(values) if values else None


class SmartCity:
    def __init__(self, parking_spaces):
        if type(parking_spaces) is not int or not 1 <= parking_spaces <= 100000:
            raise ValueError("Capacità intera fra 1 e 100000 richiesta.")
        self._parking = [False] * parking_spaces
        self._parking_ts = [-1] * parking_spaces
        self._events = {}
        self._traffic = []
        self._air = []

    @property
    def events(self):
        return copy.deepcopy(list(self._events.values()))

    def _record(self, kind, value, unit, event_id, ts, source, zone, **extra):
        if type(ts) is not int or ts < 0:
            raise ValueError("ts deve essere un intero non negativo, in secondi simulati.")
        return {"event_id": _text(event_id, "event_id"), "ts": ts,
                "source": _text(source, "source"), "zone": _text(zone, "zone"),
                "kind": kind, "value": value, "unit": unit, **extra}

    def _duplicate(self, record):
        previous = self._events.get(record["event_id"])
        if previous is None:
            return False
        if previous != record:
            raise ValueError("event_id riutilizzato con contenuto differente.")
        return True

    def set_parking(self, spot, occupied, *, event_id, ts,
                    source="parking-demo", zone="zona-demo"):
        if type(spot) is not int or not 0 <= spot < len(self._parking):
            raise ValueError("Stallo inesistente o identificativo non intero.")
        if type(occupied) is not bool:
            raise ValueError("occupied deve essere booleano.")
        record = self._record("parking", occupied, "boolean", event_id, ts,
                              source, zone, spot=spot)
        if self._duplicate(record):
            return False
        if ts <= self._parking_ts[spot]:
            raise ValueError("Evento parcheggio obsoleto o concorrente per lo stesso stallo.")
        self._events[event_id] = record
        self._parking[spot], self._parking_ts[spot] = occupied, ts
        return True

    def parking_free(self):
        return self._parking.count(False)

    def traffic_event(self, vehicles_per_min, *, event_id, ts,
                      source="traffic-demo", zone="zona-demo", unit="vehicles/min"):
        if unit != "vehicles/min":
            raise ValueError("Unità traffico richiesta: vehicles/min.")
        record = self._record("traffic", _number(vehicles_per_min, "traffic"), unit,
                              event_id, ts, source, zone)
        if self._duplicate(record):
            return False
        self._events[event_id] = record
        self._traffic.append(record["value"])
        return True

    def air_event(self, pm25, *, event_id, ts,
                  source="air-demo", zone="zona-demo", unit="ug/m3"):
        if unit != "ug/m3":
            raise ValueError("Unità PM2.5 richiesta: ug/m3.")
        record = self._record("air", _number(pm25, "pm25"), unit,
                              event_id, ts, source, zone)
        if self._duplicate(record):
            return False
        self._events[event_id] = record
        self._air.append(record["value"])
        return True

    def indicators(self, traffic_limit=80, pm25_limit=35):
        traffic_limit = _number(traffic_limit, "traffic_limit")
        pm25_limit = _number(pm25_limit, "pm25_limit")
        traffic_avg = _mean(self._traffic)
        pm25_avg = _mean(self._air)
        return {"parking_free": self.parking_free(), "parking_capacity": len(self._parking),
                "traffic_samples": len(self._traffic), "air_samples": len(self._air),
                "traffic_avg": traffic_avg, "pm25_avg": pm25_avg,
                "traffic_alert": traffic_avg > traffic_limit if traffic_avg is not None else None,
                "air_alert": pm25_avg > pm25_limit if pm25_avg is not None else None}

    def public_snapshot(self):
        # Allowlist: nessun ID evento, stallo, sorgente o timestamp individuale.
        return {"synthetic": True, "indicators": self.indicators(),
                "units": {"traffic_avg": "vehicles/min", "pm25_avg": "ug/m3"}}


def demo():
    city = SmartCity(4)
    city.set_parking(0, True, event_id="p0", ts=1)
    city.set_parking(1, True, event_id="p1", ts=1)
    for i, value in enumerate([70, 90, 100], 1):
        city.traffic_event(value, event_id=f"t{i}", ts=i)
    for i, value in enumerate([20, 40, 50], 1):
        city.air_event(value, event_id=f"a{i}", ts=i)
    duplicate_added = city.traffic_event(70, event_id="t1", ts=1)
    return {"simulation_only": True, "events_stored": len(city.events),
            "duplicate_added": duplicate_added, "public": city.public_snapshot(),
            "demonstration_limits": {"traffic_vehicles_min": 80, "pm25_ug_m3": 35}}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2, allow_nan=False))
