import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from governance import CONTROLS, decision_record, demo, governance_check


def full():
    return {name: True for names in CONTROLS.values() for name in names}


class GovernanceTest(unittest.TestCase):
    def test_full_checklist_only(self):
        result = governance_check(full())
        self.assertEqual(result, {"complete": True, "missing": [], "satisfied": 11, "total": 11})

    def test_empty_lists_every_control_in_stable_order(self):
        result = governance_check({})
        self.assertEqual(result["missing"], [f"{area}:{name}" for area, names in CONTROLS.items() for name in names])
        self.assertEqual(result["satisfied"], 0)

    def test_false_and_absent_are_missing(self):
        controls = full()
        controls["monitoring"] = False
        del controls["privacy"]
        self.assertEqual(governance_check(controls)["missing"], ["data:privacy", "operations:monitoring"])

    def test_truthy_non_booleans_are_rejected(self):
        for value in ("False", "True", 1, 0, None, float("nan"), [], {}):
            with self.subTest(value=value), self.assertRaises(ValueError):
                governance_check({"monitoring": value})

    def test_unknown_key_catches_typo(self):
        with self.assertRaises(ValueError):
            governance_check({"monitroing": True})

    def test_non_mapping_rejected(self):
        for value in (None, [], "privacy", True):
            with self.subTest(value=value), self.assertRaises(ValueError):
                governance_check(value)

    def test_input_is_not_modified_and_missing_is_fresh(self):
        controls = {"privacy": True}
        before = controls.copy()
        result = governance_check(controls)
        result["missing"].clear()
        self.assertEqual(controls, before)
        self.assertEqual(len(governance_check(controls)["missing"]), 10)

    def test_record_trims_all_fields(self):
        result = decision_record(" TicketAI ", " Scopo ", " Owner ", " Limiti ")
        self.assertEqual(result, {"name": "TicketAI", "purpose": "Scopo", "owner": "Owner", "limitations": "Limiti"})

    def test_record_rejects_each_missing_or_invalid_field(self):
        for index in range(4):
            for invalid in ("", " \n\t ", None, True, 123):
                values = ["Name", "Purpose", "Owner", "Limits"]
                values[index] = invalid
                with self.subTest(index=index, invalid=invalid), self.assertRaises(ValueError):
                    decision_record(*values)

    def test_record_length_boundary(self):
        self.assertEqual(len(decision_record("x" * 2000, "p", "o", "l")["name"]), 2000)
        with self.assertRaises(ValueError):
            decision_record("x" * 2001, "p", "o", "l")

    def test_input_order_does_not_change_report_order(self):
        controls = dict(reversed(list(full().items())))
        controls["quality"] = controls["logging"] = False
        self.assertEqual(governance_check(controls)["missing"], ["data:quality", "operations:logging"])

    def test_demo_reports_two_operational_gaps(self):
        result = demo()
        self.assertEqual(result["checklist"]["satisfied"], 9)
        self.assertEqual(result["checklist"]["missing"], ["operations:monitoring", "operations:incident_response"])
        self.assertFalse(result["checklist"]["complete"])


if __name__ == "__main__":
    unittest.main()
