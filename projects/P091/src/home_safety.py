"""Macchina a stati didattica: tutti i sensori e gli attuatori sono simulati."""
import copy
import json


class SafetyController:
    def __init__(self):
        self.state = "NORMAL"
        self.actions = []
        self._sample = (False, False)
        self._audit = []
        self._pending = []
        self._delivered = []

    @property
    def audit(self):
        return copy.deepcopy(self._audit)

    @property
    def pending(self):
        return copy.deepcopy(self._pending)

    @property
    def delivered(self):
        return copy.deepcopy(self._delivered)

    def ingest(self, smoke=False, water=False, cloud_online=True):
        """Restituisce stato e azioni desiderate; non comanda dispositivi reali."""
        if any(type(value) is not bool for value in (smoke, water, cloud_online)):
            raise ValueError("I tre ingressi devono essere booleani.")
        state = "FIRE_ALERT" if smoke else "WATER_ALERT" if water else "NORMAL"
        actions = []
        if smoke:
            actions.extend(["sound_virtual_alarm", "cut_virtual_nonessential_power"])
        if water:
            actions.append("close_virtual_valve")
        previous = self.state
        self.state, self.actions = state, actions
        if (smoke, water) != self._sample:
            event = {"sequence": len(self._audit) + 1, "previous": previous,
                     "state": state, "smoke": smoke, "water": water,
                     "local_actions": list(actions)}
            self._audit.append(event)
            self._pending.append(copy.deepcopy(event))
            self._sample = (smoke, water)
        # La decisione locale è già avvenuta: questa è solo una consegna in RAM.
        if cloud_online:
            self._delivered.extend(self._pending)
            self._pending.clear()
        return self.state, list(self.actions)


def demo():
    controller = SafetyController()
    samples = [(False, False, True), (False, True, False),
               (True, True, False), (True, True, True),
               (False, True, True), (False, False, True)]
    rows = []
    for smoke, water, online in samples:
        state, actions = controller.ingest(smoke, water, online)
        rows.append({"smoke": smoke, "water": water, "cloud_online": online,
                     "state": state, "local_actions": actions,
                     "pending": len(controller.pending),
                     "delivered": len(controller.delivered)})
    return {"simulation_only": True, "samples": rows, "audit": controller.audit}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2))
