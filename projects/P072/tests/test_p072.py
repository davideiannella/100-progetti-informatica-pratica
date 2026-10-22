import pathlib
import random
import sys
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from mini_soc import Correlator, normalize, parse, process_lines


def event(ts, kind="login_failed", ip="203.0.113.9", **kwargs):
    return {"ts": ts, "event": kind, "src_ip": ip, "user": "alice", **kwargs}


class SOCTests(unittest.TestCase):
    def test_parse_quoted_values_and_equals(self):
        self.assertEqual(parse('ts=1 event=login_failed user="Alice B" note=a=b src_ip=203.0.113.9')["user"], "Alice B")
        self.assertEqual(parse("note=a=b")["note"], "a=b")

    def test_bad_parser_input(self):
        invalid = ("", " ", None, [], "event=a event=b", "junk", "x=", "=v", "Upper=x", "x='bad", "x=a\ny=b", "x=a\r", "x=\x00", "x=" + "a"*257, "x=" + "a"*8192)
        for line in invalid:
            with self.subTest(line=repr(line)[:60]):
                with self.assertRaises(ValueError): parse(line)
        with self.assertRaises(ValueError): parse(" ".join(f"k{i}=a" for i in range(33)))

    def test_normalize_validation(self):
        self.assertEqual(normalize(event("12"))["ts"], 12)
        self.assertEqual(normalize(event(12, ip="2001:0db8:0:0:0:0:0:1"))["src_ip"], "2001:db8::1")
        for value in (True, -1, 1.2, "1.2", "-1", "nan", "１２", 2**63, None):
            with self.subTest(ts=value):
                with self.assertRaises(ValueError): normalize(event(value))
        for key in ("ts", "event", "src_ip", "user"):
            bad = event(1); del bad[key]
            with self.subTest(missing=key):
                with self.assertRaises(ValueError): normalize(bad)
        for extra in ({"src_ip": "not-ip"}, {"event": "ignored"}, {"country": "it"}, {"country": "USA"}, {"user": "a\nb"}):
            with self.subTest(extra=extra):
                with self.assertRaises(ValueError): normalize({**event(1), **extra})

    def test_inclusive_boundary_expiry_and_source_isolation(self):
        c = Correlator(3, 10)
        self.assertEqual(c.ingest(event(0)), [])
        self.assertEqual(c.ingest(event(5)), [])
        self.assertEqual(c.ingest(event(5, ip="203.0.113.8")), [])
        a = c.ingest(event(10))
        self.assertEqual(a[0]["count"], 3)
        self.assertEqual(c.ingest(event(21)), [])
        self.assertEqual(set(c.failed), {"203.0.113.9"})

    def test_admin_allowed_unusual_and_missing_are_distinct(self):
        c = Correlator()
        for country in ("IT", "SM", "VA"):
            self.assertEqual(c.ingest(event(1, "admin_login", country=country)), [])
        self.assertEqual(c.ingest(event(2, "admin_login", country="US"))[0]["rule"], "admin_login_unusual_country")
        self.assertEqual(c.ingest(event(3, "admin_login"))[0]["rule"], "missing_country")
        custom = Correlator(allowed_countries=["US"])
        self.assertEqual(custom.ingest(event(1, "admin_login", country="US")), [])

    def test_bad_event_not_counted_and_order_rejected(self):
        c = Correlator(2, 10); c.ingest(event(5))
        for bad in (event(4), event(6, country="bad"), {"ts": 6, "event": "login_failed"}):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError): c.ingest(bad)
        self.assertEqual(list(c.failed["203.0.113.9"]), [5]); self.assertEqual(c.last_ts, 5)
        self.assertEqual(c.ingest(event(6))[0]["count"], 2)

    def test_capacity_is_explicit_and_expiry_recovers(self):
        c = Correlator(2, 10, max_sources=1, max_events_per_source=2)
        c.ingest(event(0)); c.ingest(event(1))
        with self.assertRaises(OverflowError): c.ingest(event(2))
        with self.assertRaises(OverflowError): c.ingest(event(2, ip="203.0.113.8"))
        self.assertEqual(c.ingest(event(12, ip="203.0.113.8")), [])
        self.assertEqual(set(c.failed), {"203.0.113.8"})

    def test_no_alert_for_success_and_no_automatic_reset(self):
        c = Correlator(2, 10); c.ingest(event(0))
        self.assertEqual(c.ingest(event(1, "login_success")), [])
        self.assertEqual(c.ingest(event(2))[0]["count"], 2)

    def test_duplicate_timestamps_count_as_separate_records(self):
        c = Correlator(2, 10)
        self.assertEqual(c.ingest(event(0)), [])
        self.assertEqual(c.ingest(event(0))[0]["count"], 2)

    def test_stream_keeps_rejection_evidence_and_continues(self):
        lines = ["event=a event=b secret=do-not-repeat", "ts=1 event=login_failed src_ip=203.0.113.9 user=alice",
                 "ts=2 event=login_failed src_ip=203.0.113.9 user=alice"]
        results = list(process_lines(lines, Correlator(1, 10, max_events_per_source=1)))
        self.assertEqual(results[0]["alerts"][0]["rule"], "invalid_event")
        self.assertNotIn("do-not-repeat", str(results))
        self.assertEqual(results[1]["alerts"][0]["rule"], "repeated_login_failures")
        self.assertEqual(results[2]["alerts"][0]["rule"], "capacity_exceeded")

    def test_invalid_settings(self):
        for name in ("threshold", "window", "max_sources", "max_events_per_source"):
            for value in (0, -1, True, 1.0, "3", None):
                with self.subTest(name=name, value=value):
                    with self.assertRaises(ValueError): Correlator(**{name: value})
        for countries in ([], ["it"], [None], "IT", None):
            with self.subTest(countries=countries):
                with self.assertRaises(ValueError): Correlator(allowed_countries=countries)
        with self.assertRaises(ValueError): Correlator(5, 10, max_events_per_source=4)


def make_seeded_case(seed):
    def test(self):
        rng = random.Random(7200 + seed); window = rng.randint(1, 45); threshold = rng.randint(1, 7)
        c = Correlator(threshold, window); history = []; ts = 0
        for _ in range(160):
            ts += rng.randint(0, 8); ip = f"203.0.113.{rng.randint(1, 5)}"
            kind = rng.choice(("login_failed", "login_failed", "admin_login", "login_success"))
            country = rng.choice(("IT", "SM", "VA", "US", None))
            kwargs = {"country": country} if country is not None else {}
            current = event(ts, kind, ip, **kwargs)
            result = c.ingest(current)
            if kind == "login_failed":
                history.append((ip, ts))
                expected = sum(source == ip and ts-window <= when <= ts for source, when in history)
                self.assertEqual(bool(result), expected >= threshold)
                if result: self.assertEqual(result[0]["count"], expected)
            elif kind == "admin_login":
                expected = "missing_country" if country is None else "admin_login_unusual_country" if country == "US" else None
                self.assertEqual([a["rule"] for a in result], [] if expected is None else [expected])
            else:
                self.assertEqual(result, [])
            self.assertTrue(all(ts-window <= when <= ts for q in c.failed.values() for when in q))
    return test
for seed in range(100): setattr(SOCTests, f"test_seeded_correlation_oracle_{seed:03}", make_seeded_case(seed))

if __name__ == "__main__": unittest.main(verbosity=2)
