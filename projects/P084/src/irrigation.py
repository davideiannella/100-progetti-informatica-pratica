"""Gemello didattico: percentuali simulate, passo temporale convenzionale."""

import json
import math
from numbers import Real


def _number(value, name, minimum=0.0, maximum=None):
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name}: serve un numero reale finito.")
    try:
        value = float(value)
    except (OverflowError, ValueError) as error:
        raise ValueError(f"{name}: valore non rappresentabile.") from error
    if not math.isfinite(value) or value < minimum or (maximum is not None and value > maximum):
        raise ValueError(f"{name}: valore fuori intervallo.")
    return value


class IrrigationTwin:
    def __init__(self, moisture=45.0, on_below=30.0, off_above=45.0):
        self.moisture = _number(moisture, "moisture", maximum=100.0)
        self.on_below = _number(on_below, "on_below", maximum=100.0)
        self.off_above = _number(off_above, "off_above", maximum=100.0)
        if self.on_below >= self.off_above:
            raise ValueError("Le soglie richiedono on_below < off_above.")
        self.pump = False
        self._history = []

    @property
    def history(self):
        return [record.copy() for record in self._history]

    def step(self, rain=0.0, evaporation=1.0):
        rain = _number(rain, "rain")
        evaporation = _number(evaporation, "evaporation")
        previous_pump = self.pump
        irrigation = 5.0 if previous_pump else 0.0
        self.moisture = max(0.0, min(100.0, self.moisture + rain - evaporation + irrigation))
        reason = "hold"
        if not self.pump and self.moisture < self.on_below:
            self.pump, reason = True, "below_on_threshold"
        elif self.pump and self.moisture > self.off_above:
            self.pump, reason = False, "above_off_threshold"
        record = {"step": len(self._history) + 1, "moisture": self.moisture,
                  "previous_pump": previous_pump, "irrigation": irrigation,
                  "pump": self.pump, "reason": reason}
        self._history.append(record.copy())
        return record


def demo():
    twin = IrrigationTwin(31.0)
    for evaporation in (1, 1, 0, 0, 0, 0, 1):
        twin.step(evaporation=evaporation)
    return {"on_below": twin.on_below, "off_above": twin.off_above,
            "comparison": "moisture < on_below; moisture > off_above",
            "history": twin.history}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2))
