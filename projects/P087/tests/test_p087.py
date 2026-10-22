import dataclasses
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from smart_meter import Meter, Collector, Sample, validate, demo


class SmartMeterTests(unittest.TestCase):
    def test_seconds_to_hours(self):
        sample = Meter("m").sample("e1", 2, 1800)
        self.assertEqual(sample.delta_kwh, 1)
        self.assertEqual(sample.total_kwh, 1)

    def test_variable_intervals(self):
        meter = Meter("m")
        values = [meter.sample("a", 1, 1800), meter.sample("b", 2, 5400), meter.sample("c", 1.5, 7200)]
        self.assertEqual([s.delta_kwh for s in values], [0.5, 2, 0.75])
        self.assertEqual(meter.total_kwh, 3.25)

    def test_zero_power_is_valid(self):
        sample = Meter("m", initial_kwh=5).sample("e1", 0, 60)
        self.assertEqual(sample.delta_kwh, 0)
        self.assertEqual(sample.total_kwh, 5)

    def test_initial_time_and_register(self):
        meter, collector = Meter("m", 100, 10), Collector("m", 100, 10)
        collector.ingest(meter.sample("a", 2, 1900))
        self.assertEqual(collector.summary()["total_kwh"], 11)
        self.assertEqual(collector.summary()["period_kwh"], 1)
        self.assertEqual(collector.summary()["average_kw"], 2)

    def test_invalid_identifiers(self):
        for value in ("", " ", " x", None, True, "x" * 65):
            with self.subTest(value=value), self.assertRaises(ValueError):
                Meter(value)
            with self.subTest(event=value), self.assertRaises(ValueError):
                Meter("m").sample(value, 1, 60)

    def test_invalid_initial_values(self):
        for value in (-1, float("nan"), float("inf"), True, None, "0", 10**1000):
            for cls in (Meter, Collector):
                with self.subTest(cls=cls.__name__, value=type(value).__name__), self.assertRaises(ValueError):
                    cls("m", initial_kwh=value)
                with self.assertRaises(ValueError):
                    cls("m", start_s=value)

    def test_invalid_power_and_time(self):
        for value in (-1, float("nan"), float("inf"), True, None, "1", 10**1000):
            with self.subTest(value=type(value).__name__), self.assertRaises(ValueError):
                Meter("m").sample("a", value, 60)
            with self.assertRaises(ValueError):
                Meter("m").sample("a", 1, value)

    def test_nonincreasing_time_rejected(self):
        meter = Meter("m", start_s=10)
        for end in (0, 9, 10):
            with self.subTest(end=end), self.assertRaises(ValueError):
                meter.sample("a", 1, end)
        self.assertEqual(meter.total_kwh, 0)

    def test_meter_retry_is_idempotent(self):
        meter = Meter("m")
        first = meter.sample("a", 1, 3600)
        meter.sample("b", 2, 7200)
        self.assertIs(meter.sample("a", 1, 3600), first)
        self.assertEqual(meter.total_kwh, 3)

    def test_meter_id_conflict_is_atomic(self):
        meter = Meter("m")
        meter.sample("a", 1, 3600)
        with self.assertRaises(ValueError):
            meter.sample("a", 2, 7200)
        self.assertEqual(meter.total_kwh, 1)
        self.assertEqual(meter.sample("b", 1, 7200).start_s, 3600)

    def test_overflow_rejected(self):
        meter = Meter("m")
        with self.assertRaises(ValueError):
            meter.sample("a", 1e308, 1e308)
        self.assertEqual(meter.total_kwh, 0)
        self.assertEqual(meter.sample("a", 1, 3600).total_kwh, 1)

    def test_unrepresentable_increment_rejected(self):
        with self.assertRaises(ValueError):
            Meter("m", initial_kwh=1e300).sample("a", 1, 1)
        with self.assertRaises(ValueError):
            Meter("m").sample("a", 1e-300, 1e-300)

    def test_empty_collector_summary(self):
        summary = Collector("m").summary()
        self.assertEqual(summary["samples"], 0)
        self.assertIsNone(summary["average_kw"])
        self.assertIsNone(summary["max_kw"])

    def test_collector_duplicate_ignored(self):
        collector = Collector("m")
        sample = Meter("m").sample("a", 1, 3600)
        self.assertTrue(collector.ingest(sample))
        self.assertFalse(collector.ingest(sample))
        self.assertEqual(len(collector.history), 1)

    def test_collector_conflicting_id_rejected(self):
        collector = Collector("m")
        sample = Meter("m").sample("a", 1, 3600)
        collector.ingest(sample)
        changed = dataclasses.replace(sample, power_kw=2, delta_kwh=2, total_kwh=2)
        with self.assertRaises(ValueError):
            collector.ingest(changed)
        self.assertEqual(collector.summary()["total_kwh"], 1)

    def test_missing_interval_then_replay(self):
        collector, meter = Collector("m"), Meter("m")
        first, second = meter.sample("a", 1, 60), meter.sample("b", 1, 120)
        with self.assertRaises(ValueError):
            collector.ingest(second)
        self.assertEqual(collector.history, ())
        collector.ingest(first)
        collector.ingest(second)
        self.assertEqual(len(collector.history), 2)

    def test_overlap_and_reordered_event_rejected(self):
        collector = Collector("m")
        sample = Meter("m").sample("a", 1, 3600)
        collector.ingest(sample)
        with self.assertRaises(ValueError):
            collector.ingest(dataclasses.replace(sample, event_id="b"))
        self.assertEqual(collector.summary()["duration_s"], 3600)

    def test_wrong_device_rejected(self):
        with self.assertRaises(ValueError):
            Collector("m").ingest(Meter("other").sample("a", 1, 3600))

    def test_inconsistent_energy_and_total_rejected(self):
        sample = Meter("m").sample("a", 1, 3600)
        for changed in (dataclasses.replace(sample, delta_kwh=2), dataclasses.replace(sample, total_kwh=2),
                        dataclasses.replace(sample, total_kwh=0),
                        Sample("zero", "m", 0, 1, 0, 1e-15, 1e-15),
                        Sample("tiny", "m", 0, 1e-300, 1e-300, 0, 0)):
            collector = Collector("m")
            with self.subTest(changed=changed), self.assertRaises(ValueError):
                collector.ingest(changed)
            self.assertEqual(collector.history, ())

    def test_invalid_event_schema(self):
        sample = Meter("m").sample("a", 1, 3600)
        for changed in (None, {}, dataclasses.replace(sample, power_kw=True),
                        dataclasses.replace(sample, end_s=float("nan")), dataclasses.replace(sample, end_s=0)):
            with self.subTest(changed=changed), self.assertRaises(ValueError):
                validate(changed)

    def test_power_alert_threshold_is_strict(self):
        collector, meter = Collector("m", power_alert_kw=2), Meter("m")
        collector.ingest(meter.sample("a", 2, 3600))
        self.assertEqual(collector.summary()["power_alerts"], 0)
        collector.ingest(meter.sample("b", 2.1, 7200))
        self.assertEqual(collector.summary()["power_alerts"], 1)

    def test_invalid_alert_limit(self):
        for value in (-1, True, float("nan"), "2"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                Collector("m", power_alert_kw=value)

    def test_demo_and_weighted_average(self):
        result = demo()
        self.assertTrue(result["duplicate_ignored"])
        self.assertEqual(result["summary"], {"samples": 3, "total_kwh": 3.25, "period_kwh": 3.25,
                        "duration_s": 7200.0, "average_kw": 1.625, "max_kw": 2.0, "power_alerts": 1})


if __name__ == "__main__":
    unittest.main()
