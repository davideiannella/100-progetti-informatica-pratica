import sys
import tempfile
import unittest
import sqlite3
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from smart_waste_platform import DeviceRegistry, EventStore, SmartWastePlatform, EventSigner, new_classification_event, demo


class SmartWastePlatformTests(unittest.TestCase):
    def setUp(self):
        self.registry = DeviceRegistry()
        self.device = self.registry.register("BIN-001", "t" * 64)
        self.store = EventStore()
        self.addCleanup(self.store.close)
        self.platform = SmartWastePlatform(self.registry, self.store)

    def event(self, event_id="E1", **changes):
        payload = new_classification_event("BIN-001", event_id, "carta", 0.92, 35, "2026-10-21T10:00:00+00:00")
        payload.update(changes)
        return payload

    def send(self, payload, platform=None, secret=None):
        return (platform or self.platform).ingest(payload, EventSigner.sign(payload, secret or self.device.secret))

    def test_valid_event_and_class_counts(self):
        self.assertEqual(self.send(self.event()), {"accepted": True, "inserted": True})
        self.send(self.event("E2", waste_class="vetro"))
        self.assertEqual((self.store.count_events(), self.store.waste_counts()), (2, {"carta": 1, "vetro": 1}))

    def test_identical_retry_does_not_duplicate_event_or_alert(self):
        payload = self.event(fill_pct=80)
        self.assertTrue(self.send(payload)["inserted"])
        self.assertFalse(self.send(dict(reversed(list(payload.items()))))["inserted"])
        self.assertEqual((self.store.count_events(), len(self.store.alerts())), (1, 1))

    def test_duplicate_conflicting_content_rejected(self):
        self.send(self.event())
        with self.assertRaises(ValueError):
            self.send(self.event(fill_pct=85))
        self.assertEqual((self.store.count_events(), len(self.store.alerts())), (1, 0))

    def test_event_ids_are_scoped_to_device(self):
        second = self.registry.register("BIN-002", "s" * 64)
        self.send(self.event())
        self.send(self.event(device_id=second.device_id), secret=second.secret)
        self.assertEqual(self.store.count_events(), 2)

    def test_tampered_payload_and_wrong_secret_rejected(self):
        payload = self.event()
        mac = EventSigner.sign(payload, self.device.secret)
        payload["fill_pct"] = 90
        with self.assertRaises(PermissionError):
            self.platform.ingest(payload, mac)
        with self.assertRaises(PermissionError):
            self.send(self.event(), secret="x" * 64)
        self.assertEqual(self.store.count_events(), 0)

    def test_malformed_mac_rejected_without_comparison_crash(self):
        for mac in ("bad", "ø" * 64, None, b"0" * 64, "0" * 64, "A" * 64):
            with self.subTest(mac=mac), self.assertRaises(PermissionError):
                self.platform.ingest(self.event(), mac)
        self.assertEqual(self.store.count_events(), 0)

    def test_unknown_device_rejected(self):
        with self.assertRaises(PermissionError):
            self.platform.ingest(self.event(device_id="UNKNOWN"), "0" * 64)
        self.assertEqual(self.store.count_events(), 0)

    def test_registry_rejects_bad_ids_duplicates_and_short_secrets(self):
        for device_id in ("", "has space", "x" * 65, True, None, []):
            with self.subTest(device_id=device_id), self.assertRaises(ValueError):
                self.registry.register(device_id)
        with self.assertRaises(ValueError):
            self.registry.register("BIN-001")
        for secret in ("", "short", True, b"x" * 64):
            with self.subTest(secret=secret), self.assertRaises(ValueError):
                self.registry.register("NEW", secret)

    def test_random_secret_and_repr_do_not_expose_it(self):
        device = self.registry.register("NEW")
        self.assertEqual(len(device.secret), 64)
        self.assertNotIn(device.secret, repr(device))
        self.assertIs(self.registry.get("NEW"), device)

    def test_confidence_boundaries_and_boolean_rejection(self):
        for n, confidence in enumerate((0, 1)):
            self.send(self.event(f"B{n}", confidence=confidence))
        for confidence in (-0.1, 1.1, 10 ** 400, True, "0.8", None):
            with self.subTest(confidence=confidence), self.assertRaises(ValueError):
                self.send(self.event("INVALID", confidence=confidence))
        self.assertEqual(self.store.count_events(), 2)

    def test_nonfinite_numbers_rejected_before_any_write(self):
        for field in ("confidence", "fill_pct"):
            for value in (float("nan"), float("inf"), -float("inf")):
                payload = self.event(**{field: value})
                with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                    self.platform.ingest(payload, "0" * 64)
                with self.assertRaises(ValueError):
                    EventSigner.sign(payload, self.device.secret)
        self.assertEqual(self.store.count_events(), 0)

    def test_fill_boundaries_alert_is_greater_or_equal_80(self):
        for n, fill in enumerate((0, 79.99, 80, 100)):
            self.send(self.event(f"F{n}", fill_pct=fill))
        self.assertEqual(len(self.store.alerts()), 2)
        self.assertEqual([a["event_id"] for a in self.store.alerts()], ["F2", "F3"])
        for fill in (-1, 101, False, "80", None):
            with self.subTest(fill=fill), self.assertRaises(ValueError):
                self.send(self.event("INVALID", fill_pct=fill))
        self.assertEqual(self.store.count_events(), 4)

    def test_schema_exact_no_images_or_unknown_event_types(self):
        for payload in (None, {}, self.event(image="raw"), self.event(event_type="telemetry"), self.event(waste_class="uranio"), self.event(waste_class=[])):
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                self.platform.ingest(payload, "0" * 64)
        payload = self.event()
        del payload["confidence"]
        with self.assertRaises(ValueError):
            self.platform.ingest(payload, "0" * 64)

    def test_timestamp_must_be_parseable_and_timezone_aware(self):
        for timestamp in ("yesterday", "2026-10-21", "2026-10-21T10:00:00", None, True):
            with self.subTest(timestamp=timestamp), self.assertRaises(ValueError):
                self.send(self.event(created_at=timestamp))
        self.send(self.event(created_at="2026-10-21T10:00:00Z"))
        self.assertEqual(self.store.count_events(), 1)

    def test_invalid_event_ids_and_sql_injection_are_rejected(self):
        for event_id in ("", " ", None, True, "E'; DROP TABLE device_event;--"):
            with self.subTest(event_id=event_id), self.assertRaises(ValueError):
                payload = self.event()
                payload["event_id"] = event_id
                self.platform.ingest(payload, "0" * 64)
        self.send(self.event())
        self.assertEqual(self.store.count_events(), 1)

    def test_transaction_rolls_back_event_if_alert_creation_fails(self):
        with patch.object(self.store, "_create_alert", side_effect=RuntimeError("guasto alert")):
            with self.assertRaises(RuntimeError):
                self.send(self.event(fill_pct=85))
        self.assertEqual((self.store.count_events(), self.store.alerts()), (0, []))
        self.assertTrue(self.send(self.event(fill_pct=85))["inserted"])
        self.assertEqual((self.store.count_events(), len(self.store.alerts())), (1, 1))

    def test_sql_errors_are_not_silently_treated_as_duplicates(self):
        self.store.conn.execute("CREATE TRIGGER block_event BEFORE INSERT ON device_event BEGIN SELECT RAISE(ABORT, 'blocked'); END")
        with self.assertRaises(sqlite3.IntegrityError):
            self.send(self.event())
        self.assertEqual(self.store.count_events(), 0)
        self.store.conn.execute("DROP TRIGGER block_event")
        self.assertTrue(self.send(self.event())["inserted"])

    def test_file_database_survives_close_and_keeps_dedup(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = str(Path(tmp) / "events.sqlite3")
            first = EventStore(path)
            platform = SmartWastePlatform(self.registry, first)
            self.send(self.event(fill_pct=85), platform)
            first.close()
            second = EventStore(path)
            try:
                self.assertEqual((second.count_events(), len(second.alerts())), (1, 1))
                self.assertFalse(self.send(self.event(fill_pct=85), SmartWastePlatform(self.registry, second))["inserted"])
            finally:
                second.close()

    def test_memory_databases_do_not_persist(self):
        other = EventStore()
        try:
            self.send(self.event())
            self.assertEqual(other.count_events(), 0)
        finally:
            other.close()

    def test_canonical_json_has_stable_key_order_and_rejects_non_json(self):
        self.assertEqual(EventSigner.canonical_payload({"b": 2, "a": 1}), b'{"a":1,"b":2}')
        for payload in ([1], {1: "a"}, {"x": object()}):
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                EventSigner.canonical_payload(payload)

    def test_payload_mutation_after_ingestion_cannot_change_database(self):
        payload = self.event()
        self.send(payload)
        payload["waste_class"] = "vetro"
        self.assertEqual(self.store.waste_counts(), {"carta": 1})

    def test_helper_does_not_invent_model_results(self):
        payload = self.event()
        self.assertEqual((payload["waste_class"], payload["confidence"]), ("carta", 0.92))
        self.assertEqual(set(payload), {"device_id", "event_id", "event_type", "waste_class", "confidence", "fill_pct", "created_at"})

    def test_helper_rejects_explicit_empty_or_boolean_timestamp(self):
        for timestamp in ("", False):
            with self.subTest(timestamp=timestamp), self.assertRaises(ValueError):
                new_classification_event("BIN-001", "E1", "carta", 0.92, 35, timestamp)

    def test_demo_numbers(self):
        self.assertEqual(demo(), {"mode": "metadati_manuali_HMAC_SQLite", "first_inserted": True,
                                 "retry_inserted": False, "events": 2, "alerts": 1,
                                 "counts": {"carta": 1, "vetro": 1}, "storage": ":memory:"})


if __name__ == "__main__":
    unittest.main()
