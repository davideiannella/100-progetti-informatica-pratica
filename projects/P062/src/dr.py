"""Modello in memoria, singolo writer: replica asincrona e failover di sola lettura."""
from copy import deepcopy
from dataclasses import dataclass
import math


def _time(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("tempo numerico finito >= 0")
    try:
        result = float(value)
    except OverflowError as exc:
        raise ValueError("tempo troppo grande") from exc
    if not math.isfinite(result) or result < 0:
        raise ValueError("tempo numerico finito >= 0")
    return result


@dataclass(frozen=True)
class Change:
    sequence: int
    when: float
    key: str
    value: object


class Zone:
    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise ValueError("nome zona")
        self.name, self.up, self.data = name, True, {}

    def write(self, key, value):
        if not self.up:
            raise RuntimeError("zona non disponibile")
        if not isinstance(key, str) or not key:
            raise ValueError("chiave non vuota")
        self.data[key] = deepcopy(value)

    def read(self, key):
        if not self.up:
            raise RuntimeError("zona non disponibile")
        return deepcopy(self.data[key])


class ReplicatedService:
    def __init__(self, primary, secondary, *, start_time=0):
        if primary is secondary or primary.name == secondary.name:
            raise ValueError("servono due zone distinte")
        if primary.data or secondary.data:
            raise ValueError("il modello parte da zone vuote")
        self.primary, self.secondary = primary, secondary
        self.last_time = _time(start_time)
        self.recovery_point = self.last_time
        self.journal = []
        self.acked = 0

    def write(self, key, value, *, now=None):
        when = self.last_time + 1 if now is None else _time(now)
        if when < self.last_time:
            raise ValueError("tempo regressivo")
        self.primary.write(key, value)
        self.journal.append(Change(len(self.journal) + 1, when, key, deepcopy(value)))
        self.last_time = when
        if self.secondary.up:
            self.catch_up()

    def catch_up(self):
        if not self.primary.up or not self.secondary.up:
            raise RuntimeError("recupero replica richiede entrambe le zone")
        for change in self.journal[self.acked:]:
            self.secondary.write(change.key, change.value)
            self.acked = change.sequence
            self.recovery_point = change.when

    def read(self, key):
        zone = self.primary if self.primary.up else self.secondary
        return zone.read(key), zone.name

    def exposure(self, *, incident_time):
        incident = _time(incident_time)
        if incident < self.last_time:
            raise ValueError("incidente precedente all'ultima scrittura")
        pending = self.journal[self.acked:]
        # Finestra del punto recuperabile; non conta quante righe sono perse.
        return {"pending_writes": len(pending),
                "affected_keys": sorted({entry.key for entry in pending}),
                "recovery_point": self.recovery_point,
                "potential_loss_window_s": incident - self.recovery_point if pending else 0.0}


def rpo_lost_keys(primary, secondary):
    """Compatibilità: chiavi mancanti O con valore obsoleto, non un RPO temporale."""
    return sorted(key for key, value in primary.data.items()
                  if key not in secondary.data or secondary.data[key] != value)


def recovery_duration(incident_time, recovered_time):
    incident, recovered = _time(incident_time), _time(recovered_time)
    if recovered < incident:
        raise ValueError("ripristino prima dell'incidente")
    return recovered - incident


def demo():
    a, b = Zone("zona-a"), Zone("zona-b")
    service = ReplicatedService(a, b)
    service.write("ordine-1", "ricevuto", now=10)
    b.up = False
    service.write("ordine-1", "spedito", now=20)
    print("Esposizione:", service.exposure(incident_time=25))
    b.up, a.up = True, False
    print("Failover di lettura:", service.read("ordine-1"))
    print("Durata ripristino simulata:", recovery_duration(25, 28), "s")
    a.up = True
    service.catch_up()
    print("Divergenze dopo recupero:", rpo_lost_keys(a, b))


if __name__ == "__main__":
    demo()
