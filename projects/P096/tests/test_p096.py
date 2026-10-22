import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ecommerce import Catalog, Inventory, EventBus, Orders, recommend_same_category, demo


class EcommerceTests(unittest.TestCase):
    def setUp(self):
        self.stock, self.bus = Inventory(), EventBus()
        self.stock.set("A", 5)
        self.orders = Orders(self.stock, self.bus)

    def test_create_reserves_once_and_publishes(self):
        result = self.orders.create("O1", "A", 2)
        self.assertEqual(result, {"sku": "A", "qty": 2, "status": "CONFIRMED"})
        self.assertEqual(self.stock.stock["A"], 3)
        self.assertEqual(self.bus.events, [{"type": "OrderConfirmed", "order_id": "O1", "sku": "A", "qty": 2}])

    def test_retry_is_idempotent(self):
        first = self.orders.create("O1", "A", 2)
        self.assertEqual(self.orders.create("O1", "A", 2), first)
        self.assertEqual((self.stock.stock["A"], len(self.bus.events)), (3, 1))

    def test_retry_conflict_leaves_all_state_unchanged(self):
        self.orders.create("O1", "A", 2)
        snapshot = (self.stock.stock, self.orders.orders, self.bus.events)
        for sku, qty in (("A", 3), ("B", 2)):
            with self.subTest(sku=sku, qty=qty), self.assertRaises(ValueError):
                self.orders.create("O1", sku, qty)
        self.assertEqual((self.stock.stock, self.orders.orders, self.bus.events), snapshot)

    def test_insufficient_and_unknown_stock_do_not_create(self):
        for sku, qty in (("A", 6), ("UNKNOWN", 1)):
            with self.subTest(sku=sku), self.assertRaises(ValueError):
                self.orders.create("O1", sku, qty)
        self.assertEqual((self.stock.stock, self.orders.orders, self.bus.events), ({"A": 5}, {}, []))

    def test_invalid_order_quantities_are_rejected_before_mutation(self):
        for qty in (0, -1, True, 1.5, float("nan"), float("inf"), "2", None):
            with self.subTest(qty=qty), self.assertRaises(ValueError):
                self.orders.create("O1", "A", qty)
        self.assertEqual((self.stock.stock["A"], self.orders.orders, self.bus.events), (5, {}, []))

    def test_invalid_identifiers_are_rejected(self):
        for value in ("", " ", " A", None, True, []):
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.orders.create(value, "A", 1)
            with self.subTest(sku=value), self.assertRaises(ValueError):
                self.stock.set(value, 1)

    def test_inventory_set_requires_nonnegative_integer(self):
        self.stock.set("A", 0)
        for value in (-1, False, 1.2, float("nan")):
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.stock.set("A", value)
        self.assertEqual(self.stock.stock["A"], 0)

    def test_exact_stock_can_be_allocated_then_exhausted(self):
        self.orders.create("O1", "A", 5)
        with self.assertRaises(ValueError):
            self.orders.create("O2", "A", 1)
        self.assertEqual(self.stock.stock["A"], 0)

    def test_refund_restores_stock_once(self):
        self.orders.create("O1", "A", 2)
        self.assertEqual(self.orders.refund("O1")["status"], "REFUNDED")
        self.orders.refund("O1")
        self.assertEqual((self.stock.stock["A"], len(self.bus.events)), (5, 2))

    def test_retry_after_refund_does_not_reopen_order(self):
        self.orders.create("O1", "A", 2)
        self.orders.refund("O1")
        self.assertEqual(self.orders.create("O1", "A", 2)["status"], "REFUNDED")
        self.assertEqual(self.stock.stock["A"], 5)

    def test_shipping_and_delivery_are_idempotent(self):
        self.orders.create("O1", "A", 2)
        self.orders.ship("O1")
        self.orders.ship("O1")
        self.orders.deliver("O1")
        self.orders.deliver("O1")
        self.assertEqual(self.orders.orders["O1"]["status"], "DELIVERED")
        self.assertEqual((self.stock.stock["A"], len(self.bus.events)), (3, 3))

    def test_invalid_transition_and_post_shipping_refund(self):
        self.orders.create("O1", "A", 2)
        with self.assertRaises(ValueError):
            self.orders.deliver("O1")
        self.orders.ship("O1")
        with self.assertRaises(ValueError):
            self.orders.refund("O1")
        self.assertEqual((self.stock.stock["A"], len(self.bus.events)), (3, 2))

    def test_refunded_order_cannot_ship_and_unknown_cannot_refund(self):
        self.orders.create("O1", "A", 2)
        self.orders.refund("O1")
        for action, oid in ((self.orders.ship, "O1"), (self.orders.refund, "missing")):
            with self.subTest(oid=oid), self.assertRaises(ValueError):
                action(oid)

    def test_local_create_rollback_after_publisher_failure(self):
        def fail(event):
            EventBus.publish(self.bus, event)
            raise RuntimeError("publisher simulato guasto")
        self.bus.publish = fail
        with self.assertRaises(RuntimeError):
            self.orders.create("O1", "A", 2)
        self.assertEqual((self.stock.stock, self.orders.orders, self.bus.events), ({"A": 5}, {}, []))

    def test_local_refund_rollback_after_publisher_failure(self):
        self.orders.create("O1", "A", 2)
        def fail(event):
            raise RuntimeError("publisher simulato guasto")
        self.bus.publish = fail
        with self.assertRaises(RuntimeError):
            self.orders.refund("O1")
        self.assertEqual((self.stock.stock["A"], self.orders.orders["O1"]["status"], len(self.bus.events)), (3, "CONFIRMED", 1))

    def test_returned_snapshots_do_not_mutate_internal_state(self):
        result = self.orders.create("O1", "A", 2)
        result["qty"] = 99
        self.orders.orders["O1"]["status"] = "REFUNDED"
        self.stock.stock["A"] = -1
        self.bus.events[0]["sku"] = "B"
        self.assertEqual(self.orders.orders["O1"]["qty"], 2)
        self.assertEqual((self.stock.stock["A"], self.bus.events[0]["sku"]), (3, "A"))

    def test_catalog_rejects_duplicates_and_invalid_metadata(self):
        catalog = Catalog()
        catalog.add("A", "SSD", "storage")
        with self.assertRaises(ValueError):
            catalog.add("A", "other", "input")
        with self.assertRaises(ValueError):
            catalog.add("B", " ", "storage")
        self.assertEqual(catalog.products["A"]["name"], "SSD")

    def test_recommendations_are_sorted_and_category_only(self):
        catalog = Catalog()
        for args in (("C", "C", "storage"), ("A", "A", "storage"), ("B", "B", "storage"), ("D", "D", "input")):
            catalog.add(*args)
        self.assertEqual(recommend_same_category(catalog, "A"), ["B", "C"])
        self.assertEqual(recommend_same_category(catalog, "D"), [])
        with self.assertRaises(ValueError):
            recommend_same_category(catalog, "missing")

    def test_demo_numbers(self):
        self.assertEqual(demo(), {"mode": "simulazione_monoprocesso", "stock_after_create": 3,
                                 "stock_after_refund": 5, "status": "REFUNDED", "events": 2,
                                 "recommendations": ["B"]})


if __name__ == "__main__":
    unittest.main()
