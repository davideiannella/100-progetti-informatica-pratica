from dataclasses import FrozenInstanceError
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from access import AccessControl, Badge, demo


class AccessTest(unittest.TestCase):
    def setUp(self):
        self.system = AccessControl()
        self.system.register(Badge("B1", "Anna", "employee"))

    def test_permission_matrix(self):
        expected = {"employee": {"office"}, "admin": {"office", "server"}, "guest": {"lobby"}}
        for role, zones in expected.items():
            self.system.register(Badge(role, role, role))
            for zone in ("office", "server", "lobby"):
                with self.subTest(role=role, zone=zone):
                    self.assertEqual(self.system.authorize(role, zone, 1), zone in zones)
        self.assertEqual(len(self.system.audit), 9)

    def test_unknown_badge_is_audited(self):
        self.assertFalse(self.system.authorize("NO", "office", 1))
        self.assertEqual(self.system.audit[-1]["reason"], "unknown_badge")

    def test_inactive_badge_is_denied(self):
        self.system.register(Badge("B2", "Luca", "admin", active=False))
        self.assertFalse(self.system.authorize("B2", "server", 1))
        self.assertEqual(self.system.audit[-1]["reason"], "inactive_badge")

    def test_revoke_changes_future_decisions_and_is_idempotent(self):
        self.assertTrue(self.system.authorize("B1", "office", 1))
        self.assertTrue(self.system.revoke("B1"))
        self.assertFalse(self.system.revoke("B1"))
        self.assertFalse(self.system.authorize("B1", "office", 2))
        self.assertEqual(self.system.audit[-1]["reason"], "inactive_badge")

    def test_revoke_unknown_does_not_create_badge(self):
        with self.assertRaises(ValueError):
            self.system.revoke("UNKNOWN")
        self.assertEqual(list(self.system.badges), ["B1"])

    def test_duplicate_cannot_replace_privileges(self):
        with self.assertRaises(ValueError):
            self.system.register(Badge("B1", "Altro", "admin"))
        self.assertEqual(self.system.badges["B1"].role, "employee")
        self.assertFalse(self.system.authorize("B1", "server", 1))
        self.assertEqual(self.system.audit[-1]["reason"], "role_not_permitted")

    def test_trimmed_identifier_collision_is_rejected(self):
        with self.assertRaises(ValueError):
            self.system.register(Badge(" B1 ", "Altro", "guest"))
        self.assertTrue(self.system.authorize(" B1 ", " office ", 1))

    def test_badge_fields_are_validated(self):
        cases = (("", "Anna", "employee", True), (True, "Anna", "employee", True),
                 ("B/2", "Anna", "employee", True), ("B2", " ", "employee", True),
                 ("B2", "Anna", "root", True), ("B2", "Anna", "employee", 1),
                 ("B2", "Anna", "employee", "False"))
        for values in cases:
            with self.subTest(values=values), self.assertRaises(ValueError):
                Badge(*values)

    def test_registration_requires_badge(self):
        with self.assertRaises(ValueError):
            self.system.register({"id": "B2", "role": "admin"})

    def test_invalid_timestamp_is_rejected_before_audit(self):
        for value in (-1, True, 1.0, "1", None, float("nan"), float("inf")):
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.system.authorize("B1", "office", value)
        self.assertEqual(self.system.audit, [])

    def test_unknown_zone_has_distinct_reason(self):
        self.assertFalse(self.system.authorize("B1", "warehouse", 1))
        self.assertEqual(self.system.audit[-1]["reason"], "unknown_zone")

    def test_malformed_request_does_not_modify_state(self):
        for badge, zone in (("", "office"), ("B1", " "), (None, "office"), ("B1", True)):
            with self.subTest(badge=badge, zone=zone), self.assertRaises(ValueError):
                self.system.authorize(badge, zone, 1)
        self.assertEqual(self.system.audit, [])
        self.assertEqual(len(self.system.badges), 1)

    def test_audit_snapshot_and_policy_are_protected(self):
        self.system.authorize("B1", "office", 1)
        snapshot = self.system.audit
        snapshot[0]["allowed"] = False
        snapshot.clear()
        self.assertTrue(self.system.audit[0]["allowed"])
        with self.assertRaises(TypeError):
            self.system.permissions["employee"] = {"server"}
        with self.assertRaises(TypeError):
            self.system.badges["B2"] = Badge("B2", "Luca", "admin")

    def test_duplicate_attempts_and_call_order_are_preserved(self):
        self.system.authorize("B1", "office", 20)
        self.system.authorize("B1", "office", 10)
        self.system.authorize("B1", "office", 10)
        self.assertEqual([r["ts"] for r in self.system.audit], [20, 10, 10])

    def test_badge_is_frozen(self):
        with self.assertRaises(FrozenInstanceError):
            self.system.badges["B1"].role = "admin"

    def test_length_boundaries(self):
        self.assertEqual(len(Badge("x" * 64, "a" * 120, "guest").id), 64)
        for values in (("x" * 65, "Anna", "guest"), ("B2", "a" * 121, "guest")):
            with self.subTest(values=values), self.assertRaises(ValueError):
                Badge(*values)

    def test_demo_totals_and_reasons(self):
        result = demo()
        self.assertEqual((result["allowed"], result["denied"]), (2, 4))
        self.assertEqual([r["reason"] for r in result["audit"]],
                         ["granted", "role_not_permitted", "granted", "inactive_badge", "unknown_badge", "unknown_zone"])


if __name__ == "__main__":
    unittest.main()
