from dataclasses import FrozenInstanceError
import pathlib
import sys
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).parents[1] / "src"))
from telemonitoring import Monitor, VitalReading, demo

RANGES = {"metric_a": (10, 20), "metric_b": (100, 200)}
USERS = {"service": "ingestor", "reader": "viewer", "reviewer": "reviewer"}


def reading(**changes):
    fields = dict(patient_code="SYN-001", metric="metric_a", value=15,
                  ts=1, event_id="e1", unit="demo_unit")
    return VitalReading(**(fields | changes))


class MonitorTests(unittest.TestCase):
    def setUp(self):
        self.monitor = Monitor(RANGES, USERS)

    def test_inside_range_is_ok_without_pending_review(self):
        event = self.monitor.ingest(reading(), "service")
        self.assertEqual(event["status"], "OK")
        self.assertFalse(event["requires_human_review"])
        self.assertEqual(event["review_state"], "NOT_REQUIRED")

    def test_artificial_bounds_are_inclusive(self):
        for value in (10, 20):
            with self.subTest(value=value):
                event = self.monitor.ingest(reading(value=value, event_id=str(value)), "service")
                self.assertEqual(event["status"], "OK")

    def test_below_or_above_range_opens_review(self):
        for value in (9.99, 20.01):
            with self.subTest(value=value):
                event = self.monitor.ingest(reading(value=value, event_id=str(value)), "service")
                self.assertEqual((event["status"], event["review_state"], event["requires_human_review"]),
                                 ("REVIEW", "PENDING", True))

    def test_numeric_values_reject_nan_infinity_bool_and_text(self):
        for value in (float("nan"), float("inf"), float("-inf"), True, "15", None, 10**1000):
            with self.subTest(value_type=type(value).__name__):
                with self.assertRaises(ValueError):
                    reading(value=value)
        self.assertEqual(self.monitor.view_events("reader"), [])

    def test_large_integer_boundaries_cannot_silently_lose_precision(self):
        for value in (2**53 + 1, -(2**53 + 1)):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    reading(value=value)
                with self.assertRaises(ValueError):
                    Monitor({"metric_a": (value, value)}, USERS)
        for value in (2**53, 2**53 + 2):
            with self.subTest(exact_integer=value):
                monitor = Monitor({"metric_a": (value, value)}, USERS)
                event = monitor.ingest(reading(value=value), "service")
                self.assertEqual(event["status"], "OK")
                self.assertEqual(event["value"], value)

    def test_readings_and_bounds_share_float_normalization(self):
        item = reading(value=15)
        self.assertIs(type(item.value), float)
        monitor = Monitor({"metric_a": (15, 15)}, USERS)
        self.assertEqual(monitor.ingest(item, "service")["status"], "OK")

    def test_synthetic_patient_code_required(self):
        for value in ("P001", "SYN-", "", None, "x" * 81):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    reading(patient_code=value)

    def test_timestamps_are_nonnegative_integer_simulated_seconds(self):
        self.assertEqual(reading(ts=0).ts, 0)
        for value in (-1, True, 1.0, "1", float("nan")):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    reading(ts=value)

    def test_metric_event_id_and_unit_are_validated(self):
        for changes in ({"metric": " "}, {"event_id": ""}, {"event_id": "e" * 81},
                        {"unit": "bpm"}, {"unit": None}):
            with self.subTest(changes=changes):
                with self.assertRaises(ValueError):
                    reading(**changes)

    def test_reading_is_immutable(self):
        item = reading()
        with self.assertRaises(FrozenInstanceError):
            item.value = float("nan")

    def test_unknown_metric_and_wrong_object_do_not_enter_history(self):
        for item in (reading(metric="unknown"), {}, None):
            with self.subTest(item=item):
                with self.assertRaises(ValueError):
                    self.monitor.ingest(item, "service")
        self.assertEqual(self.monitor.view_events("reader"), [])

    def test_range_configuration_rejects_invalid_shape_or_values(self):
        for ranges in ({}, [], {"m": (20, 10)}, {"m": [10]}, {"m": "10"},
                       {"m": (True, 20)}, {"m": (10, float("nan"))},
                       {"m": (10, float("inf"))}, {" ": (1, 2)}):
            with self.subTest(ranges=ranges):
                with self.assertRaises(ValueError):
                    Monitor(ranges, USERS)

    def test_degenerate_range_accepts_only_its_single_bound(self):
        monitor = Monitor({"metric_a": (15, 15)}, USERS)
        self.assertEqual(monitor.ingest(reading(), "service")["status"], "OK")
        self.assertEqual(monitor.ingest(reading(value=14, event_id="other"), "service")["status"], "REVIEW")

    def test_configuration_is_copied(self):
        ranges = {"metric_a": [10, 20]}
        users = dict(USERS)
        monitor = Monitor(ranges, users)
        ranges["metric_a"][0] = 100
        users["reader"] = "reviewer"
        self.assertEqual(monitor.ingest(reading(), "service")["status"], "OK")
        with self.assertRaises(PermissionError):
            monitor.close_review("e1", "reader", "demo")

    def test_roles_must_be_explicit_and_known(self):
        for users in ({}, [], {"actor": "admin"}, {"actor": True}, {" ": "viewer"}):
            with self.subTest(users=users):
                with self.assertRaises(ValueError):
                    Monitor(RANGES, users)

    def test_duplicate_reading_is_idempotent(self):
        first = self.monitor.ingest(reading(), "service")
        second = self.monitor.ingest(reading(), "service")
        self.assertEqual(first, second)
        self.assertEqual(len(self.monitor.audit), 1)
        self.assertEqual(len(self.monitor.view_events("reader")), 1)

    def test_conflicting_duplicate_cannot_replace_reading(self):
        self.monitor.ingest(reading(), "service")
        with self.assertRaises(ValueError):
            self.monitor.ingest(reading(value=25), "service")
        self.assertEqual(self.monitor.view_events("reader")[0]["value"], 15)

    def test_viewer_cannot_ingest_or_close_and_denials_are_audited(self):
        with self.assertRaises(PermissionError):
            self.monitor.ingest(reading(), "reader")
        with self.assertRaises(PermissionError):
            self.monitor.close_review("e1", "reader", "demo")
        self.assertEqual([item["result"] for item in self.monitor.audit], ["denied", "denied"])

    def test_ingestor_and_unknown_identity_cannot_view(self):
        for actor in ("service", "unknown"):
            with self.subTest(actor=actor):
                with self.assertRaises(PermissionError):
                    self.monitor.view_events(actor)

    def test_reviewer_closes_request_and_preserves_rule_classification(self):
        self.monitor.ingest(reading(value=25), "service")
        event = self.monitor.close_review("e1", "reviewer", "Verifica tecnica demo.")
        self.assertEqual(event["status"], "REVIEW")
        self.assertEqual(event["review_state"], "CLOSED")
        self.assertFalse(event["requires_human_review"])
        self.assertEqual(event["reviewed_by"], "reviewer")

    def test_identical_close_is_idempotent(self):
        self.monitor.ingest(reading(value=25), "service")
        first = self.monitor.close_review("e1", "reviewer", "demo")
        before = self.monitor.audit
        self.assertEqual(self.monitor.close_review("e1", "reviewer", "demo"), first)
        self.assertEqual(self.monitor.audit, before)

    def test_changed_close_cannot_overwrite_existing_note(self):
        self.monitor.ingest(reading(value=25), "service")
        self.monitor.close_review("e1", "reviewer", "originale")
        with self.assertRaises(ValueError):
            self.monitor.close_review("e1", "reviewer", "sostituzione")
        self.assertEqual(self.monitor.view_events("reader")[0]["review_note"], "originale")

    def test_retry_ingest_after_close_does_not_reopen_request(self):
        item = reading(value=25)
        self.monitor.ingest(item, "service")
        self.monitor.close_review("e1", "reviewer", "demo")
        self.assertEqual(self.monitor.ingest(item, "service")["review_state"], "CLOSED")

    def test_close_unknown_ok_or_invalid_note_fails(self):
        self.monitor.ingest(reading(), "service")
        for event_id, note in (("missing", "demo"), ("e1", "demo"), ("e1", ""), ("e1", "x" * 201)):
            with self.subTest(event_id=event_id, note_length=len(note)):
                with self.assertRaises(ValueError):
                    self.monitor.close_review(event_id, "reviewer", note)

    def test_returned_event_view_and_audit_do_not_mutate_storage(self):
        returned = self.monitor.ingest(reading(), "service")
        returned["value"] = -1
        snapshot = self.monitor.view_events("reader")
        snapshot[0]["value"] = -2
        audit = self.monitor.audit
        audit.clear()
        self.assertEqual(self.monitor.view_events("reader")[0]["value"], 15)
        self.assertGreaterEqual(len(self.monitor.audit), 3)

    def test_demo_has_three_synthetic_readings_and_one_closed_request(self):
        result = demo()
        self.assertTrue(result["synthetic_only"])
        self.assertFalse(result["clinical_validation"])
        self.assertEqual([e["status"] for e in result["before_review"]], ["OK", "REVIEW", "OK"])
        self.assertEqual([e["review_state"] for e in result["after_review"]],
                         ["NOT_REQUIRED", "CLOSED", "NOT_REQUIRED"])


if __name__ == "__main__":
    unittest.main()
