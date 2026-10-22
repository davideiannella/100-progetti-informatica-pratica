import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from smart_building import ZoneTwin, Building, demo


class BuildingTests(unittest.TestCase):
    def test_heating_cooling_and_off(self):
        zone = ZoneTwin("office", 18, True)
        self.assertEqual(zone.control(), "HEAT")
        zone.temp = 24
        self.assertEqual(zone.control(), "COOL")
        zone.temp = 21
        self.assertEqual(zone.control(), "OFF")

    def test_boundaries_are_off(self):
        for temperature in (20, 22):
            with self.subTest(temperature=temperature):
                self.assertEqual(ZoneTwin("office", temperature, True).control(), "OFF")

    def test_deadband_has_no_memory_hysteresis(self):
        zone = ZoneTwin("office", 18, True)
        zone.control()
        zone.temp = 20.5
        self.assertEqual(zone.control(), "OFF")

    def test_unoccupied_is_eco_even_when_cold(self):
        zone = ZoneTwin("office", 18, False)
        self.assertEqual(zone.control(), "ECO")
        self.assertAlmostEqual(zone.step_energy(2), 0.6)

    def test_energy_sums_power_times_duration(self):
        zone = ZoneTwin("office", 18, True)
        zone.control()
        self.assertEqual(zone.step_energy(1.5), 3)
        zone.temp = 21
        zone.control()
        self.assertAlmostEqual(zone.step_energy(0.5), 3.05)
        self.assertAlmostEqual(zone.step_energy(0), 3.05)

    def test_cooling_uses_distinct_rate(self):
        zone = ZoneTwin("office", 25, True)
        zone.control()
        self.assertAlmostEqual(zone.step_energy(0.5), 1.1)

    def test_invalid_temperatures_leave_previous_state(self):
        zone = ZoneTwin("office", 18, True)
        for value in (True, float("nan"), float("inf"), 10 ** 400, -51, 61, "21", None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                zone.temp = value
        self.assertEqual(zone.temp, 18)

    def test_occupied_requires_boolean(self):
        zone = ZoneTwin("office")
        for value in (0, 1, "False", None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                zone.occupied = value
        self.assertFalse(zone.occupied)

    def test_invalid_control_does_not_change_hvac(self):
        zone = ZoneTwin("office", 18, True)
        zone.control()
        for kwargs in ({"target": float("nan")}, {"target": True}, {"deadband": -1}, {"deadband": float("inf")}, {"deadband": False}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                zone.control(**kwargs)
        self.assertEqual(zone.hvac, "HEAT")

    def test_invalid_duration_does_not_change_energy(self):
        zone = ZoneTwin("office")
        for value in (-1, True, float("nan"), float("inf"), "1", None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                zone.step_energy(value)
        self.assertEqual(zone.energy_kwh, 0)

    def test_invalid_names_and_duplicate_zones(self):
        for name in ("", " ", " office", None):
            with self.subTest(name=name), self.assertRaises(ValueError):
                ZoneTwin(name)
        with self.assertRaises(ValueError):
            Building([ZoneTwin("a"), ZoneTwin("a")])
        with self.assertRaises(ValueError):
            Building([])
        with self.assertRaises(ValueError):
            Building(["not a twin"])

    def test_alarm_is_virtual_and_independent_from_hvac(self):
        zone = ZoneTwin("office", 18, True)
        zone.control()
        building = Building([zone])
        self.assertEqual(building.safety_event("smoke"), {"kind": "smoke", "local_alarm": True, "simulation": True})
        building.safety_event("water")
        self.assertEqual(building.alerts, ["smoke", "water"])
        self.assertEqual((zone.hvac, zone.energy_kwh), ("HEAT", 0))
        building.alerts.clear()
        self.assertEqual(len(building.alerts), 2)

    def test_invalid_alarm_adds_nothing(self):
        building = Building([ZoneTwin("office")])
        for kind in ("fire", "", None, [], True):
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                building.safety_event(kind)
        self.assertEqual(building.alerts, [])

    def test_demo_numbers(self):
        report = demo()
        self.assertEqual((report["heating"], report["lower_boundary"], report["unoccupied"]), ("HEAT", "OFF", "ECO"))
        self.assertEqual(report["energy_kwh"], 3.65)


if __name__ == "__main__":
    unittest.main()
