import hashlib
import hmac
import json
import pathlib
import sys
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).parents[1] / "src"))
from fleet_update import ALGORITHM, MAX_VERSION, Device, demo, manifest, verify


class UpdateTests(unittest.TestCase):
    def setUp(self):
        self.key = b"test-only-shared-key-000000000000"  # Fixture pubblica, mai usare in prodotti.
        self.payload = b"firmware-v2"
        self.m = manifest(2, self.payload, self.key)
        self.device = Device("dev-1")

    def test_manifest_matches_independent_hmac_calculation(self):
        body = {"algorithm": "HMAC-SHA256", "sha256": hashlib.sha256(self.payload).hexdigest(), "version": 2}
        raw = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("ascii")
        self.assertEqual(self.m, body | {"mac": hmac.new(self.key, raw, hashlib.sha256).hexdigest()})

    def test_valid_update_stores_version_and_payload(self):
        self.assertTrue(self.device.apply(self.m, self.payload, self.key))
        self.assertEqual((self.device.version, self.device.payload), (2, self.payload))
        self.assertEqual(self.device.previous, (1, b"firmware-v1"))

    def test_payload_tampering_rejected_without_state_change(self):
        self.assertFalse(self.device.apply(self.m, b"tampered", self.key))
        self.assertEqual((self.device.version, self.device.payload, self.device.previous),
                         (1, b"firmware-v1", None))

    def test_manifest_field_tampering_rejected(self):
        for field, value in (("version", 3), ("sha256", "0" * 64),
                             ("mac", "0" * 64), ("algorithm", "SHA256")):
            with self.subTest(field=field):
                self.assertFalse(verify(self.m | {field: value}, self.payload, self.key, 1))

    def test_wrong_key_rejected(self):
        self.assertFalse(verify(self.m, self.payload, b"x" * 32, 1))

    def test_missing_extra_or_path_fields_rejected(self):
        for value in (None, [], {}, {k: v for k, v in self.m.items() if k != "mac"},
                      self.m | {"path": "../../outside.bin"}, self.m | {"signature": self.m["mac"]}):
            with self.subTest(value=value):
                self.assertFalse(verify(value, self.payload, self.key, 1))

    def test_digest_types_lengths_and_non_ascii_rejected(self):
        for field in ("sha256", "mac"):
            for value in (None, b"a" * 64, "a" * 63, "A" * 64, "é" * 64, []):
                with self.subTest(field=field, value=value):
                    self.assertFalse(verify(self.m | {field: value}, self.payload, self.key, 1))

    def test_versions_reject_bool_nan_fraction_and_out_of_range(self):
        for value in (True, False, 0, -1, 2.0, "2", float("nan"), MAX_VERSION + 1):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    manifest(value, self.payload, self.key)
                self.assertFalse(verify(self.m | {"version": value}, self.payload, self.key, 1))

    def test_version_boundaries_are_inclusive(self):
        self.assertEqual(manifest(1, self.payload, self.key)["version"], 1)
        top = manifest(MAX_VERSION, self.payload, self.key)
        self.assertTrue(verify(top, self.payload, self.key, MAX_VERSION - 1))

    def test_equal_older_or_invalid_current_version_rejected(self):
        for current in (2, 3, 0, True, "1", float("nan")):
            with self.subTest(current=current):
                self.assertFalse(verify(self.m, self.payload, self.key, current))

    def test_secret_contract(self):
        for key in (b"", b"x" * 31, "x" * 32, None, bytearray(b"x" * 32)):
            with self.subTest(key_type=type(key).__name__):
                with self.assertRaises(ValueError):
                    manifest(2, self.payload, key)
                self.assertFalse(verify(self.m, self.payload, key, 1))
        self.assertTrue(verify(self.m, self.payload, self.key, 1))

    def test_payload_contract(self):
        for payload in (b"", "firmware", None, bytearray(b"firmware")):
            with self.subTest(payload_type=type(payload).__name__):
                with self.assertRaises(ValueError):
                    manifest(2, payload, self.key)
                self.assertFalse(verify(self.m, payload, self.key, 1))

    def test_device_constructor_validation(self):
        for ident in ("", " ", None, 1, "x" * 65):
            with self.subTest(ident=ident):
                with self.assertRaises(ValueError):
                    Device(ident)
        with self.assertRaises(ValueError):
            Device("a", version=True)
        with self.assertRaises(ValueError):
            Device("a", payload=b"")

    def test_replay_after_apply_does_not_replace_previous(self):
        self.device.apply(self.m, self.payload, self.key)
        self.assertFalse(self.device.apply(self.m, self.payload, self.key))
        self.assertEqual(self.device.previous, (1, b"firmware-v1"))

    def test_rollback_once_does_not_toggle(self):
        self.assertFalse(self.device.rollback())
        self.device.apply(self.m, self.payload, self.key)
        self.assertTrue(self.device.rollback())
        self.assertFalse(self.device.rollback())
        self.assertEqual((self.device.version, self.device.payload), (1, b"firmware-v1"))

    def test_rollback_preserves_high_watermark_against_replay(self):
        self.device.apply(self.m, self.payload, self.key)
        self.device.rollback()
        self.assertEqual(self.device.highest_version, 2)
        self.assertFalse(self.device.apply(self.m, self.payload, self.key))
        newer = manifest(3, b"v3", self.key)
        self.assertTrue(self.device.apply(newer, b"v3", self.key))

    def test_health_failure_restores_complete_modeled_snapshot(self):
        self.device.apply(self.m, self.payload, self.key)
        before = (self.device.version, self.device.payload, self.device.previous, self.device.highest_version)
        m3 = manifest(3, b"v3", self.key)
        self.assertFalse(self.device.apply(m3, b"v3", self.key, healthy=False))
        self.assertEqual((self.device.version, self.device.payload, self.device.previous,
                          self.device.highest_version), before)
        self.assertEqual(self.device.audit[-1]["action"], "health_failed_restored")

    def test_health_failure_does_not_consume_version(self):
        self.device.apply(self.m, self.payload, self.key, healthy=False)
        self.assertTrue(self.device.apply(self.m, self.payload, self.key))

    def test_health_requires_bool_and_has_no_effect_on_invalid_input(self):
        for invalid in (0, 1, None, "false", float("nan")):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    self.device.apply(self.m, self.payload, self.key, healthy=invalid)
        self.assertEqual(self.device.audit, [])

    def test_audit_is_copied_and_excludes_shared_secret(self):
        self.device.apply(self.m, self.payload, self.key)
        log = self.device.audit
        log[0]["version"] = -1
        self.assertEqual(self.device.audit[0]["version"], 2)
        self.assertNotIn(self.key.decode(), json.dumps(self.device.audit))

    def test_serialization_key_order_does_not_change_verification(self):
        reordered = dict(reversed(list(self.m.items())))
        self.assertTrue(verify(reordered, self.payload, self.key, 1))

    def test_demo_reports_simulated_rollback_and_replay_rejection(self):
        result = demo()
        self.assertEqual(result["algorithm"], ALGORITHM)
        self.assertTrue(result["rollback"])
        self.assertFalse(result["replay_accepted"])
        self.assertFalse(result["unhealthy_accepted"])
        self.assertEqual((result["final_version"], result["highest_version"]), (1, 2))
        self.assertNotIn("secret", result)


if __name__ == "__main__":
    unittest.main()
