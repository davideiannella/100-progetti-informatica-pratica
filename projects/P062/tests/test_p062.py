import random
import unittest
from dr import Zone, ReplicatedService, rpo_lost_keys, recovery_duration


class DisasterRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.a, self.b = Zone("a"), Zone("b")
        self.service = ReplicatedService(self.a, self.b)

    def test_replication_and_read_failover(self):
        self.service.write("order-1", "ok", now=10)
        self.assertEqual(self.b.read("order-1"), "ok")
        self.a.up = False
        self.assertEqual(self.service.read("order-1"), ("ok", "b"))

    def test_stale_update_is_exposed(self):
        self.service.write("order", "old", now=10)
        self.b.up = False
        self.service.write("order", "new", now=20)
        self.assertEqual(rpo_lost_keys(self.a, self.b), ["order"])
        self.assertEqual(self.service.exposure(incident_time=25), {
            "pending_writes": 1, "affected_keys": ["order"],
            "recovery_point": 10, "potential_loss_window_s": 15})

    def test_unreplicated_new_key_and_multiple_updates(self):
        self.b.up = False
        for i in range(3):
            self.service.write("order", i, now=i + 1)
        self.assertEqual(rpo_lost_keys(self.a, self.b), ["order"])
        self.assertEqual(self.service.exposure(incident_time=5)["pending_writes"], 3)
        self.assertEqual(self.service.exposure(incident_time=5)["affected_keys"], ["order"])

    def test_catchup_and_idempotence(self):
        self.b.up = False
        self.service.write("a", 1)
        self.service.write("a", 2)
        self.service.write("b", 3)
        self.b.up = True
        self.service.catch_up()
        self.service.catch_up()
        self.assertEqual(self.b.data, {"a": 2, "b": 3})
        self.assertEqual(self.service.acked, 3)
        self.assertEqual(self.service.exposure(incident_time=100)["potential_loss_window_s"], 0)

    def test_values_do_not_alias(self):
        value = {"items": [1]}
        self.service.write("a", value)
        value["items"].append(2)
        result, _ = self.service.read("a")
        result["items"].append(3)
        self.assertEqual(self.a.read("a"), {"items": [1]})
        self.assertEqual(self.b.read("a"), {"items": [1]})

    def test_write_primary_down_is_rejected(self):
        self.a.up = False
        with self.assertRaises(RuntimeError):
            self.service.write("a", 1)
        self.assertEqual(self.service.journal, [])
        self.assertEqual(self.b.data, {})

    def test_both_down_and_missing_key_fail(self):
        with self.assertRaises(KeyError):
            self.service.read("missing")
        self.a.up = self.b.up = False
        with self.assertRaises(RuntimeError):
            self.service.read("missing")
        with self.assertRaises(RuntimeError):
            self.service.catch_up()

    def test_clock_and_interval_validation(self):
        self.service.write("a", 1, now=10)
        for value in (-1, 9, float("nan"), float("inf"), True, "10"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.service.write("a", 2, now=value)
        self.assertEqual(self.a.read("a"), 1)
        with self.assertRaises(ValueError):
            self.service.exposure(incident_time=9)
        with self.assertRaises(ValueError):
            recovery_duration(5, 4)
        self.assertEqual(recovery_duration(5, 5), 0)
        self.assertEqual(recovery_duration(5, 8), 3)

    def test_invalid_initial_topology(self):
        with self.assertRaises(ValueError):
            ReplicatedService(self.a, self.a)
        with self.assertRaises(ValueError):
            ReplicatedService(self.a, Zone("a"))
        self.a.write("existing", 1)
        with self.assertRaises(ValueError):
            ReplicatedService(self.a, self.b)

    def test_100_seeded_partition_scenarios(self):
        rng = random.Random(62062)
        for case in range(100):
            with self.subTest(case=case):
                a, b = Zone("a"), Zone("b")
                service, reference = ReplicatedService(a, b), {}
                for instant in range(1, 41):
                    b.up = rng.random() < 0.6
                    key, value = "k" + str(rng.randrange(6)), rng.randrange(1000)
                    service.write(key, value, now=instant)
                    reference[key] = value
                    self.assertEqual(a.data, reference)
                    self.assertEqual(service.exposure(incident_time=instant)["pending_writes"], len(service.journal) - service.acked)
                    if b.up:
                        self.assertEqual(b.data, reference)
                b.up = True
                service.catch_up()
                self.assertEqual(a.data, b.data)
                self.assertEqual(rpo_lost_keys(a, b), [])
