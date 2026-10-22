import sys
import math
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from logistics import Warehouse, shortest, moving_average, Shipment, eta_minutes, demo


class LogisticsTests(unittest.TestCase):
    def setUp(self):
        self.graph = {"WH": [("HUB", 5), ("DEST", 15)], "HUB": [("DEST", 6)], "DEST": []}

    def test_route_improves_direct_cost(self):
        self.assertEqual(shortest(self.graph, "WH", "DEST"), (11, ["WH", "HUB", "DEST"]))

    def test_zero_weights_cycles_and_same_node(self):
        graph = {"A": [("B", 0)], "B": [("A", 0), ("C", 2)], "C": []}
        self.assertEqual(shortest(graph, "A", "C"), (2, ["A", "B", "C"]))
        self.assertEqual(shortest(graph, "B", "B"), (0, ["B"]))

    def test_disconnected_and_unknown_nodes(self):
        for start, target in (("DEST", "WH"), ("missing", "WH")):
            with self.subTest(start=start), self.assertRaises(ValueError):
                shortest(self.graph, start, target)

    def test_all_negative_or_nonfinite_weights_rejected_even_off_path(self):
        for weight in (-1, float("nan"), float("inf"), 10 ** 400, True, "5"):
            graph = {"A": [], "B": [("A", weight)]}
            with self.subTest(weight=weight), self.assertRaises(ValueError):
                shortest(graph, "A", "A")

    def test_graph_shape_and_missing_destination_rejected(self):
        for graph in ({}, {"A": [("B", 1)]}, {"A": [1]}, {"A": [("A",)]}, {"A": "A"}, {1: []}):
            with self.subTest(graph=graph), self.assertRaises(ValueError):
                shortest(graph, "A", "A")

    def test_routing_is_deterministic_across_input_order(self):
        first = {"A": [("C", 1), ("B", 1)], "B": [("D", 1)], "C": [("D", 1)], "D": []}
        second = {key: list(reversed(value)) for key, value in reversed(list(first.items()))}
        self.assertEqual(shortest(first, "A", "D"), shortest(second, "A", "D"))
        self.assertEqual(shortest(first, "A", "D"), (2, ["A", "B", "D"]))

    def test_parallel_edges_choose_cheaper(self):
        self.assertEqual(shortest({"A": [("B", 9), ("B", 2)], "B": []}, "A", "B"), (2, ["A", "B"]))

    def test_overflowing_route_is_rejected(self):
        with self.assertRaises(ValueError):
            shortest({"A": [("B", 1e308)], "B": [("C", 1e308)], "C": []}, "A", "C")

    def test_warehouse_allocation_and_insufficiency(self):
        warehouse = Warehouse()
        warehouse.set("A", 10)
        self.assertTrue(warehouse.allocate("A", 4))
        self.assertFalse(warehouse.allocate("A", 7))
        self.assertFalse(warehouse.allocate("missing", 1))
        self.assertEqual(warehouse.stock, {"A": 6})
        warehouse.stock["A"] = -1
        self.assertEqual(warehouse.stock["A"], 6)

    def test_warehouse_invalid_quantities_do_not_mutate(self):
        warehouse = Warehouse()
        warehouse.set("A", 10)
        for qty in (0, -1, True, 2.5, float("nan")):
            with self.subTest(qty=qty), self.assertRaises(ValueError):
                warehouse.allocate("A", qty)
        for qty in (-1, False, float("inf")):
            with self.subTest(set_qty=qty), self.assertRaises(ValueError):
                warehouse.set("A", qty)
        self.assertEqual(warehouse.stock["A"], 10)

    def test_moving_average_uses_last_k(self):
        self.assertEqual(moving_average([10, 12, 14, 16], 3), 14)
        self.assertEqual(moving_average([10, 12], 1), 12)
        self.assertEqual(moving_average([0, 0], 2), 0)
        self.assertEqual(moving_average([1e308, 1e308], 2), 1e308)

    def test_invalid_history_and_window(self):
        for history, k in (([], 3), ([1], 2), ([1, 2], 0), ([1, 2], True), ([1, 2], 1.5), ([float("nan"), 2], 1), ([-1, 2], 1), ([True, 2], 1)):
            with self.subTest(history=history, k=k), self.assertRaises(ValueError):
                moving_average(history, k)

    def test_mean_near_float_limit_stays_finite(self):
        maximum = sys.float_info.max
        for history, k, expected in (
                ([maximum] * 3, 3, maximum),
                ([maximum, 0, 0], 3, maximum / 3),
                ([0, maximum, maximum], 2, maximum),
                ([0, 0, 0], 3, 0.0)):
            with self.subTest(history=history, k=k):
                result = moving_average(history, k)
                self.assertTrue(math.isfinite(result))
                self.assertLessEqual(result, max(history[-k:]))
                self.assertTrue(math.isclose(result, expected, rel_tol=1e-15))

    def test_eta_is_separate_arithmetic(self):
        self.assertEqual(eta_minutes(22, 44, 5), 35)
        self.assertEqual(eta_minutes(0, 44), 0)
        for args in ((-1, 44), (1, 0), (1, True), (1, float("nan")), (1, 4, -1)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                eta_minutes(*args)

    def test_shipment_transitions_and_idempotent_retry(self):
        shipment = Shipment("S1")
        self.assertTrue(shipment.update("PICKED", 1, "E1"))
        self.assertTrue(shipment.update("IN_TRANSIT", 2, "E2"))
        self.assertFalse(shipment.update("PICKED", 1, "E1"))
        self.assertTrue(shipment.update("DELIVERED", 3, "E3"))
        self.assertEqual([e["status"] for e in shipment.events], ["PICKED", "IN_TRANSIT", "DELIVERED"])

    def test_shipment_cannot_skip_or_repeat_state_with_new_id(self):
        shipment = Shipment("S1")
        with self.assertRaises(ValueError):
            shipment.update("IN_TRANSIT", 1, "E1")
        shipment.update("PICKED", 1, "E1")
        for status in ("PICKED", "DELIVERED", "UNKNOWN"):
            with self.subTest(status=status), self.assertRaises(ValueError):
                shipment.update(status, 2, "E2")
        self.assertEqual(len(shipment.events), 1)

    def test_tracking_conflict_and_nonincreasing_time_rejected(self):
        shipment = Shipment("S1")
        shipment.update("PICKED", 1, "E1")
        for status, ts, event_id in (("PICKED", 2, "E1"), ("IN_TRANSIT", 1, "E2"), ("IN_TRANSIT", 0, "E2")):
            with self.subTest(ts=ts), self.assertRaises(ValueError):
                shipment.update(status, ts, event_id)
        self.assertEqual(len(shipment.events), 1)

    def test_tracking_invalid_values_do_not_mutate(self):
        shipment = Shipment("S1")
        for ts in (True, -1, float("nan"), float("inf")):
            with self.subTest(ts=ts), self.assertRaises(ValueError):
                shipment.update("PICKED", ts, "E1")
        with self.assertRaises(ValueError):
            shipment.update("PICKED", 1, "")
        self.assertEqual(shipment.events, [])

    def test_tracking_snapshot_and_terminal_state(self):
        shipment = Shipment("S1")
        for status, ts, event_id in (("PICKED", 1, "E1"), ("IN_TRANSIT", 2, "E2"), ("DELIVERED", 3, "E3")):
            shipment.update(status, ts, event_id)
        shipment.events[0]["status"] = "UNKNOWN"
        with self.assertRaises(ValueError):
            shipment.update("IN_TRANSIT", 4, "E4")
        self.assertEqual(shipment.events[0]["status"], "PICKED")

    def test_demo_numbers(self):
        self.assertEqual(demo(), {"stock": 6, "route_minutes": 11, "path": ["WH", "HUB", "DEST"],
                                 "forecast_units": 14, "eta_separate_example_minutes": 35,
                                 "tracking_events": 2, "status": "IN_TRANSIT"})


if __name__ == "__main__":
    unittest.main()
