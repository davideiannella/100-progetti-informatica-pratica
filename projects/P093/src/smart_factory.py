"""KPI di macchine interamente sintetiche, senza bus o connessioni industriali."""
from dataclasses import dataclass
import json
import math

RELATIVE_TOLERANCE = 1e-12


def _bounded_ratio(numerator, denominator):
    ratio = numerator / denominator
    if ratio > 1 and math.isclose(numerator, denominator,
                                  rel_tol=RELATIVE_TOLERANCE, abs_tol=0):
        return 1.0
    return ratio


def _finite(value, label, positive=False):
    try:
        valid = type(value) in (int, float) and math.isfinite(value)
    except OverflowError:
        valid = False
    if not valid or (value <= 0 if positive else value < 0):
        raise ValueError(f"{label}: numero finito {'positivo' if positive else 'non negativo'} richiesto.")
    return float(value)


@dataclass(frozen=True)
class MachineTwin:
    name: str
    planned_min: float
    runtime_min: float
    total_count: int
    good_count: int
    ideal_cycle_min: float
    vibration: float  # Intensità sintetica, in mm/s; nessun sensore reale.

    def __post_init__(self):
        if type(self.name) is not str or not self.name.strip() or len(self.name) > 64:
            raise ValueError("Nome macchina non vuoto, massimo 64 caratteri.")
        planned = _finite(self.planned_min, "planned_min", positive=True)
        runtime = _finite(self.runtime_min, "runtime_min")
        cycle = _finite(self.ideal_cycle_min, "ideal_cycle_min", positive=True)
        _finite(self.vibration, "vibration")
        for count in (self.total_count, self.good_count):
            if type(count) is not int or not 0 <= count <= 2**31 - 1:
                raise ValueError("Conteggi interi non negativi, massimo 2**31-1.")
        if (runtime > planned and not math.isclose(runtime, planned,
                rel_tol=RELATIVE_TOLERANCE, abs_tol=0)) or self.good_count > self.total_count:
            raise ValueError("Runtime o conteggi incoerenti.")
        ideal_time = cycle * self.total_count
        if ideal_time > runtime and not math.isclose(ideal_time, runtime,
                rel_tol=RELATIVE_TOLERANCE, abs_tol=0):
            raise ValueError("Produzione incompatibile con runtime e ciclo ideale.")

    def oee(self):
        availability = _bounded_ratio(self.runtime_min, self.planned_min)
        performance = (_bounded_ratio(self.ideal_cycle_min * self.total_count, self.runtime_min)
                       if self.runtime_min else 0.0)
        quality = self.good_count / self.total_count if self.total_count else 0.0
        return {"availability": availability, "performance": performance,
                "quality": quality, "oee": availability * performance * quality}

    def maintenance_signal(self, limit=4.0):
        return self.vibration > _finite(limit, "limit")


class Plant:
    def __init__(self, machines):
        self.machines = tuple(machines)
        if any(not isinstance(machine, MachineTwin) for machine in self.machines):
            raise ValueError("Sono richiesti MachineTwin.")
        names = [machine.name for machine in self.machines]
        if len(names) != len(set(names)):
            raise ValueError("I nomi delle macchine devono essere univoci.")

    def summary(self, vibration_limit=4.0):
        limit = _finite(vibration_limit, "vibration_limit")
        values = [machine.oee()["oee"] for machine in self.machines]
        return {"machines": len(values),
                "mean_oee": math.fsum(values) / len(values) if values else None,
                "maintenance": [m.name for m in self.machines if m.maintenance_signal(limit)]}


def demo():
    machines = [MachineTwin("M1", 480, 420, 380, 370, 1.0, 2.0),
                MachineTwin("M2", 480, 400, 350, 330, 1.0, 5.2)]
    return {"simulation_only": True,
            "units": {"time": "min", "counts": "pezzi", "vibration": "mm/s",
                      "oee": "frazione 0..1"},
            "metrics": [{"name": m.name, **m.oee()} for m in machines],
            "summary": Plant(machines).summary(), "vibration_limit_mm_s": 4.0}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2, allow_nan=False))
