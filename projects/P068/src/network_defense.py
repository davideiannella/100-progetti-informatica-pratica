"""Modello di policy direzionale e detector; non modifica il firewall host."""
from collections import deque
from ipaddress import ip_address
from math import isfinite
from types import MappingProxyType

RULES = MappingProxyType({
    ("internet", "dmz", "https"): True,
    ("dmz", "app", "https"): True,
    ("app", "db", "postgres"): True,
    ("internet", "db", "postgres"): False,
    ("guest", "management", "ssh"): False,
})


def firewall(src, dst, service):
    """Valuta una tripla; tuple non dichiarate e input malformati sono negati."""
    if any(not isinstance(value, str) or not value for value in (src, dst, service)):
        return False
    return RULES.get((src, dst, service), False)


def _number(value, name, positive=False):
    if type(value) not in (int, float):
        raise ValueError(f"{name}: numero richiesto")
    try:
        finite = isfinite(value)
    except OverflowError:
        finite = False
    if not finite or value < 0 or (positive and value == 0):
        raise ValueError(f"{name}: numero finito {'positivo' if positive else 'non negativo'}")
    return value


class FailedLoginDetector:
    """Flusso globale in ordine non decrescente; finestra chiusa [ts-window, ts].

    Memoria massima: max_sources * threshold timestamp; conserva solo gli
    ultimi threshold eventi di ogni IP, sufficienti alla risposta booleana.
    """
    def __init__(self, threshold=5, window=60, max_sources=10000):
        if type(threshold) is not int or threshold < 1:
            raise ValueError("threshold: intero positivo")
        if type(max_sources) is not int or max_sources < 1:
            raise ValueError("max_sources: intero positivo")
        self.threshold = threshold
        self.window = _number(window, "window", positive=True)
        self.max_sources = max_sources
        self.events = {}
        self.last_ts = None

    def record(self, ip, ts):
        if not isinstance(ip, str):
            raise ValueError("ip: indirizzo testuale")
        try:
            key = str(ip_address(ip))
        except ValueError as exc:
            raise ValueError("ip non valido") from exc
        ts = _number(ts, "ts")
        if self.last_ts is not None and ts < self.last_ts:
            raise ValueError("timestamp fuori ordine")
        # Il cleanup usa un watermark globale; non espelle eventi al bordo.
        for old_key, queue in list(self.events.items()):
            while queue and queue[0] < ts - self.window:
                queue.popleft()
            if not queue:
                del self.events[old_key]
        if key not in self.events:
            if len(self.events) >= self.max_sources:
                raise OverflowError("limite sorgenti attive raggiunto")
            self.events[key] = deque(maxlen=self.threshold)
        self.events[key].append(ts)
        self.last_ts = ts
        return len(self.events[key]) >= self.threshold


def main():
    print("Internet -> DMZ HTTPS:", firewall("internet", "dmz", "https"))
    print("Internet -> DB PostgreSQL:", firewall("internet", "db", "postgres"))
    detector = FailedLoginDetector(3, 10)
    for ts in (0, 5, 10, 21):
        print(f"t={ts}: alert={detector.record('203.0.113.1', ts)}")


if __name__ == "__main__":
    main()
