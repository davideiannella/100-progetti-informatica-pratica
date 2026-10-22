"""Mini-SOC per log sintetici: parsing rigoroso, correlazione e triage esplicito."""
from collections import deque
from collections.abc import Mapping
from ipaddress import ip_address
import re
import shlex

_KEY = re.compile(r"[a-z_][a-z0-9_]*", re.ASCII)
_COUNTRY = re.compile(r"[A-Z]{2}", re.ASCII)
_EVENT_TYPES = frozenset({"login_failed", "admin_login", "login_success"})


def _text(value, name):
    if (not isinstance(value, str) or not value.strip() or len(value) > 256
            or any(ord(char) < 32 or ord(char) == 127 for char in value)):
        raise ValueError(f"campo {name} non valido")
    return value


def parse(line):
    """Una riga key=value; valori con spazi tra virgolette; chiavi univoche."""
    if (not isinstance(line, str) or not line.strip() or len(line) > 8192
            or any(ord(char) < 32 or ord(char) == 127 for char in line)):
        raise ValueError("riga non valida: vuota, troppo lunga o caratteri di controllo")
    tokens = shlex.split(line, posix=True)
    if len(tokens) > 32:
        raise ValueError("troppi campi")
    result = {}
    for token in tokens:
        if "=" not in token:
            raise ValueError("token senza uguale")
        key, value = token.split("=", 1)
        if _KEY.fullmatch(key) is None or key in result:
            raise ValueError("chiave non valida o duplicata")
        result[key] = _text(value, key)
    return result


def normalize(event):
    if not isinstance(event, Mapping) or len(event) > 32:
        raise ValueError("evento non valido")
    if any(not isinstance(key, str) or _KEY.fullmatch(key) is None for key in event):
        raise ValueError("chiave evento non valida")
    result = dict(event)
    for key in ("event", "src_ip", "user"):
        result[key] = _text(event.get(key), key)
    if result["event"] not in _EVENT_TYPES:
        raise ValueError("tipo evento non supportato")
    for key, value in result.items():
        if key != "ts":
            _text(value, key)
    value = event.get("ts")
    if isinstance(value, str) and re.fullmatch(r"[0-9]{1,19}", value, re.ASCII):
        value = int(value)
    if type(value) is not int or not 0 <= value <= 2**63 - 1:
        raise ValueError("ts: secondi interi non negativi, massimo 2**63-1")
    result["ts"] = value
    try:
        result["src_ip"] = str(ip_address(result["src_ip"]))
    except ValueError as exc:
        raise ValueError("src_ip non valido") from exc
    if "country" in result and _COUNTRY.fullmatch(result["country"]) is None:
        raise ValueError("country: due lettere ASCII maiuscole")
    return result


class Correlator:
    """Flusso globale ordinato; finestra chiusa; contatori esatti fino al limite."""
    def __init__(self, threshold=4, window=60, *, allowed_countries=("IT", "SM", "VA"),
                 max_sources=10000, max_events_per_source=10000):
        for name, value in (("threshold", threshold), ("window", window),
                            ("max_sources", max_sources), ("max_events_per_source", max_events_per_source)):
            if type(value) is not int or value < 1:
                raise ValueError(f"{name}: intero positivo")
        if threshold > max_events_per_source:
            raise ValueError("threshold supera la capacità per sorgente")
        if isinstance(allowed_countries, str):
            raise ValueError("allowed_countries: sequenza di codici")
        try:
            countries = tuple(allowed_countries)
        except TypeError as exc:
            raise ValueError("allowed_countries: sequenza di codici") from exc
        if not countries or any(not isinstance(c, str) or _COUNTRY.fullmatch(c) is None for c in countries):
            raise ValueError("allowed_countries non valido")
        self.threshold, self.window = threshold, window
        self.max_sources, self.max_events_per_source = max_sources, max_events_per_source
        self.allowed_countries = frozenset(countries)
        self.failed = {}
        self.last_ts = None

    def ingest(self, event):
        e = normalize(event)
        ts, ip = e["ts"], e["src_ip"]
        if self.last_ts is not None and ts < self.last_ts:
            raise ValueError("timestamp fuori ordine")
        for old_ip, queue in list(self.failed.items()):
            while queue and queue[0] < ts - self.window:
                queue.popleft()
            if not queue:
                del self.failed[old_ip]
        alerts = []
        if e["event"] == "login_failed":
            if ip not in self.failed:
                if len(self.failed) >= self.max_sources:
                    raise OverflowError("limite sorgenti attive raggiunto")
                self.failed[ip] = deque()
            queue = self.failed[ip]
            if len(queue) >= self.max_events_per_source:
                raise OverflowError("limite eventi per sorgente raggiunto")
            queue.append(ts)
            if len(queue) >= self.threshold:
                alerts.append({"rule": "repeated_login_failures", "src_ip": ip,
                               "count": len(queue), "ts": ts, "window": self.window})
        if e["event"] == "admin_login":
            if "country" not in e:
                alerts.append({"rule": "missing_country", "user": e["user"], "ts": ts})
            elif e["country"] not in self.allowed_countries:
                alerts.append({"rule": "admin_login_unusual_country", "user": e["user"],
                               "country": e["country"], "ts": ts})
        self.last_ts = ts
        return alerts


def process_lines(lines, correlator=None):
    """Conserva evidenza del rifiuto senza riportare la riga grezza o segreti."""
    correlator = Correlator() if correlator is None else correlator
    for number, line in enumerate(lines, 1):
        try:
            yield {"line": number, "alerts": correlator.ingest(parse(line))}
        except (ValueError, OverflowError) as exc:
            rule = "capacity_exceeded" if isinstance(exc, OverflowError) else "invalid_event"
            yield {"line": number, "alerts": [{"rule": rule, "reason": str(exc)}]}


def main():
    lines = [f"ts={ts} event=login_failed src_ip=203.0.113.9 user=alice" for ts in (0, 5, 10)]
    lines += ["ts=11 event=admin_login src_ip=198.51.100.2 user=alice country=US",
              "ts=12 event=admin_login src_ip=198.51.100.2 user=alice",
              "ts=13 event=login_failed event=admin_login"]
    for result in process_lines(lines, Correlator(3, 10)):
        print(f"riga {result['line']}:", [a["rule"] for a in result["alerts"]])


if __name__ == "__main__":
    main()
