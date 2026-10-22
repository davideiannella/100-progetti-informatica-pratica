import json
import math
import random
import unittest
from observability import Metrics, alerts, request_event


class ObservabilityTests(unittest.TestCase):
    def test_original_healthy_case(self):
        m = Metrics()
        for value in (100, 120, 80, 150):
            m.record(value)
        self.assertEqual((m.availability, m.avg_latency), (1.0, 112.5))
        self.assertEqual(alerts(m), [])

    def test_original_degraded_case(self):
        m = Metrics()
        for i in range(100):
            m.record(100 if i < 98 else 500, i < 98)
        self.assertEqual(alerts(m), ["availability"])

    def test_empty_window_is_unknown(self):
        m = Metrics()
        self.assertIsNone(m.availability)
        self.assertIsNone(m.avg_latency)
        self.assertEqual(alerts(m), ["no_data"])

    def test_invalid_records_are_atomic(self):
        m = Metrics()
        m.record(12)
        before = vars(m).copy()
        for value in (-1, float("nan"), float("inf"), float("-inf"), True, "12", None, 10**1000):
            with self.subTest(value=repr(value)[:30]):
                with self.assertRaises(ValueError):
                    m.record(value)
                self.assertEqual(vars(m), before)
        with self.assertRaises(ValueError):
            m.record(12, "false")
        self.assertEqual(vars(m), before)

    def test_sum_overflow_does_not_count_request(self):
        m = Metrics()
        m.record(1e308)
        with self.assertRaises(ValueError):
            m.record(1e308)
        self.assertEqual(m.requests, 1)
        self.assertTrue(math.isfinite(m.avg_latency))

    def test_threshold_equality_and_both_alerts(self):
        m = Metrics()
        for i in range(100):
            m.record(250, i != 99)
        self.assertEqual(alerts(m), [])
        m.record(1000, False)
        self.assertEqual(alerts(m), ["availability", "latency"])

    def test_invalid_thresholds(self):
        for value in (-1, 1.1, float("nan"), float("inf"), True, "0.99"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                alerts(Metrics(), availability_slo=value)
        for value in (-1, float("nan"), float("inf"), True):
            with self.subTest(latency=value), self.assertRaises(ValueError):
                alerts(Metrics(), latency_slo_ms=value)

    def test_structured_log_is_one_json_line(self):
        event = request_event("t\nforged", "catalogo", 23, False)
        self.assertNotIn("\n", event)
        self.assertEqual(json.loads(event), {"trace_id": "t\nforged", "component": "catalogo", "latency_ms": 23.0, "ok": False})
        with self.assertRaises(ValueError):
            request_event("x" * 65, "api", 1)

    def test_100_seeded_windows_against_reference(self):
        rng = random.Random(61061)
        for case in range(100):
            with self.subTest(case=case):
                rows = [(rng.randint(0, 10000) / 10, rng.random() > 0.2) for _ in range(rng.randint(1, 100))]
                m = Metrics()
                for latency, ok in rows:
                    m.record(latency, ok)
                self.assertEqual(m.errors, sum(not ok for _, ok in rows))
                self.assertAlmostEqual(m.avg_latency, math.fsum(x for x, _ in rows) / len(rows))
                self.assertEqual(m.availability, sum(ok for _, ok in rows) / len(rows))
                rng.shuffle(rows)
                shuffled = Metrics()
                for latency, ok in rows:
                    shuffled.record(latency, ok)
                self.assertAlmostEqual(m.avg_latency, shuffled.avg_latency)
                self.assertEqual(m.availability, shuffled.availability)
