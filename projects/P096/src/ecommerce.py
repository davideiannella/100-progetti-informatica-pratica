"""Simulazione monoprocesso: nessuna API, pagamento o transazione distribuita."""
from copy import deepcopy
from contextlib import contextmanager
import json


def _text(value, field):
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise ValueError(f"{field}: stringa non vuota, senza spazi esterni")
    return value


def _quantity(value, *, positive=False):
    if type(value) is not int or value < (1 if positive else 0):
        raise ValueError("quantità intera non negativa (positiva per gli ordini)")
    return value


class EventBus:
    def __init__(self):
        self._events = []

    @property
    def events(self):
        return deepcopy(self._events)

    def publish(self, event):
        if not isinstance(event, dict):
            raise ValueError("evento non valido")
        self._events.append(deepcopy(event))


class Catalog:
    def __init__(self):
        self._products = {}

    @property
    def products(self):
        return deepcopy(self._products)

    def add(self, sku, name, category):
        for value, field in ((sku, "sku"), (name, "name"), (category, "category")):
            _text(value, field)
        if sku in self._products:
            raise ValueError("SKU già presente")
        self._products[sku] = {"name": name, "category": category}


class Inventory:
    def __init__(self):
        self._stock = {}

    @property
    def stock(self):
        return self._stock.copy()

    def set(self, sku, qty):
        _text(sku, "sku")
        self._stock[sku] = _quantity(qty)

    def reserve(self, sku, qty):
        _text(sku, "sku")
        _quantity(qty, positive=True)
        if self._stock.get(sku, 0) < qty:
            return False
        self._stock[sku] -= qty
        return True


class Orders:
    def __init__(self, inventory, bus):
        self.inventory = inventory
        self.bus = bus
        self._orders = {}

    @property
    def orders(self):
        return deepcopy(self._orders)

    @contextmanager
    def _local_change(self):
        # Ripristino locale dimostrativo, senza concorrenza o broker esterno.
        snapshot = (self.inventory._stock.copy(), deepcopy(self._orders), self.bus.events)
        try:
            yield
        except Exception:
            self.inventory._stock, self._orders, self.bus._events = snapshot
            raise

    def create(self, order_id, sku, qty):
        _text(order_id, "order_id")
        _text(sku, "sku")
        _quantity(qty, positive=True)
        if order_id in self._orders:
            old = self._orders[order_id]
            if (old["sku"], old["qty"]) != (sku, qty):
                raise ValueError("order_id riutilizzato con dati diversi")
            return deepcopy(old)
        with self._local_change():
            if not self.inventory.reserve(sku, qty):
                raise ValueError("stock insufficiente")
            self._orders[order_id] = {"sku": sku, "qty": qty, "status": "CONFIRMED"}
            self.bus.publish({"type": "OrderConfirmed", "order_id": order_id, "sku": sku, "qty": qty})
        return deepcopy(self._orders[order_id])

    def _transition(self, order_id, target, required):
        _text(order_id, "order_id")
        if order_id not in self._orders:
            raise ValueError("ordine sconosciuto")
        order = self._orders[order_id]
        if order["status"] == target:
            return deepcopy(order)
        if order["status"] != required:
            raise ValueError("transizione non consentita")
        with self._local_change():
            if target == "REFUNDED":
                self.inventory._stock[order["sku"]] += order["qty"]
            order["status"] = target
            self.bus.publish({"type": "Order" + target.title(), "order_id": order_id})
        return deepcopy(order)

    def ship(self, order_id):
        return self._transition(order_id, "SHIPPED", "CONFIRMED")

    def deliver(self, order_id):
        return self._transition(order_id, "DELIVERED", "SHIPPED")

    def refund(self, order_id):
        # Cancellazione prima della spedizione: nessun rimborso monetario reale.
        return self._transition(order_id, "REFUNDED", "CONFIRMED")


def recommend_same_category(catalog, sku):
    _text(sku, "sku")
    products = catalog.products
    if sku not in products:
        raise ValueError("SKU sconosciuto")
    category = products[sku]["category"]
    return sorted(key for key, value in products.items()
                  if key != sku and value["category"] == category)


def demo():
    catalog = Catalog()
    for args in (("A", "SSD 1 TB", "storage"), ("B", "SSD 2 TB", "storage"), ("C", "Mouse", "input")):
        catalog.add(*args)
    stock, bus = Inventory(), EventBus()
    stock.set("A", 5)
    orders = Orders(stock, bus)
    orders.create("O1", "A", 2)
    after_create = stock.stock["A"]
    orders.create("O1", "A", 2)
    orders.refund("O1")
    orders.refund("O1")
    return {"mode": "simulazione_monoprocesso", "stock_after_create": after_create,
            "stock_after_refund": stock.stock["A"], "status": orders.orders["O1"]["status"],
            "events": len(bus.events), "recommendations": recommend_same_category(catalog, "A")}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, sort_keys=True))
