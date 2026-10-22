from dataclasses import FrozenInstanceError
import pathlib
import sys
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).parents[1] / "src"))
from smart_factory import MachineTwin, Plant, demo


def machine(**changes):
    fields = dict(name="M1", planned_min=480, runtime_min=420, total_count=380,
                  good_count=370, ideal_cycle_min=1.0, vibration=2.0)
    return MachineTwin(**(fields | changes))


class FactoryTests(unittest.TestCase):
    def test_known_availability_performance_quality_and_oee(self):
        metrics = machine().oee()
        self.assertAlmostEqual(metrics["availability"], 420 / 480)
        self.assertAlmostEqual(metrics["performance"], 380 / 420)
        self.assertAlmostEqual(metrics["quality"], 370 / 380)
        self.assertAlmostEqual(metrics["oee"], 370 / 480)

    def test_perfect_machine_at_upper_bound(self):
        self.assertEqual(machine(planned_min=10, runtime_min=10, total_count=10,
                                 good_count=10).oee(),
                         dict(availability=1, performance=1, quality=1, oee=1))

    def test_decimal_cycle_boundary_does_not_reject_float_rounding(self):
        metrics = machine(planned_min=1.0, runtime_min=0.3, total_count=3,
                          good_count=3, ideal_cycle_min=0.1).oee()
        self.assertEqual(metrics["performance"], 1.0)
        self.assertEqual(metrics["oee"], 0.3)
        with self.assertRaises(ValueError):
            machine(planned_min=1.0, runtime_min=0.3, total_count=3,
                    good_count=3, ideal_cycle_min=0.10000001)

    def test_decimal_planned_boundary_is_bounded_only_within_tolerance(self):
        metrics = machine(planned_min=0.3, runtime_min=0.1 * 3, total_count=3,
                          good_count=3, ideal_cycle_min=0.1).oee()
        self.assertEqual(metrics, dict(availability=1, performance=1, quality=1, oee=1))
        with self.assertRaises(ValueError):
            machine(planned_min=0.3, runtime_min=0.30000001, total_count=3,
                    good_count=3, ideal_cycle_min=0.1)

    def test_stopped_machine_has_zero_components(self):
        self.assertEqual(machine(runtime_min=0, total_count=0, good_count=0).oee(),
                         dict(availability=0, performance=0, quality=0, oee=0))

    def test_runtime_without_production_has_zero_quality_by_convention(self):
        metrics = machine(total_count=0, good_count=0).oee()
        self.assertGreater(metrics["availability"], 0)
        self.assertEqual((metrics["performance"], metrics["quality"], metrics["oee"]), (0, 0, 0))

    def test_all_scrap_has_zero_quality(self):
        self.assertEqual(machine(good_count=0).oee()["oee"], 0)

    def test_runtime_cannot_exceed_planned_time(self):
        with self.assertRaises(ValueError):
            machine(runtime_min=481)

    def test_impossible_cycle_or_zero_runtime_production_rejected(self):
        for changes in ({"ideal_cycle_min": 2}, {"runtime_min": 0},
                        {"good_count": 381}, {"planned_min": 0}, {"ideal_cycle_min": 0}):
            with self.subTest(changes=changes):
                with self.assertRaises(ValueError):
                    machine(**changes)

    def test_finite_numeric_fields_reject_nan_inf_bool_and_strings(self):
        for field in ("planned_min", "runtime_min", "ideal_cycle_min", "vibration"):
            for value in (float("nan"), float("inf"), float("-inf"), True, "1", None, 10**1000):
                with self.subTest(field=field, value_type=type(value).__name__):
                    with self.assertRaises(ValueError):
                        machine(**{field: value})

    def test_negative_measurements_rejected(self):
        for field in ("planned_min", "runtime_min", "ideal_cycle_min", "vibration"):
            with self.subTest(field=field):
                with self.assertRaises(ValueError):
                    machine(**{field: -1})

    def test_count_contract_rejects_bool_float_and_out_of_range(self):
        for field in ("total_count", "good_count"):
            for value in (True, 1.5, -1, 2**31, float("nan"), None):
                with self.subTest(field=field, value=value):
                    with self.assertRaises(ValueError):
                        machine(**{field: value})

    def test_names_must_be_nonempty_bounded_strings(self):
        for value in ("", " ", "x" * 65, None, 3):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    machine(name=value)

    def test_validated_twin_is_immutable(self):
        twin = machine()
        with self.assertRaises(FrozenInstanceError):
            twin.runtime_min = -1

    def test_maintenance_threshold_is_strict(self):
        twin = machine(vibration=4)
        self.assertFalse(twin.maintenance_signal(4))
        self.assertTrue(twin.maintenance_signal(3.999))
        self.assertTrue(machine(vibration=5.2).maintenance_signal())

    def test_maintenance_limit_must_be_finite_nonnegative(self):
        for value in (-1, True, float("nan"), float("inf"), "4"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    machine().maintenance_signal(value)
                with self.assertRaises(ValueError):
                    Plant([]).summary(value)

    def test_empty_plant_has_no_mean(self):
        self.assertEqual(Plant([]).summary(), {"machines": 0, "mean_oee": None, "maintenance": []})

    def test_plant_rejects_duplicate_machine_names(self):
        with self.assertRaises(ValueError):
            Plant([machine(), machine()])

    def test_plant_rejects_non_twin_members(self):
        with self.assertRaises(ValueError):
            Plant([machine(), {}])

    def test_plant_keeps_its_own_machine_sequence(self):
        source = [machine()]
        plant = Plant(source)
        source.clear()
        self.assertEqual(plant.summary()["machines"], 1)

    def test_mean_oee_is_arithmetic_not_a_weighted_plant_oee(self):
        one = machine(name="A", planned_min=10, runtime_min=10, total_count=10, good_count=5)
        two = machine(name="B", planned_min=100, runtime_min=100, total_count=100, good_count=100)
        self.assertEqual(Plant([one, two]).summary()["mean_oee"], 0.75)
        self.assertNotAlmostEqual(0.75, 105 / 110)

    def test_demo_reports_two_machines_and_one_rule_signal(self):
        result = demo()
        self.assertTrue(result["simulation_only"])
        self.assertAlmostEqual(result["summary"]["mean_oee"], 0.7291666666666667)
        self.assertEqual(result["summary"]["maintenance"], ["M2"])
        self.assertEqual(result["units"]["vibration"], "mm/s")


if __name__ == "__main__":
    unittest.main()
