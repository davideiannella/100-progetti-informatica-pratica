import itertools
import pathlib
import random
import sys
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from threat_model import STRIDE, make_threat, risk


class ThreatModelTests(unittest.TestCase):
    def test_exhaustive_25_scores(self):
        expected_bands = [
            ["low", "low", "low", "low", "low"],
            ["low", "low", "medium", "medium", "medium"],
            ["low", "medium", "medium", "medium", "high"],
            ["low", "medium", "medium", "high", "high"],
            ["low", "medium", "high", "high", "high"],
        ]
        for likelihood, impact in itertools.product(range(1, 6), repeat=2):
            with self.subTest(likelihood=likelihood, impact=impact):
                self.assertEqual(risk(likelihood, impact), (likelihood * impact, expected_bands[likelihood-1][impact-1]))

    def test_all_categories_and_input_retention(self):
        names = ["Spoofing", "Tampering", "Repudiation", "Information Disclosure", "Denial of Service", "Elevation of Privilege"]
        for letter, name in zip("STRIDE", names):
            t = make_threat(" login ", letter, 4, 4, " MFA ", rationale=" motivazione ")
            self.assertEqual(t["category"], name)
            self.assertEqual((t["component"], t["mitigation"], t["rationale"]), ("login", "MFA", "motivazione"))
            self.assertEqual((t["likelihood"], t["impact"], t["score"], t["band"]), (4, 4, 16, "high"))

    def test_invalid_scale(self):
        for value in (True, False, 0, 6, -1, 1.0, 5.0, float("nan"), float("inf"), "2", None, [], {}):
            for args in ((value, 2), (2, value)):
                with self.subTest(args=args):
                    with self.assertRaises(ValueError): risk(*args)

    def test_invalid_category(self):
        for value in ("", "s", "S ", "X", None, [], 1):
            with self.subTest(value=value):
                with self.assertRaises(ValueError): make_threat("login", value, 1, 1, "MFA")

    def test_empty_fields(self):
        for value in ("", " \t", None, 1, [], {}):
            with self.subTest(value=value):
                with self.assertRaises(ValueError): make_threat(value, "S", 1, 1, "MFA")
                with self.assertRaises(ValueError): make_threat("login", "S", 1, 1, value)
        with self.assertRaises(ValueError): make_threat("login", "S", 1, 1, "MFA", rationale=" ")

    def test_symmetry_and_monotonicity(self):
        for a, b in itertools.product(range(1, 6), repeat=2):
            self.assertEqual(risk(a, b), risk(b, a))
            if a < 5: self.assertLess(risk(a, b)[0], risk(a+1, b)[0])
            if b < 5: self.assertLess(risk(a, b)[0], risk(a, b+1)[0])

    def test_immutable_categories_and_independent_records(self):
        with self.assertRaises(TypeError): STRIDE["S"] = "changed"
        a = make_threat("a", "S", 2, 2, "control"); b = make_threat("a", "S", 2, 2, "control")
        a["score"] = 0
        self.assertEqual(b["score"], 4)


    def test_exhaustive_residual_225_combinations(self):
        count = 0
        for likelihood, impact in itertools.product(range(1, 6), repeat=2):
            before = risk(likelihood, impact)
            for reduced_likelihood in range(1, likelihood+1):
                for reduced_impact in range(1, impact+1):
                    residual = risk(reduced_likelihood, reduced_impact)
                    self.assertLessEqual(residual[0], before[0])
                    order = {"low": 0, "medium": 1, "high": 2}
                    self.assertLessEqual(order[residual[1]], order[before[1]])
                    count += 1
        self.assertEqual(count, 225)

if __name__ == "__main__": unittest.main(verbosity=2)
