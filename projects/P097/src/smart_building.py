"""Modello software di comfort e consumo: nessun impianto o allarme reale."""
import json
import math
import numbers


def _number(value, field, low, high):
    if isinstance(value, bool) or not isinstance(value, numbers.Real):
        raise ValueError(f"{field}: numero reale richiesto")
    try:
        value = float(value)
    except (OverflowError, ValueError) as exc:
        raise ValueError("numero fuori intervallo") from exc
    if not math.isfinite(value) or not low <= value <= high:
        raise ValueError(f"{field}: fuori intervallo")
    return value


class ZoneTwin:
    RATES = {"OFF": 0.1, "ECO": 0.3, "HEAT": 2.0, "COOL": 2.2}

    def __init__(self, name, temp=21, occupied=False):
        if not isinstance(name, str) or not name.strip() or name != name.strip():
            raise ValueError("nome zona non valido")
        self.name = name
        self.temp = temp
        self.occupied = occupied
        self._hvac = "OFF"
        self._energy_kwh = 0.0

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        self._temp = _number(value, "temperatura", -50, 60)

    @property
    def occupied(self):
        return self._occupied

    @occupied.setter
    def occupied(self, value):
        if type(value) is not bool:
            raise ValueError("occupied deve essere booleano")
        self._occupied = value

    @property
    def hvac(self):
        return self._hvac

    @property
    def energy_kwh(self):
        return self._energy_kwh

    def control(self, target=21, deadband=1):
        target = _number(target, "target", -50, 60)
        deadband = _number(deadband, "deadband", 0, 20)
        if not self.occupied:
            self._hvac = "ECO"
        elif self.temp < target - deadband:
            self._hvac = "HEAT"
        elif self.temp > target + deadband:
            self._hvac = "COOL"
        else:
            self._hvac = "OFF"
        return self.hvac

    def step_energy(self, hours=1):
        hours = _number(hours, "ore", 0, 1_000_000)
        total = self.energy_kwh + self.RATES[self.hvac] * hours
        if not math.isfinite(total):
            raise ValueError("energia non finita")
        self._energy_kwh = total
        return total


class Building:
    def __init__(self, zones):
        self.zones = tuple(zones)
        if not self.zones or any(not isinstance(z, ZoneTwin) for z in self.zones):
            raise ValueError("servono zone software valide")
        if len({z.name for z in self.zones}) != len(self.zones):
            raise ValueError("nomi zona duplicati")
        self._alerts = []

    @property
    def alerts(self):
        return list(self._alerts)

    def safety_event(self, kind):
        if not isinstance(kind, str) or kind not in {"smoke", "water"}:
            raise ValueError("evento virtuale non riconosciuto")
        self._alerts.append(kind)
        return {"local_alarm": True, "kind": kind, "simulation": True}


def demo():
    zone = ZoneTwin("ufficio", temp=18, occupied=True)
    heating = zone.control()
    zone.step_energy(1.5)
    zone.temp = 20
    boundary = zone.control()
    zone.step_energy(0.5)
    zone.occupied = False
    eco = zone.control()
    zone.step_energy(2)
    alarm = Building([zone]).safety_event("smoke")
    return {"mode": "modello_software", "heating": heating, "lower_boundary": boundary,
            "unoccupied": eco, "energy_kwh": round(zone.energy_kwh, 2), "alarm": alarm}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, sort_keys=True))
