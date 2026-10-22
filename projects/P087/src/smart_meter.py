"""Integrazione rettangolare di potenze simulate e raccolta locale idempotente."""
from dataclasses import dataclass, asdict
import json
import math
import numbers


def _number(value, name):
    if isinstance(value, bool) or not isinstance(value, numbers.Real):
        raise ValueError(f"{name}: numero reale richiesto")
    try:
        value = float(value)
    except (OverflowError, ValueError) as exc:
        raise ValueError(f"{name}: numero non finito") from exc
    if not math.isfinite(value) or value < 0:
        raise ValueError(f"{name}: numero finito non negativo richiesto")
    return value


def _identifier(value):
    if (not isinstance(value, str) or not value.strip()
            or value != value.strip() or len(value) > 64):
        raise ValueError("identificativo non valido")
    return value


@dataclass(frozen=True)
class Sample:
    event_id: str
    device: str
    start_s: float
    end_s: float
    power_kw: float
    delta_kwh: float
    total_kwh: float


def validate(sample):
    if not isinstance(sample, Sample):
        raise ValueError("atteso Sample")
    _identifier(sample.event_id)
    _identifier(sample.device)
    for name in ("start_s", "end_s", "power_kw", "delta_kwh", "total_kwh"):
        _number(getattr(sample, name), name)
    if sample.end_s <= sample.start_s:
        raise ValueError("intervallo temporale non positivo")
    expected = sample.power_kw * ((sample.end_s - sample.start_s) / 3600)
    if not math.isfinite(expected) or (sample.power_kw > 0 and expected == 0):
        raise ValueError("energia non rappresentabile")
    if not math.isclose(sample.delta_kwh, expected, rel_tol=1e-12, abs_tol=0):
        raise ValueError("delta_kwh incoerente con potenza e durata")
    if sample.total_kwh < sample.delta_kwh:
        raise ValueError("totale minore del delta")
    return True


class Meter:
    def __init__(self, device, start_s=0, initial_kwh=0):
        self.device = _identifier(device)
        self._time = _number(start_s, "start_s")
        self._kwh = _number(initial_kwh, "initial_kwh")
        self._events = {}

    @property
    def total_kwh(self):
        return self._kwh

    def sample(self, event_id, power_kw, end_s):
        event_id = _identifier(event_id)
        power_kw = _number(power_kw, "power_kw")
        end_s = _number(end_s, "end_s")
        if event_id in self._events:
            old = self._events[event_id]
            if old.power_kw != power_kw or old.end_s != end_s:
                raise ValueError("event_id riutilizzato con dati diversi")
            return old
        if end_s <= self._time:
            raise ValueError("end_s deve aumentare")
        delta = power_kw * ((end_s - self._time) / 3600)
        total = self._kwh + delta
        if not math.isfinite(delta) or not math.isfinite(total):
            raise ValueError("overflow dell'energia")
        if power_kw > 0 and (delta == 0 or total <= self._kwh):
            raise ValueError("incremento di energia non rappresentabile")
        sample = Sample(event_id, self.device, self._time, end_s, power_kw, delta, total)
        validate(sample)
        self._events[event_id] = sample
        self._time, self._kwh = end_s, total
        return sample


class Collector:
    def __init__(self, device, start_s=0, initial_kwh=0, power_alert_kw=1.8):
        self.device = _identifier(device)
        self._start = self._end = _number(start_s, "start_s")
        self._initial = self._total = _number(initial_kwh, "initial_kwh")
        self._power_limit = _number(power_alert_kw, "power_alert_kw")
        self._events = {}
        self._history = []

    @property
    def history(self):
        return tuple(self._history)

    def ingest(self, sample):
        validate(sample)
        if sample.device != self.device:
            raise ValueError("device inatteso")
        if sample.event_id in self._events:
            if sample != self._events[sample.event_id]:
                raise ValueError("event_id in conflitto")
            return False
        if sample.start_s != self._end:
            raise ValueError("intervallo mancante, sovrapposto o fuori ordine")
        expected_total = self._total + sample.delta_kwh
        if (sample.total_kwh < self._total
                or (sample.delta_kwh > 0 and sample.total_kwh <= self._total)
                or not math.isfinite(expected_total)
                or not math.isclose(sample.total_kwh, expected_total,
                                    rel_tol=1e-12, abs_tol=0)):
            raise ValueError("totale cumulato incoerente")
        self._history.append(sample)
        self._events[sample.event_id] = sample
        self._end, self._total = sample.end_s, sample.total_kwh
        return True

    def summary(self):
        hours = (self._end - self._start) / 3600
        energy = math.fsum(s.delta_kwh for s in self._history)
        return {"samples": len(self._history), "total_kwh": self._total,
                "period_kwh": energy, "duration_s": self._end - self._start,
                "average_kw": energy / hours if hours else None,
                "max_kw": max((s.power_kw for s in self._history), default=None),
                "power_alerts": sum(s.power_kw > self._power_limit for s in self._history)}


def demo():
    meter, collector = Meter("meter-01"), Collector("meter-01")
    samples = [meter.sample("e1", 1, 1800), meter.sample("e2", 2, 5400),
               meter.sample("e3", 1.5, 7200)]
    collector.ingest(samples[0])
    duplicate_ignored = not collector.ingest(samples[0])
    try:
        collector.ingest(samples[2])
    except ValueError as exc:
        missing_interval_error = str(exc)
    for sample in samples[1:]:
        collector.ingest(sample)
    return {"mode": "simulazione_locale", "samples": [asdict(s) for s in samples],
            "duplicate_ignored": duplicate_ignored,
            "missing_interval_error": missing_interval_error, "summary": collector.summary()}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2, allow_nan=False))
