"""Componenti logistici locali: routing, stock, tracking e baseline separati."""
from copy import deepcopy
import heapq
import json
import math
import numbers


def _text(value):
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise ValueError("identificativo non valido")
    return value


def _number(value, *, positive=False):
    if isinstance(value, bool) or not isinstance(value, numbers.Real):
        raise ValueError("numero reale richiesto")
    try:
        value = float(value)
    except (OverflowError, ValueError) as exc:
        raise ValueError("numero fuori intervallo") from exc
    if not math.isfinite(value) or value < 0 or (positive and value == 0):
        raise ValueError("numero finito non negativo richiesto")
    return value


class Warehouse:
    def __init__(self):
        self._stock = {}

    @property
    def stock(self):
        return self._stock.copy()

    @staticmethod
    def _quantity(qty, minimum):
        if type(qty) is not int or qty < minimum:
            raise ValueError("quantità intera fuori intervallo")
        return qty

    def set(self, sku, qty):
        _text(sku)
        self._stock[sku] = self._quantity(qty, 0)

    def allocate(self, sku, qty):
        _text(sku)
        self._quantity(qty, 1)
        if self._stock.get(sku, 0) < qty:
            return False
        self._stock[sku] -= qty
        return True


def shortest(graph, start, target):
    if not isinstance(graph, dict) or not graph:
        raise ValueError("grafo vuoto o non valido")
    for node in graph:
        _text(node)
    validated = {}
    for node, edges in graph.items():
        if not isinstance(edges, (list, tuple)):
            raise ValueError("archi non validi")
        validated[node] = []
        for edge in edges:
            if not isinstance(edge, (list, tuple)) or len(edge) != 2:
                raise ValueError("arco non valido")
            nxt, weight = edge
            _text(nxt)
            if nxt not in graph:
                raise ValueError("destinazione mancante nel grafo")
            validated[node].append((nxt, _number(weight)))
    _text(start)
    _text(target)
    if start not in graph or target not in graph:
        raise ValueError("nodo sconosciuto")
    queue, seen = [(0.0, start, [])], set()
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in seen:
            continue
        seen.add(node)
        path = path + [node]
        if node == target:
            return cost, path
        for nxt, weight in sorted(validated[node]):
            total = cost + weight
            if not math.isfinite(total):
                raise ValueError("costo non finito")
            if nxt not in seen:
                heapq.heappush(queue, (total, nxt, path))
    raise ValueError("destinazione irraggiungibile")


def moving_average(values, k=3):
    if type(k) is not int or k <= 0 or not isinstance(values, (list, tuple)) or len(values) < k:
        raise ValueError("storico o finestra non validi")
    values = [_number(value) for value in values]
    window = values[-k:]
    scale = max(window)
    if scale == 0:
        return 0.0
    # Termini in [0, 1]: la somma non cresce con la grandezza dei campioni.
    fraction = math.fsum(value / scale for value in window) / k
    # La media di valori non negativi non può superare il massimo.
    result = scale * min(fraction, 1.0)
    if not math.isfinite(result):
        raise ValueError("media non finita")
    return result


def eta_minutes(distance_km, speed_kmh, handling_minutes=0):
    distance = _number(distance_km)
    speed = _number(speed_kmh, positive=True)
    handling = _number(handling_minutes)
    result = distance / speed * 60 + handling
    if not math.isfinite(result):
        raise ValueError("ETA non finita")
    return result


class Shipment:
    NEXT = {None: "PICKED", "PICKED": "IN_TRANSIT", "IN_TRANSIT": "DELIVERED"}

    def __init__(self, id):
        self.id = _text(id)
        self._events = []
        self._by_id = {}

    @property
    def events(self):
        return deepcopy(self._events)

    def update(self, status, ts, event_id):
        _text(event_id)
        _text(status)
        ts = _number(ts)
        event = {"event_id": event_id, "status": status, "ts": ts}
        if event_id in self._by_id:
            if self._by_id[event_id] != event:
                raise ValueError("event_id riutilizzato con dati diversi")
            return False
        current = self._events[-1]["status"] if self._events else None
        if self.NEXT.get(current) != status:
            raise ValueError("transizione tracking non consentita")
        if self._events and ts <= self._events[-1]["ts"]:
            raise ValueError("timestamp non crescente")
        self._events.append(event)
        self._by_id[event_id] = event
        return True


def demo():
    warehouse = Warehouse()
    warehouse.set("SKU1", 10)
    warehouse.allocate("SKU1", 4)
    graph = {"WH": [("HUB", 5), ("DEST", 15)], "HUB": [("DEST", 6)], "DEST": []}
    cost, path = shortest(graph, "WH", "DEST")
    shipment = Shipment("S1")
    shipment.update("PICKED", 1, "T1")
    shipment.update("IN_TRANSIT", 2, "T2")
    shipment.update("IN_TRANSIT", 2, "T2")
    return {"stock": warehouse.stock["SKU1"], "route_minutes": cost, "path": path,
            "forecast_units": moving_average([10, 12, 14, 16], 3),
            "eta_separate_example_minutes": eta_minutes(22, 44, 5),
            "tracking_events": len(shipment.events), "status": shipment.events[-1]["status"]}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, sort_keys=True))
