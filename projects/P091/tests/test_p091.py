import pathlib
import sys
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).parents[1] / "src"))
from home_safety import SafetyController, demo


class SafetyTests(unittest.TestCase):
    def setUp(self):
        self.controller = SafetyController()

    def test_normal_has_no_actions_or_transition(self):
        self.assertEqual(self.controller.ingest(), ("NORMAL", []))
        self.assertEqual(self.controller.audit, [])

    def test_smoke_requests_two_local_actions(self):
        self.assertEqual(self.controller.ingest(smoke=True),
                         ("FIRE_ALERT", ["sound_virtual_alarm", "cut_virtual_nonessential_power"]))

    def test_water_requests_valve(self):
        self.assertEqual(self.controller.ingest(water=True),
                         ("WATER_ALERT", ["close_virtual_valve"]))

    def test_both_prioritizes_state_without_losing_water_action(self):
        state, actions = self.controller.ingest(smoke=True, water=True)
        self.assertEqual(state, "FIRE_ALERT")
        self.assertEqual(len(actions), 3)
        self.assertIn("close_virtual_valve", actions)

    def test_return_to_normal_is_automatic_in_this_simulation(self):
        self.controller.ingest(True, True)
        self.assertEqual(self.controller.ingest(), ("NORMAL", []))
        self.assertEqual(self.controller.audit[-1]["previous"], "FIRE_ALERT")

    def test_fire_to_water_transition(self):
        self.controller.ingest(True, True)
        self.assertEqual(self.controller.ingest(False, True)[0], "WATER_ALERT")

    def test_same_state_different_hazard_is_recorded(self):
        self.controller.ingest(True, False)
        self.controller.ingest(True, True)
        self.assertEqual(len(self.controller.audit), 2)
        self.assertEqual(self.controller.audit[-1]["previous"], "FIRE_ALERT")
        self.assertIn("close_virtual_valve", self.controller.audit[-1]["local_actions"])

    def test_repeated_sample_does_not_duplicate_notification(self):
        expected = self.controller.ingest(True, True)
        self.assertEqual(self.controller.ingest(True, True), expected)
        self.assertEqual(len(self.controller.audit), 1)
        self.assertEqual(len(self.controller.delivered), 1)

    def test_offline_decision_and_ordered_single_flush(self):
        self.controller.ingest(False, True, False)
        self.controller.ingest(True, True, False)
        self.assertEqual(len(self.controller.pending), 2)
        self.assertEqual(self.controller.delivered, [])
        self.assertEqual(self.controller.state, "FIRE_ALERT")
        self.controller.ingest(True, True, True)
        self.controller.ingest(True, True, True)
        self.assertEqual(self.controller.pending, [])
        self.assertEqual([e["sequence"] for e in self.controller.delivered], [1, 2])

    def test_invalid_booleans_rejected_without_mutation(self):
        self.controller.ingest(water=True, cloud_online=False)
        before = (self.controller.state, self.controller.audit, self.controller.pending)
        for field in ("smoke", "water", "cloud_online"):
            for invalid in (0, 1, "false", None, float("nan"), [], {}):
                with self.subTest(field=field, invalid=repr(invalid)):
                    with self.assertRaises(ValueError):
                        self.controller.ingest(**{field: invalid})
                    self.assertEqual((self.controller.state, self.controller.audit,
                                      self.controller.pending), before)

    def test_returned_lists_do_not_modify_controller(self):
        _, actions = self.controller.ingest(water=True)
        actions.clear()
        audit = self.controller.audit
        audit[0]["local_actions"].clear()
        delivered = self.controller.delivered
        delivered.clear()
        self.assertEqual(self.controller.actions, ["close_virtual_valve"])
        self.assertEqual(self.controller.audit[0]["local_actions"], ["close_virtual_valve"])
        self.assertEqual(len(self.controller.delivered), 1)

    def test_instances_do_not_share_state(self):
        self.controller.ingest(smoke=True)
        other = SafetyController()
        self.assertEqual(other.ingest(), ("NORMAL", []))

    def test_demo_has_six_samples_and_four_transitions(self):
        result = demo()
        self.assertTrue(result["simulation_only"])
        self.assertEqual(len(result["samples"]), 6)
        self.assertEqual(len(result["audit"]), 4)
        self.assertEqual(result["samples"][-1]["delivered"], 4)


if __name__ == "__main__":
    unittest.main()
