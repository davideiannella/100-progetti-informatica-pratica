import dataclasses
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from smart_parking import Parking, ParkingEvent, demo


def event(**changes):
    return dataclasses.replace(ParkingEvent("a", "enter", 0, 1, "auto-A"), **changes)


class ParkingTests(unittest.TestCase):
    def test_initial_capacity(self):
        parking = Parking(3)
        self.assertEqual(parking.available(), 3)
        self.assertEqual(parking.snapshot(), {1: None, 2: None, 3: None})

    def test_invalid_capacity(self):
        for value in (0, -1, 1.5, True, float("nan"), "2", None, 10001):
            with self.subTest(value=value), self.assertRaises(ValueError):
                Parking(value)

    def test_enter_and_exit_duration(self):
        parking = Parking(2)
        self.assertEqual(parking.apply(event(timestamp_s=10)).status, "accepted")
        result = parking.apply(event(event_id="b", kind="exit", timestamp_s=70))
        self.assertEqual(result.dwell_s, 60)
        self.assertEqual(result.available, 2)

    def test_capacity_never_overflows(self):
        parking = Parking(1)
        parking.apply(event())
        result = parking.apply(event(event_id="b", vehicle_id="auto-B", timestamp_s=1))
        self.assertEqual((result.status, result.reason), ("rejected", "spot_occupied"))
        self.assertEqual(parking.available(), 0)

    def test_vehicle_cannot_occupy_two_spots(self):
        parking = Parking(2)
        parking.apply(event())
        result = parking.apply(event(event_id="b", spot=2, timestamp_s=1))
        self.assertEqual(result.reason, "vehicle_already_inside")
        self.assertEqual(parking.available(), 1)

    def test_exit_empty_spot(self):
        parking = Parking(1)
        result = parking.apply(event(kind="exit"))
        self.assertEqual(result.reason, "spot_empty")
        self.assertEqual(parking.available(), 1)

    def test_exit_wrong_vehicle(self):
        parking = Parking(1)
        parking.apply(event())
        result = parking.apply(event(event_id="b", kind="exit", vehicle_id="auto-B", timestamp_s=1))
        self.assertEqual(result.reason, "vehicle_mismatch")
        self.assertEqual(parking.snapshot()[1], "auto-A")

    def test_duplicate_enter_has_no_effect(self):
        parking = Parking(2)
        first = parking.apply(event())
        self.assertIs(parking.apply(event()), first)
        self.assertEqual(len(parking.audit), 1)
        self.assertEqual(parking.available(), 1)

    def test_duplicate_exit_after_new_arrival_is_safe(self):
        parking = Parking(1)
        parking.apply(event())
        leave = event(event_id="b", kind="exit", timestamp_s=1)
        result = parking.apply(leave)
        parking.apply(event(event_id="c", vehicle_id="auto-C", timestamp_s=2))
        self.assertIs(parking.apply(leave), result)
        self.assertEqual(parking.snapshot()[1], "auto-C")
        self.assertEqual(len(parking.audit), 3)

    def test_rejected_retry_keeps_original_result(self):
        parking = Parking(1)
        leave = event(kind="exit")
        rejected = parking.apply(leave)
        parking.apply(event(event_id="b", timestamp_s=1))
        self.assertIs(parking.apply(leave), rejected)
        self.assertEqual(parking.available(), 0)

    def test_conflicting_id_rejected_without_changes(self):
        parking = Parking(2)
        parking.apply(event())
        before = parking.snapshot()
        with self.assertRaises(ValueError):
            parking.apply(event(spot=2))
        self.assertEqual(parking.snapshot(), before)
        self.assertEqual(len(parking.audit), 1)

    def test_late_unique_event_rejected(self):
        parking = Parking(2)
        parking.apply(event(timestamp_s=10))
        result = parking.apply(event(event_id="b", spot=2, vehicle_id="auto-B", timestamp_s=9))
        self.assertEqual(result.reason, "out_of_order")
        self.assertEqual(parking.available(), 1)

    def test_equal_time_events_are_allowed(self):
        parking = Parking(2)
        parking.apply(event())
        result = parking.apply(event(event_id="b", spot=2, vehicle_id="auto-B"))
        self.assertEqual(result.status, "accepted")
        self.assertEqual(parking.available(), 0)

    def test_rejection_does_not_advance_time_watermark(self):
        parking = Parking(2)
        parking.apply(event(timestamp_s=10))
        parking.apply(event(event_id="b", timestamp_s=100))
        result = parking.apply(event(event_id="c", spot=2, vehicle_id="auto-C", timestamp_s=11))
        self.assertEqual(result.status, "accepted")

    def test_invalid_spot_types_and_bounds(self):
        for value in (0, 3, -1, True, 1.0, float("nan"), "1", None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                Parking(2).apply(event(spot=value))

    def test_invalid_times(self):
        for value in (-1, True, float("nan"), float("inf"), "0", None, 10**1000):
            with self.subTest(value=type(value).__name__), self.assertRaises(ValueError):
                Parking(2).apply(event(timestamp_s=value))

    def test_invalid_ids(self):
        for field in ("event_id", "vehicle_id"):
            for value in ("", " ", " a", None, True, "x" * 65):
                with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                    Parking(2).apply(event(**{field: value}))

    def test_invalid_kind_and_schema(self):
        for value in ("ENTER", "", None, True, [], 1):
            with self.subTest(value=value), self.assertRaises(ValueError):
                Parking(1).apply(event(kind=value))
        with self.assertRaises(ValueError):
            Parking(1).apply({"kind": "enter"})

    def test_invalid_input_is_atomic(self):
        parking = Parking(1)
        with self.assertRaises(ValueError):
            parking.apply(event(spot=2))
        self.assertEqual(parking.audit, ())
        self.assertEqual(parking.apply(event()).status, "accepted")

    def test_snapshot_and_audit_do_not_expose_mutable_state(self):
        parking = Parking(1)
        parking.apply(event())
        snapshot = parking.snapshot()
        snapshot[1] = None
        self.assertEqual(parking.available(), 0)
        self.assertIsInstance(parking.audit, tuple)
        with self.assertRaises(dataclasses.FrozenInstanceError):
            parking.audit[0][1].available = 999

    def test_no_negative_occupancy_after_repeated_exit(self):
        parking = Parking(1)
        for i in range(3):
            result = parking.apply(event(event_id=str(i), kind="exit", timestamp_s=i))
            self.assertEqual((result.occupied, result.available), (0, 1))
        self.assertEqual(len(parking.audit), 3)

    def test_demo_values_and_cached_old_snapshot(self):
        result = demo()
        self.assertEqual([r["status"] for r in result["results"]].count("accepted"), 4)
        self.assertEqual([r["status"] for r in result["results"]].count("rejected"), 3)
        self.assertEqual(result["results"][3]["dwell_s"], 70)
        self.assertTrue(result["duplicate_same_result"])
        self.assertEqual((result["audit_events"], result["available"]), (7, 0))


if __name__ == "__main__":
    unittest.main()
