from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from iot_simulator import Collector, SensorSimulator, Telemetry, VirtualBroker, demo

STAMP = datetime(2026, 10, 21, 12, 0, tzinfo=timezone.utc)


def payload(**changes):
    result = {"schema": "telemetry.v1", "device_id": "S01", "seq": 0,
              "temperature_c": 22.0, "humidity_pct": 50.0, "timestamp": STAMP.isoformat()}
    result.update(changes)
    return json.dumps(result)


class IoTSimulatorTest(unittest.TestCase):
    def setUp(self):
        self.broker, self.collector = VirtualBroker(), Collector()
        self.topic = "devices/S01/telemetry"
        self.broker.subscribe(self.topic, self.collector.on_message)
        self.sensor = SensorSimulator("S01", self.broker, seed=7, clock=lambda: STAMP)

    def test_publish_delivers_valid_schema(self):
        self.assertTrue(self.sensor.publish_once())
        self.assertEqual(len(self.collector.messages), 1)
        data = self.collector.messages[0]
        self.assertEqual((data["schema"], data["device_id"], data["seq"]), ("telemetry.v1", "S01", 0))
        self.assertEqual(data["timestamp"], STAMP.isoformat())

    def test_seed_and_clock_are_reproducible(self):
        other = SensorSimulator("S01", self.broker, seed=7, clock=lambda: STAMP)
        first, second = self.sensor.sample(), other.sample()
        self.assertEqual(first.to_json(), second.to_json())
        self.assertEqual(json.loads(first.to_json())["temperature_c"], 21.93)
        self.assertEqual(json.loads(first.to_json())["humidity_pct"], 53.65)
        self.assertEqual(self.sensor.sample().seq, first.seq + 1)

    def test_numeric_envelope_includes_boundaries(self):
        for temperature, humidity in ((-50, 0), (80, 100)):
            item = Telemetry("S01", 0, temperature, humidity, STAMP.isoformat())
            self.assertTrue(self.collector.on_message(self.topic, item.to_json()))
            self.collector = Collector()

    def test_bad_numbers_and_booleans_are_rejected(self):
        for name in ("temperature_c", "humidity_pct"):
            for value in (True, "22", None, float("nan"), float("inf"), 10 ** 1000):
                with self.subTest(name=name, value=repr(value)), self.assertRaises(ValueError):
                    self.collector.on_message(self.topic, payload(**{name: value}))
        for changes in ({"temperature_c": -50.01}, {"temperature_c": 80.01},
                        {"humidity_pct": -0.01}, {"humidity_pct": 100.01}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.collector.on_message(self.topic, payload(**changes))
        self.assertEqual(self.collector.messages, [])

    def test_sequence_requires_nonnegative_integer(self):
        for value in (-1, True, 1.0, "1", None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.collector.on_message(self.topic, payload(seq=value))

    def test_timestamp_requires_explicit_utc(self):
        for value in ("", "yesterday", "2026-10-21T12:00:00", "2026-10-21T12:00:00+02:00", None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.collector.on_message(self.topic, payload(timestamp=value))
        self.assertTrue(self.collector.on_message(self.topic, payload(timestamp="2026-10-21T12:00:00Z")))
        self.assertFalse(self.collector.on_message(self.topic, payload(timestamp=STAMP.isoformat())))

    def test_device_and_sensor_configuration_are_validated(self):
        for value in ("", "S/01", "s#", "x" * 65, True):
            with self.subTest(value=value), self.assertRaises(ValueError):
                SensorSimulator(value, self.broker)
        for options in ({"seed": True}, {"seed": 1.0}, {"clock": 1}):
            with self.subTest(options=options), self.assertRaises(ValueError):
                SensorSimulator("S01", self.broker, **options)
        with self.assertRaises(ValueError):
            SensorSimulator("S01", None)

    def test_bad_clock_does_not_advance_sequence_or_rng(self):
        for invalid in (None, datetime(2026, 10, 21), "2026-10-21"):
            self.sensor.clock = lambda: invalid
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                self.sensor.sample()
            self.assertEqual(self.sensor.seq, 0)
        self.sensor.clock = lambda: STAMP
        other = SensorSimulator("S01", self.broker, seed=7, clock=lambda: STAMP)
        self.assertEqual(self.sensor.sample(), other.sample())

    def test_broker_rejects_bad_topic_callback_and_duplicate_subscription(self):
        for topic in ("devices/+/telemetry", "devices/S01", "", None):
            with self.subTest(topic=topic), self.assertRaises(ValueError):
                self.broker.subscribe(topic, self.collector.on_message)
        with self.assertRaises(ValueError):
            self.broker.subscribe(self.topic, None)
        with self.assertRaises(ValueError):
            self.broker.subscribe(self.topic, self.collector.on_message)
        with self.assertRaises(ValueError):
            self.broker.online = "False"
        with self.assertRaises(ValueError):
            self.broker.publish(self.topic, "x" * 32_001)

    def test_offline_buffers_without_delivery(self):
        self.broker.online = False
        self.assertFalse(self.sensor.publish_once())
        self.assertEqual([item.seq for item in self.sensor.pending], [0])
        self.assertEqual(self.collector.messages, [])

    def test_reconnection_delivers_old_events_before_new_sample(self):
        self.broker.online = False
        self.sensor.publish_once()
        self.sensor.publish_once()
        self.broker.online = True
        self.assertTrue(self.sensor.publish_once())
        self.assertEqual([item["seq"] for item in self.collector.messages], [0, 1, 2])
        self.assertEqual(self.sensor.pending, [])

    def test_failed_flush_keeps_unsent_head(self):
        self.broker.online = False
        self.sensor.publish_once()
        with self.assertRaises(ConnectionError):
            self.sensor.flush_pending()
        self.assertEqual([item.seq for item in self.sensor.pending], [0])
        self.broker.online = True
        self.assertEqual(self.sensor.flush_pending(), 1)
        self.assertEqual(self.sensor.flush_pending(), 0)

    def test_schema_and_fields_are_exact(self):
        for text in (payload(schema="x"), payload(extra=1), '{"schema":"telemetry.v1"}'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.collector.on_message(self.topic, text)
        self.assertEqual(self.collector.messages, [])

    def test_malformed_json_duplicate_keys_and_wrong_root_are_rejected(self):
        for text in ("{", "[]", "null", "true", '{"seq":0,"seq":1}', "x" * 32_001):
            with self.subTest(text=text[:80]), self.assertRaises(ValueError):
                self.collector.on_message(self.topic, text)

    def test_topic_and_payload_device_must_match(self):
        with self.assertRaises(ValueError):
            self.collector.on_message(self.topic, payload(device_id="S02"))
        self.assertEqual(self.collector.messages, [])

    def test_identical_retry_is_acknowledged_without_duplicate(self):
        self.assertTrue(self.collector.on_message(self.topic, payload()))
        self.assertFalse(self.collector.on_message(self.topic, payload()))
        self.assertEqual(len(self.collector.messages), 1)

    def test_conflicting_duplicate_is_rejected_without_rounding_away_difference(self):
        self.collector.on_message(self.topic, payload(temperature_c=22.0001))
        with self.assertRaises(ValueError):
            self.collector.on_message(self.topic, payload(temperature_c=22.0002))
        self.assertEqual(self.collector.messages[0]["temperature_c"], 22.0001)

    def test_unseen_out_of_order_is_rejected_but_old_retry_is_allowed(self):
        self.collector.on_message(self.topic, payload(seq=1))
        self.collector.on_message(self.topic, payload(seq=3))
        self.assertFalse(self.collector.on_message(self.topic, payload(seq=1)))
        with self.assertRaises(ValueError):
            self.collector.on_message(self.topic, payload(seq=2))
        self.assertEqual([item["seq"] for item in self.collector.messages], [1, 3])

    def test_devices_have_independent_sequences(self):
        self.collector.on_message(self.topic, payload(seq=3))
        self.assertTrue(self.collector.on_message("devices/S02/telemetry", payload(device_id="S02", seq=0)))
        self.assertEqual(len(self.collector.messages), 2)

    def test_partial_callback_failure_can_retry_without_duplicate_at_collector(self):
        attempts = []
        def transient_failure(topic, text):
            attempts.append(text)
            if len(attempts) == 1:
                raise ConnectionError("Guasto simulato dopo il primo subscriber")
        self.broker.subscribe(self.topic, transient_failure)
        self.assertFalse(self.sensor.publish_once())
        self.assertEqual(len(self.collector.messages), 1)
        self.assertEqual(len(self.sensor.pending), 1)
        self.assertEqual(self.sensor.flush_pending(), 1)
        self.assertEqual(len(self.collector.messages), 1)
        self.assertEqual(len(attempts), 2)

    def test_returned_messages_cannot_corrupt_history_or_deduplication(self):
        self.collector.on_message(self.topic, payload())
        snapshot = self.collector.messages
        snapshot[0]["temperature_c"] = -50
        snapshot.clear()
        self.assertFalse(self.collector.on_message(self.topic, payload()))
        self.assertEqual(self.collector.messages[0]["temperature_c"], 22)

    def test_demo_is_three_ordered_events_and_no_persistent_transport(self):
        result = demo()
        self.assertEqual(result["offline_results"], [False, False])
        self.assertTrue(result["reconnected"])
        self.assertEqual(result["pending"], 0)
        self.assertFalse(result["duplicate_added"])
        self.assertEqual([item["seq"] for item in result["messages"]], [0, 1, 2])
        empty = VirtualBroker()
        empty.publish(self.topic, payload())  # Senza subscriber non c'è conferma di ricezione.


if __name__ == "__main__":
    unittest.main()
