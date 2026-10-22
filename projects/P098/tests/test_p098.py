import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from resilient_monitor import Collector, EdgeNode, demo


class MonitorTests(unittest.TestCase):
    def setUp(self):
        self.node, self.collector = EdgeNode("env-1"), Collector()

    def test_offline_retains_fifo(self):
        self.node.online = False
        self.node.sample(10)
        self.node.sample(11)
        self.assertEqual(self.node.flush(self.collector), 0)
        self.assertEqual([event["seq"] for event in self.node.buffer], [1, 2])
        self.assertEqual(self.collector.events, [])

    def test_reconnect_drains_in_order(self):
        self.node.sample(10)
        self.node.sample(11)
        self.assertEqual(self.node.flush(self.collector), 2)
        self.assertEqual([event["seq"] for event in self.collector.events], [1, 2])
        self.assertEqual(self.node.buffer, [])
        self.assertEqual(self.node.flush(self.collector), 0)

    def test_duplicate_ack_has_no_second_effect(self):
        event = self.node.sample(10)
        self.assertTrue(self.collector.ingest(event)["inserted"])
        self.assertFalse(self.collector.ingest(event)["inserted"])
        self.assertEqual(self.node.flush(self.collector), 1)
        self.assertEqual(len(self.collector.events), 1)

    def test_conflicting_duplicate_is_rejected(self):
        event = self.node.sample(10)
        self.collector.ingest(event)
        event["value"] = 11
        with self.assertRaises(ValueError):
            self.collector.ingest(event)
        self.assertEqual(self.collector.events[0]["value"], 10)

    def test_new_event_gap_is_rejected(self):
        with self.assertRaises(ValueError):
            self.collector.ingest({"device": "env-1", "seq": 2, "value": 10})
        self.assertEqual(self.collector.events, [])

    def test_devices_have_independent_sequences(self):
        second = EdgeNode("env-2")
        self.node.sample(-3)
        second.sample(5)
        self.node.flush(self.collector)
        second.flush(self.collector)
        self.assertEqual([(e["device"], e["seq"]) for e in self.collector.events], [("env-1", 1), ("env-2", 1)])

    def test_network_error_before_acceptance_keeps_all_events(self):
        self.node.sample(10)
        self.node.sample(11)
        class Down:
            def ingest(self, event):
                raise ConnectionError("offline")
        self.assertEqual(self.node.flush(Down()), 0)
        self.assertFalse(self.node.online)
        self.assertEqual(len(self.node.buffer), 2)
        self.node.online = True
        self.assertEqual(self.node.flush(self.collector), 2)

    def test_lost_ack_replay_deduplicates_then_continues(self):
        self.node.sample(10)
        self.node.sample(11)
        collector = self.collector
        class LostAck:
            def ingest(self, event):
                collector.ingest(event)
                raise TimeoutError("ACK perso")
        self.assertEqual(self.node.flush(LostAck()), 0)
        self.assertEqual((len(self.node.buffer), len(self.collector.events)), (2, 1))
        self.node.online = True
        self.assertEqual(self.node.flush(self.collector), 2)
        self.assertEqual([e["seq"] for e in self.collector.events], [1, 2])

    def test_partial_flush_keeps_head_and_suffix_on_error(self):
        for value in (10, 11, 12):
            self.node.sample(value)
        collector = self.collector
        class Partial:
            def ingest(self, event):
                if event["seq"] == 2:
                    raise ConnectionError("guasto")
                return collector.ingest(event)
        self.assertEqual(self.node.flush(Partial()), 1)
        self.assertEqual([e["seq"] for e in self.node.buffer], [2, 3])
        self.node.online = True
        self.assertEqual(self.node.flush(self.collector), 2)

    def test_wrong_or_missing_ack_cannot_discard_event(self):
        self.node.sample(10)
        for bad in (None, False, {"ack": False}, {"ack": True, "device": "other", "seq": 1}, {"ack": True, "device": "env-1", "seq": True}):
            class InvalidAck:
                def ingest(self, event):
                    return bad
            with self.subTest(ack=bad), self.assertRaises(ValueError):
                self.node.flush(InvalidAck())
            self.assertEqual(len(self.node.buffer), 1)

    def test_collector_validation_error_preserves_head(self):
        self.node.sample(10)
        class Invalid:
            def ingest(self, event):
                raise ValueError("rifiuto")
        with self.assertRaises(ValueError):
            self.node.flush(Invalid())
        self.assertEqual(self.node.buffer[0]["seq"], 1)

    def test_invalid_samples_do_not_consume_sequence(self):
        for value in (float("nan"), float("inf"), 10 ** 400, True, "10", None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.node.sample(value)
        self.assertEqual((self.node.seq, self.node.buffer), (0, []))
        self.assertEqual(self.node.sample(-10)["seq"], 1)

    def test_invalid_event_schema_and_sequence(self):
        for event in ({}, {"device": "a", "seq": True, "value": 2}, {"device": "a", "seq": 0, "value": 2}, {"device": "a", "seq": 1.0, "value": 2}, {"device": "a", "seq": 1, "value": float("nan")}, {"device": "a", "seq": 1, "value": 2, "extra": 3}):
            with self.subTest(event=event), self.assertRaises(ValueError):
                self.collector.ingest(event)
        self.assertEqual(self.collector.events, [])

    def test_invalid_identity_and_online_flag(self):
        for value in ("", " ", None, True):
            with self.subTest(value=value), self.assertRaises(ValueError):
                EdgeNode(value)
        with self.assertRaises(ValueError):
            self.node.online = 1
        self.assertTrue(self.node.online)

    def test_snapshots_do_not_modify_buffer_or_collector(self):
        event = self.node.sample(10)
        event["value"] = -99
        self.node.buffer.clear()
        self.node.flush(self.collector)
        self.collector.events[0]["value"] = -88
        self.assertEqual(self.collector.events[0]["value"], 10)

    def test_restart_loses_ram_state_and_detects_sequence_conflict(self):
        self.node.sample(10)
        self.node.flush(self.collector)
        restarted = EdgeNode("env-1")
        restarted.sample(20)
        with self.assertRaises(ValueError):
            restarted.flush(self.collector)
        self.assertEqual(restarted.buffer[0]["seq"], 1)
        self.assertEqual(Collector().events, [])

    def test_demo_numbers(self):
        self.assertEqual(demo(), {"mode": "buffer_in_memoria", "offline_ack": 0, "reconnect_ack": 2,
                                 "pending": 0, "sequence": [1, 2], "replay_inserted": False})


if __name__ == "__main__":
    unittest.main()
