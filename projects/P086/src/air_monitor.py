"""Telemetria ambientale interamente locale; soglie soltanto didattiche."""
from dataclasses import dataclass
import json
import math
import numbers

UNITS = ("ug/m3", "ppm", "degC", "%")


def _number(value, name, low, high):
    if isinstance(value, bool) or not isinstance(value, numbers.Real):
        raise ValueError(f"{name}: atteso numero reale, esclusi i booleani")
    try:
        number = float(value)
    except (OverflowError, ValueError) as exc:
        raise ValueError(f"{name}: valore non finito") from exc
    if not math.isfinite(number) or not low <= number <= high:
        raise ValueError(f"{name}: valore fuori intervallo")
    return number


@dataclass(frozen=True)
class Reading:
    device: str
    timestamp_s: float
    pm25: float
    co2: float
    temperature: float
    humidity: float
    units: tuple = UNITS


def validate(reading):
    if not isinstance(reading, Reading):
        raise ValueError("attesa una Reading")
    if (not isinstance(reading.device, str) or not reading.device.strip()
            or reading.device != reading.device.strip() or len(reading.device) > 64):
        raise ValueError("device non valido")
    if not isinstance(reading.units, tuple) or reading.units != UNITS:
        raise ValueError("unità richieste: ug/m3, ppm, degC, %")
    _number(reading.timestamp_s, "timestamp_s", 0, math.inf)
    _number(reading.pm25, "pm25", 0, 1000)
    _number(reading.co2, "co2", 250, 10000)
    _number(reading.temperature, "temperature", -50, 80)
    _number(reading.humidity, "humidity", 0, 100)
    return True


def alerts(reading, pm25_limit=35, co2_limit=1000):
    validate(reading)
    pm25_limit = _number(pm25_limit, "pm25_limit", 0, 1000)
    co2_limit = _number(co2_limit, "co2_limit", 250, 10000)
    out = []
    if reading.pm25 > pm25_limit:
        out.append("pm25")
    if reading.co2 > co2_limit:
        out.append("co2")
    return out


class AirMonitor:
    def __init__(self, pm25_limit=35, co2_limit=1000):
        self._pm25_limit = _number(pm25_limit, "pm25_limit", 0, 1000)
        self._co2_limit = _number(co2_limit, "co2_limit", 250, 10000)
        self._history = []
        self._last_time = {}
        self._alert_events = []

    @property
    def history(self):
        return tuple(self._history)

    @property
    def alert_events(self):
        return tuple(self._alert_events)

    def ingest(self, reading):
        validate(reading)
        previous = self._last_time.get(reading.device)
        if previous is not None and reading.timestamp_s <= previous:
            raise ValueError("timestamp non strettamente crescente per il device")
        triggered = alerts(reading, self._pm25_limit, self._co2_limit)
        self._history.append(reading)
        self._last_time[reading.device] = reading.timestamp_s
        for metric in triggered:
            self._alert_events.append((reading.device, reading.timestamp_s, metric))
        return triggered

    def summary(self):
        out = {"samples": len(self._history), "alerts": len(self._alert_events)}
        for metric in ("pm25", "co2", "temperature", "humidity"):
            values = [float(getattr(r, metric)) for r in self._history]
            out[metric] = {"mean": math.fsum(values) / len(values) if values else None,
                           "max": max(values) if values else None}
        return out


def demo():
    monitor = AirMonitor()
    readings = [Reading("aria-A", 0, 12, 650, 21, 45),
                Reading("aria-A", 60, 42, 1200, 23, 47),
                Reading("aria-B", 0, 35, 1000, 22, 50)]
    for reading in readings:
        monitor.ingest(reading)
    return {"mode": "simulazione_locale", "units": UNITS,
            "summary": monitor.summary(), "alert_events": monitor.alert_events}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2, allow_nan=False))
