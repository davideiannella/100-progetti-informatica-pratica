"""Store-and-forward in RAM; ACK e deduplica sono simulati con chiamate locali."""
from copy import deepcopy
import json
import math
import numbers


def _device(value):
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise ValueError("device non valido")
    return value


def _event(event):
    if not isinstance(event, dict) or set(event) != {"device", "seq", "value"}:
        raise ValueError("schema evento non valido")
    _device(event["device"])
    if type(event["seq"]) is not int or event["seq"] < 1:
        raise ValueError("seq deve essere intero positivo")
    value = event["value"]
    if isinstance(value, bool) or not isinstance(value, numbers.Real):
        raise ValueError("misura numerica finita richiesta")
    try:
        finite = math.isfinite(value)
    except (OverflowError, ValueError) as exc:
        raise ValueError("misura fuori intervallo") from exc
    if not finite:
        raise ValueError("misura numerica finita richiesta")
    return deepcopy(event)


class Collector:
    def __init__(self):
        self._received = {}
        self._last_seq = {}

    @property
    def events(self):
        return deepcopy(list(self._received.values()))

    def ingest(self, event):
        event = _event(event)
        key = (event["device"], event["seq"])
        inserted = key not in self._received
        if not inserted:
            if self._received[key] != event:
                raise ValueError("identificativo duplicato con contenuto diverso")
        else:
            expected = self._last_seq.get(event["device"], 0) + 1
            if event["seq"] != expected:
                raise ValueError("sequenza fuori ordine: atteso " + str(expected))
            self._received[key] = event
            self._last_seq[event["device"]] = event["seq"]
        return {"ack": True, "device": key[0], "seq": key[1], "inserted": inserted}


class EdgeNode:
    def __init__(self, device):
        self.device = _device(device)
        self._seq = 0
        self._buffer = []
        self.online = True

    @property
    def buffer(self):
        return deepcopy(self._buffer)

    @property
    def seq(self):
        return self._seq

    @property
    def online(self):
        return self._online

    @online.setter
    def online(self, value):
        if type(value) is not bool:
            raise ValueError("online deve essere booleano")
        self._online = value

    def sample(self, value):
        event = _event({"device": self.device, "seq": self.seq + 1, "value": value})
        self._seq += 1
        self._buffer.append(event)
        return deepcopy(event)

    def flush(self, collector):
        if not self.online:
            return 0
        acknowledged = 0
        while self._buffer:
            event = self._buffer[0]
            try:
                ack = collector.ingest(deepcopy(event))
            except (ConnectionError, TimeoutError, OSError):
                self.online = False
                break
            if (not isinstance(ack, dict) or ack.get("ack") is not True
                    or ack.get("device") != event["device"]
                    or type(ack.get("seq")) is not int or ack["seq"] != event["seq"]):
                raise ValueError("ACK assente o non corrispondente")
            self._buffer.pop(0)
            acknowledged += 1
        return acknowledged


def demo():
    node, collector = EdgeNode("env-1"), Collector()
    node.online = False
    first = node.sample(10)
    node.sample(11)
    offline = node.flush(collector)
    node.online = True
    acknowledged = node.flush(collector)
    replay = collector.ingest(first)
    return {"mode": "buffer_in_memoria", "offline_ack": offline,
            "reconnect_ack": acknowledged, "pending": len(node.buffer),
            "sequence": [e["seq"] for e in collector.events], "replay_inserted": replay["inserted"]}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, sort_keys=True))
