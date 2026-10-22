"""SLI locali: una Metrics rappresenta una finestra scelta dal chiamante."""
from dataclasses import dataclass, field
import json
import math


def _finite_nonnegative(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(name)
    try:
        result = float(value)
    except OverflowError as exc:
        raise ValueError(name) from exc
    if not math.isfinite(result) or result < 0:
        raise ValueError(name)
    return result


@dataclass
class Metrics:
    requests: int = field(default=0, init=False)
    errors: int = field(default=0, init=False)
    latency_ms_total: float = field(default=0.0, init=False)

    def record(self, latency_ms, ok=True):
        latency = _finite_nonnegative(latency_ms, "latenza finita >= 0")
        if type(ok) is not bool:
            raise ValueError("ok deve essere bool")
        new_total = self.latency_ms_total + latency
        if not math.isfinite(new_total):
            raise ValueError("overflow della latenza totale")
        # Validare prima di modificare: un evento rifiutato non altera gli SLI.
        self.requests += 1
        self.errors += int(not ok)
        self.latency_ms_total = new_total

    @property
    def availability(self):
        return None if self.requests == 0 else (self.requests - self.errors) / self.requests

    @property
    def avg_latency(self):
        return None if self.requests == 0 else self.latency_ms_total / self.requests


def alerts(m: Metrics, availability_slo=0.99, latency_slo_ms=250):
    target = _finite_nonnegative(availability_slo, "SLO disponibilità")
    latency_target = _finite_nonnegative(latency_slo_ms, "SLO latenza")
    if target > 1:
        raise ValueError("SLO disponibilità tra 0 e 1")
    if not isinstance(m, Metrics):
        raise TypeError("Metrics richiesta")
    if m.requests == 0:
        return ["no_data"]
    out = []
    if m.availability < target:
        out.append("availability")
    if m.avg_latency > latency_target:
        out.append("latency")
    return out


def request_event(trace_id, component, latency_ms, ok=True):
    """Log strutturato minimale: nessun URL, credenziale o corpo della richiesta."""
    for value in (trace_id, component):
        if not isinstance(value, str) or not value or len(value) > 64:
            raise ValueError("identificatore non valido")
    latency = _finite_nonnegative(latency_ms, "latenza")
    if type(ok) is not bool:
        raise ValueError("ok deve essere bool")
    return json.dumps({"trace_id": trace_id, "component": component,
                       "latency_ms": latency, "ok": ok}, ensure_ascii=True, sort_keys=True)


def demo():
    m = Metrics()
    print("Finestra vuota:", alerts(m))
    for value in (100, 120, 80, 150):
        m.record(value)
    print(f"Richieste={m.requests}; disponibilità={m.availability:.2%}; media={m.avg_latency:.1f} ms")
    print("Alert:", alerts(m))
    print(request_event("trace-lab-1", "catalogo", 500, False))
    m.record(500, False)
    print(f"Dopo il guasto: disponibilità={m.availability:.2%}; alert={alerts(m)}")


if __name__ == "__main__":
    demo()
