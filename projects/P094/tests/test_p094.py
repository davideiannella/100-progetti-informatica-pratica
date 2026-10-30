import json
import math
from fractions import Fraction
import pathlib
import sys
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).parents[1] / "src"))
from smart_city import SmartCity, demo


class CityTests(unittest.TestCase):
    def setUp(self):
        self.city = SmartCity(4)

    def test_empty_measurements_are_unknown_not_zero(self):
        result = self.city.indicators()
        self.assertEqual(result["parking_free"], 4)
        for field in ("traffic_avg", "pm25_avg", "traffic_alert", "air_alert"):
            self.assertIsNone(result[field])

    def test_capacity_contract(self):
        for value in (True, False, 0, -1, 1.5, "4", 100001):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    SmartCity(value)
        self.assertEqual(SmartCity(1).parking_free(), 1)

    def test_occupy_and_release_stall(self):
        self.city.set_parking(0, True, event_id="p1", ts=1)
        self.assertEqual(self.city.parking_free(), 3)
        self.city.set_parking(0, False, event_id="p2", ts=2)
        self.assertEqual(self.city.parking_free(), 4)

    def test_parking_identifier_and_bool_contract(self):
        for spot in (True, -1, 4, 0.0, "0"):
            with self.subTest(spot=spot):
                with self.assertRaises(ValueError):
                    self.city.set_parking(spot, True, event_id="p", ts=1)
        for occupied in (1, 0, "false", None, float("nan")):
            with self.subTest(occupied=occupied):
                with self.assertRaises(ValueError):
                    self.city.set_parking(0, occupied, event_id="p", ts=1)
        self.assertEqual(self.city.events, [])

    def test_duplicate_parking_event_is_idempotent(self):
        self.assertTrue(self.city.set_parking(0, True, event_id="p", ts=1))
        self.assertFalse(self.city.set_parking(0, True, event_id="p", ts=1))
        self.assertEqual(len(self.city.events), 1)
        self.assertEqual(self.city.parking_free(), 3)

    def test_stale_or_concurrent_parking_event_cannot_revert_state(self):
        self.city.set_parking(0, True, event_id="p2", ts=2)
        for ts in (1, 2):
            with self.subTest(ts=ts):
                with self.assertRaises(ValueError):
                    self.city.set_parking(0, False, event_id=f"old-{ts}", ts=ts)
        self.assertEqual(self.city.parking_free(), 3)
        self.assertEqual(len(self.city.events), 1)

    def test_conflicting_event_id_is_rejected_across_streams(self):
        self.city.traffic_event(70, event_id="same", ts=1)
        with self.assertRaises(ValueError):
            self.city.air_event(70, event_id="same", ts=1)
        with self.assertRaises(ValueError):
            self.city.traffic_event(71, event_id="same", ts=1)
        self.assertEqual(len(self.city.events), 1)

    def test_duplicate_traffic_and_air_do_not_bias_mean(self):
        for method in (self.city.traffic_event, self.city.air_event):
            ident = method.__name__
            self.assertTrue(method(20, event_id=ident, ts=1))
            self.assertFalse(method(20, event_id=ident, ts=1))
        result = self.city.indicators()
        self.assertEqual((result["traffic_samples"], result["air_samples"]), (1, 1))

    def test_three_samples_match_hand_calculation(self):
        for i, value in enumerate([70, 90, 100]):
            self.city.traffic_event(value, event_id=f"t{i}", ts=i)
        for i, value in enumerate([20, 40, 50]):
            self.city.air_event(value, event_id=f"a{i}", ts=i)
        result = self.city.indicators()
        self.assertAlmostEqual(result["traffic_avg"], 260 / 3)
        self.assertAlmostEqual(result["pm25_avg"], 110 / 3)
        self.assertTrue(result["traffic_alert"])
        self.assertTrue(result["air_alert"])

    def test_threshold_equality_does_not_trigger_alert(self):
        self.city.traffic_event(80, event_id="t", ts=0)
        self.city.air_event(35, event_id="a", ts=0)
        self.assertFalse(self.city.indicators()["traffic_alert"])
        self.assertFalse(self.city.indicators()["air_alert"])
        self.assertTrue(self.city.indicators(79, 34)["traffic_alert"])
        self.assertTrue(self.city.indicators(79, 34)["air_alert"])

    def test_zero_readings_are_valid(self):
        self.city.traffic_event(0, event_id="t", ts=0)
        self.city.air_event(0, event_id="a", ts=0)
        self.assertEqual(self.city.indicators()["traffic_avg"], 0)
        self.assertEqual(self.city.indicators()["pm25_avg"], 0)

    def test_numeric_validation_rejects_nonfinite_bool_negative_and_text(self):
        for method in (self.city.traffic_event, self.city.air_event):
            for value in (True, -1, float("nan"), float("inf"), "10", None, 10**1000):
                with self.subTest(method=method.__name__, value_type=type(value).__name__):
                    with self.assertRaises(ValueError):
                        method(value, event_id="bad", ts=1)
        self.assertEqual(self.city.events, [])

    def test_limits_are_validated_even_without_samples(self):
        for field in ("traffic_limit", "pm25_limit"):
            for value in (-1, True, float("nan"), float("inf"), "1"):
                with self.subTest(field=field, value=value):
                    with self.assertRaises(ValueError):
                        self.city.indicators(**{field: value})

    def test_event_metadata_contract(self):
        for field, value in (("event_id", ""), ("event_id", "x" * 81),
                             ("ts", True), ("ts", -1), ("ts", 1.0),
                             ("source", " "), ("zone", None)):
            args = dict(event_id="valid", ts=1, source="source", zone="zone") | {field: value}
            with self.subTest(field=field, value=value):
                with self.assertRaises(ValueError):
                    self.city.traffic_event(10, **args)
        self.assertEqual(self.city.events, [])

    def test_units_cannot_be_silently_mixed(self):
        for method, unit in ((self.city.air_event, "mg/m3"), (self.city.traffic_event, "vehicles/hour")):
            with self.subTest(unit=unit):
                with self.assertRaises(ValueError):
                    method(10, event_id="bad", ts=1, unit=unit)

    def test_records_keep_source_zone_timestamp_and_unit(self):
        self.city.air_event(10, event_id="e", ts=7, source="sensor-demo", zone="zone-A")
        self.assertEqual(self.city.events[0], {"event_id": "e", "ts": 7, "source": "sensor-demo",
                         "zone": "zone-A", "kind": "air", "value": 10.0, "unit": "ug/m3"})

    def test_event_snapshot_cannot_mutate_internal_history(self):
        self.city.air_event(10, event_id="e", ts=1)
        self.city.events[0]["value"] = -1
        self.assertEqual(self.city.events[0]["value"], 10)

    def test_public_snapshot_uses_aggregate_allowlist(self):
        self.city.air_event(10, event_id="private-event", ts=123, source="private-source", zone="private-zone")
        exported = self.city.public_snapshot()
        self.assertEqual(set(exported), {"synthetic", "indicators", "units"})
        text = json.dumps(exported)
        for value in ("private-event", "private-source", "private-zone", '"ts"', '"spot"'):
            self.assertNotIn(value, text)

    def test_large_finite_values_do_not_overflow_the_mean(self):
        self.city.air_event(1e308, event_id="a1", ts=1)
        self.city.air_event(1e308, event_id="a2", ts=2)
        self.assertEqual(self.city.indicators()["pm25_avg"], 1e308)
        maximum = sys.float_info.max
        cases = ([maximum] * 3, [maximum] * 7,
                 [maximum, math.nextafter(maximum, 0), maximum],
                 [maximum, maximum, 0], [0, 0, 0], [20, 40, 50],
                 [0.1] * 11, [5e-324] * 3, [1e-323] * 3)
        for values in cases:
            expected = float(sum(map(Fraction.from_float, map(float, values)), Fraction()) / len(values))
            city = SmartCity(1)
            for index, value in enumerate(values):
                city.air_event(value, event_id=f"a{index}", ts=index)
                city.traffic_event(value, event_id=f"t{index}", ts=index)
            for field in ("pm25_avg", "traffic_avg"):
                with self.subTest(values=values, field=field):
                    actual = city.indicators()[field]
                    self.assertTrue(math.isfinite(actual))
                    self.assertLessEqual(actual, max(values))
                    self.assertEqual(actual, expected)
            if len(set(values)) == 1:
                indicators = city.indicators(traffic_limit=values[0], pm25_limit=values[0])
                self.assertFalse(indicators["traffic_alert"])
                self.assertFalse(indicators["air_alert"])

    def test_demo_has_eight_records_and_two_free_stalls(self):
        result = demo()
        self.assertEqual(result["events_stored"], 8)
        self.assertFalse(result["duplicate_added"])
        self.assertEqual(result["public"]["indicators"]["parking_free"], 2)


if __name__ == "__main__":
    unittest.main()
