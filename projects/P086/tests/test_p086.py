import dataclasses
import math
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from air_monitor import Reading, validate, alerts, AirMonitor, demo


def reading(**changes):
    return dataclasses.replace(Reading("aria-A", 0, 12, 650, 21, 45), **changes)


class AirMonitorTests(unittest.TestCase):
    def test_valid_reading(self):
        self.assertTrue(validate(reading()))

    def test_range_endpoints(self):
        for name, values in {"pm25": (0, 1000), "co2": (250, 10000),
                             "temperature": (-50, 80), "humidity": (0, 100)}.items():
            for value in values:
                with self.subTest(name=name, value=value):
                    self.assertTrue(validate(reading(**{name: value})))

    def test_out_of_range(self):
        for name, values in {"pm25": (-1, 1001), "co2": (249, 10001),
                             "temperature": (-51, 81), "humidity": (-1, 101),
                             "timestamp_s": (-1,)}.items():
            for value in values:
                with self.subTest(name=name, value=value), self.assertRaises(ValueError):
                    validate(reading(**{name: value}))

    def test_nonfinite_and_wrong_numeric_types(self):
        for name in ("timestamp_s", "pm25", "co2", "temperature", "humidity"):
            for value in (float("nan"), float("inf"), -float("inf"), True, "22", None, 10**1000):
                with self.subTest(name=name, value=type(value).__name__), self.assertRaises(ValueError):
                    validate(reading(**{name: value}))

    def test_device_and_schema(self):
        for value in ("", " ", " aria-A", "x" * 65, None, True):
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate(reading(device=value))
        with self.assertRaises(ValueError):
            validate({"pm25": 12})

    def test_units_are_explicit(self):
        for units in (("mg/m3", "ppm", "degC", "%"), ("ug/m3",), list(reading().units)):
            with self.subTest(units=units), self.assertRaises(ValueError):
                validate(reading(units=units))

    def test_alert_equality_is_not_exceedance(self):
        self.assertEqual(alerts(reading(pm25=35, co2=1000)), [])

    def test_alerts_are_independent(self):
        self.assertEqual(alerts(reading(pm25=42, co2=1200)), ["pm25", "co2"])
        self.assertEqual(alerts(reading(pm25=42)), ["pm25"])
        self.assertEqual(alerts(reading(co2=1200)), ["co2"])

    def test_configurable_thresholds(self):
        monitor = AirMonitor(pm25_limit=12, co2_limit=650)
        self.assertEqual(monitor.ingest(reading()), [])
        self.assertEqual(monitor.ingest(reading(timestamp_s=1, pm25=13, co2=651)), ["pm25", "co2"])

    def test_invalid_thresholds(self):
        for kwargs in ({"pm25_limit": True}, {"pm25_limit": float("nan")},
                       {"pm25_limit": -1}, {"co2_limit": 249}, {"co2_limit": float("inf")}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                AirMonitor(**kwargs)

    def test_empty_summary(self):
        summary = AirMonitor().summary()
        self.assertEqual(summary["samples"], 0)
        self.assertIsNone(summary["pm25"]["mean"])
        self.assertIsNone(summary["humidity"]["max"])

    def test_summary_real_values(self):
        summary = demo()["summary"]
        self.assertEqual(summary["samples"], 3)
        self.assertEqual(summary["alerts"], 2)
        self.assertAlmostEqual(summary["pm25"]["mean"], 89 / 3)
        self.assertEqual(summary["co2"]["mean"], 950)
        self.assertEqual(summary["temperature"]["max"], 23)
        self.assertAlmostEqual(summary["humidity"]["mean"], 142 / 3)

    def test_order_is_per_device(self):
        monitor = AirMonitor()
        monitor.ingest(reading(timestamp_s=60))
        monitor.ingest(reading(device="aria-B", timestamp_s=0))
        self.assertEqual(len(monitor.history), 2)

    def test_duplicate_timestamp_rejected(self):
        monitor = AirMonitor()
        monitor.ingest(reading())
        with self.assertRaises(ValueError):
            monitor.ingest(reading(pm25=50))
        self.assertEqual(monitor.summary()["samples"], 1)
        self.assertEqual(monitor.alert_events, ())

    def test_late_event_does_not_change_state(self):
        monitor = AirMonitor()
        monitor.ingest(reading(timestamp_s=10))
        before = monitor.summary()
        with self.assertRaises(ValueError):
            monitor.ingest(reading(timestamp_s=9, pm25=50))
        self.assertEqual(monitor.summary(), before)
        monitor.ingest(reading(timestamp_s=11))

    def test_invalid_reading_is_atomic(self):
        monitor = AirMonitor()
        with self.assertRaises(ValueError):
            monitor.ingest(reading(pm25=42, humidity=101))
        self.assertEqual(monitor.history, ())
        self.assertEqual(monitor.alert_events, ())
        monitor.ingest(reading())

    def test_history_and_readings_cannot_be_edited(self):
        monitor = AirMonitor()
        monitor.ingest(reading())
        self.assertIsInstance(monitor.history, tuple)
        with self.assertRaises(dataclasses.FrozenInstanceError):
            monitor.history[0].pm25 = 999
        summary = monitor.summary()
        summary["pm25"]["mean"] = 999
        self.assertEqual(monitor.summary()["pm25"]["mean"], 12)

    def test_alert_event_has_origin_and_time(self):
        monitor = AirMonitor()
        monitor.ingest(reading(timestamp_s=20, pm25=50))
        self.assertEqual(monitor.alert_events, (("aria-A", 20, "pm25"),))


if __name__ == "__main__":
    unittest.main()
