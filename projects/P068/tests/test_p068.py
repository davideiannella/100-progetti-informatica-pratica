import itertools
import pathlib
import random
import sys
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from network_defense import FailedLoginDetector, RULES, firewall


class NetworkDefenseTests(unittest.TestCase):
    def test_full_policy_matrix(self):
        allowed = {("internet", "dmz", "https"), ("dmz", "app", "https"), ("app", "db", "postgres")}
        for triple in itertools.product(("internet", "dmz", "app", "db", "guest", "management"), repeat=2):
            for service in ("https", "postgres", "ssh", "unknown"):
                with self.subTest(triple=triple, service=service):
                    self.assertEqual(firewall(*triple, service), (*triple, service) in allowed)

    def test_malformed_policy_input_denied(self):
        for args in (([], "db", "ssh"), (None, "db", "ssh"), ("internet", "dmz", "HTTPS"), ("", "dmz", "https")):
            with self.subTest(args=args): self.assertFalse(firewall(*args))
        with self.assertRaises(TypeError): RULES[("a", "b", "c")] = True

    def test_inclusive_boundary_and_expiry(self):
        d = FailedLoginDetector(3, 10)
        self.assertFalse(d.record("203.0.113.1", 0))
        self.assertFalse(d.record("203.0.113.1", 5))
        self.assertTrue(d.record("203.0.113.1", 10))
        self.assertFalse(d.record("203.0.113.1", 20.001))

    def test_distinct_sources_and_ipv6_canonicalization(self):
        d = FailedLoginDetector(2, 10)
        self.assertFalse(d.record("2001:db8::1", 0))
        self.assertFalse(d.record("203.0.113.1", 1))
        self.assertTrue(d.record("2001:0db8:0:0:0:0:0:1", 2))

    def test_invalid_settings(self):
        for value in (0, -1, 1.2, True, "3", None):
            with self.subTest(value=value):
                with self.assertRaises(ValueError): FailedLoginDetector(threshold=value)
                with self.assertRaises(ValueError): FailedLoginDetector(max_sources=value)
        for value in (0, -1, float("nan"), float("inf"), 10**1000, True, "3", None):
            with self.subTest(window=value):
                with self.assertRaises(ValueError): FailedLoginDetector(window=value)

    def test_bad_event_does_not_append(self):
        d = FailedLoginDetector(2, 10); d.record("203.0.113.1", 20)
        for ip, ts in (("203.0.113.1", 19), ("bad", 21), ("203.0.113.1", float("nan")), ("203.0.113.1", True)):
            with self.subTest(ip=ip, ts=ts):
                with self.assertRaises(ValueError): d.record(ip, ts)
        self.assertEqual(d.last_ts, 20)
        self.assertEqual(list(d.events["203.0.113.1"]), [20])

    def test_memory_bounded_and_inactive_sources_removed(self):
        d = FailedLoginDetector(3, 10, max_sources=2)
        for _ in range(1000): d.record("203.0.113.1", 0)
        self.assertEqual(len(d.events["203.0.113.1"]), 3)
        d.record("203.0.113.2", 1)
        with self.assertRaises(OverflowError): d.record("203.0.113.3", 2)
        self.assertFalse(d.record("203.0.113.3", 12))
        self.assertEqual(set(d.events), {"203.0.113.3"})


def make_seeded_case(seed):
    def test(self):
        rng = random.Random(seed); threshold = rng.randint(1, 9); window = rng.randint(1, 40)
        detector = FailedLoginDetector(threshold, window); history = []; ts = 0
        for _ in range(150):
            ts += rng.randint(0, 9); ip = f"203.0.113.{rng.randint(1, 6)}"
            history.append((ip, ts))
            expected = sum(source == ip and ts - window <= when <= ts for source, when in history) >= threshold
            self.assertEqual(detector.record(ip, ts), expected)
            self.assertLessEqual(sum(map(len, detector.events.values())), 6 * threshold)
    return test
for seed in range(100):
    setattr(NetworkDefenseTests, f"test_seeded_window_oracle_{seed:03}", make_seeded_case(seed))

if __name__ == "__main__": unittest.main(verbosity=2)
