import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from irrigation import IrrigationTwin, demo


class IrrigationTest(unittest.TestCase):
    def test_default_is_off_without_a_control_step(self):
        twin = IrrigationTwin()
        self.assertEqual(twin.moisture, 45.0)
        self.assertFalse(twin.pump)
        self.assertEqual(twin.history, [])

    def test_exact_low_threshold_does_not_turn_on(self):
        twin = IrrigationTwin(31)
        result = twin.step(evaporation=1)
        self.assertEqual(result["moisture"], 30)
        self.assertFalse(result["pump"])
        self.assertEqual(result["reason"], "hold")

    def test_below_low_threshold_turns_on(self):
        result = IrrigationTwin(30).step(evaporation=0.01)
        self.assertTrue(result["pump"])
        self.assertEqual(result["reason"], "below_on_threshold")
        self.assertEqual(result["irrigation"], 0)

    def test_exact_high_threshold_does_not_turn_off(self):
        twin = IrrigationTwin(25)
        twin.step(evaporation=0)
        result = twin.step(rain=15, evaporation=0)
        self.assertEqual(result["moisture"], 45)
        self.assertTrue(result["pump"])
        self.assertEqual(result["reason"], "hold")

    def test_above_high_threshold_turns_off(self):
        twin = IrrigationTwin(25)
        twin.step(evaporation=0)
        result = twin.step(rain=15.01, evaporation=0)
        self.assertFalse(result["pump"])
        self.assertEqual(result["reason"], "above_off_threshold")

    def test_same_moisture_in_deadband_keeps_previous_state(self):
        off = IrrigationTwin(35).step(evaporation=0)
        on = IrrigationTwin(25)
        on.step(evaporation=0)
        result = on.step(rain=5, evaporation=0)
        self.assertEqual(off["moisture"], result["moisture"])
        self.assertFalse(off["pump"])
        self.assertTrue(result["pump"])

    def test_old_pump_is_used_before_new_decision(self):
        twin = IrrigationTwin(29)
        first = twin.step(evaporation=0)
        second = twin.step(evaporation=0)
        self.assertEqual((first["moisture"], first["irrigation"], first["pump"]), (29, 0, True))
        self.assertEqual((second["moisture"], second["irrigation"], second["pump"]), (34, 5, True))

    def test_saturation_at_zero_and_hundred(self):
        self.assertEqual(IrrigationTwin(1).step(evaporation=200)["moisture"], 0)
        self.assertEqual(IrrigationTwin(99).step(rain=200, evaporation=0)["moisture"], 100)

    def test_rain_and_evaporation_contribute_once(self):
        result = IrrigationTwin(40).step(rain=4, evaporation=2)
        self.assertEqual(result["moisture"], 42)

    def test_invalid_initial_numbers_and_bounds(self):
        for value in (-1, 101, True, None, "45", float("nan"), float("inf"), 10 ** 1000):
            with self.subTest(value=repr(value)), self.assertRaises(ValueError):
                IrrigationTwin(value)

    def test_thresholds_are_finite_ordered_and_bounded(self):
        for low, high in ((30, 30), (50, 40), (-1, 45), (30, 101), (True, 45), (30, float("nan"))):
            with self.subTest(low=low, high=high), self.assertRaises(ValueError):
                IrrigationTwin(on_below=low, off_above=high)

    def test_invalid_step_is_atomic(self):
        twin = IrrigationTwin(29)
        for field in ("rain", "evaporation"):
            for value in (-1, True, "1", None, float("nan"), float("inf"), 10 ** 1000):
                with self.subTest(field=field, value=repr(value)), self.assertRaises(ValueError):
                    twin.step(**{field: value})
                self.assertEqual(twin.moisture, 29)
                self.assertFalse(twin.pump)
                self.assertEqual(twin.history, [])

    def test_history_and_result_cannot_modify_internal_history(self):
        twin = IrrigationTwin(29)
        result = twin.step()
        result["pump"] = False
        history = twin.history
        history[0]["moisture"] = 99
        history.clear()
        self.assertEqual(twin.history[0]["moisture"], 28)
        self.assertTrue(twin.history[0]["pump"])

    def test_threshold_extremes_remain_strict(self):
        twin = IrrigationTwin(0, on_below=0, off_above=100)
        self.assertFalse(twin.step(evaporation=10)["pump"])
        self.assertEqual(twin.moisture, 0)

    def test_demo_values_are_executable(self):
        history = demo()["history"]
        self.assertEqual([r["moisture"] for r in history], [30, 29, 34, 39, 44, 49, 48])
        self.assertEqual([r["pump"] for r in history], [False, True, True, True, True, False, False])
        self.assertEqual([r["step"] for r in history if r["reason"] != "hold"], [2, 6])


if __name__ == "__main__":
    unittest.main()
