import unittest
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from queue_manager import QueueManager


class QueueManagerTests(unittest.TestCase):
    def test_empty_queue_returns_none(self):
        q = QueueManager()
        self.assertIsNone(q.call_next(0))

    def test_fifo_with_same_priority(self):
        q = QueueManager()
        a = q.issue_ticket(2, 0)
        b = q.issue_ticket(2, 1)
        self.assertEqual(q.call_next(10).ticket.ticket_id, a.ticket_id)
        self.assertEqual(q.call_next(11).ticket.ticket_id, b.ticket_id)

    def test_priority_before_arrival_order(self):
        q = QueueManager()
        normal = q.issue_ticket(3, 0)
        high = q.issue_ticket(1, 1)
        self.assertEqual(q.call_next(5).ticket.ticket_id, high.ticket_id)
        self.assertEqual(q.call_next(6).ticket.ticket_id, normal.ticket_id)

    def test_cancel_ticket(self):
        q = QueueManager()
        a = q.issue_ticket(1, 0)
        b = q.issue_ticket(2, 1)
        self.assertTrue(q.cancel_ticket(a.ticket_id))
        self.assertFalse(q.cancel_ticket(a.ticket_id))
        self.assertEqual(q.call_next(5).ticket.ticket_id, b.ticket_id)

    def test_invalid_priority(self):
        q = QueueManager()
        with self.assertRaises(ValueError):
            q.issue_ticket(9, 0)

    def test_statistics(self):
        q = QueueManager()
        q.issue_ticket(1, 0)
        q.issue_ticket(2, 2)
        q.call_next(4)   # attesa 4
        q.call_next(8)   # attesa 6
        stats = q.statistics()
        self.assertEqual(stats["served_count"], 2)
        self.assertAlmostEqual(stats["average_wait"], 5.0)
        self.assertAlmostEqual(stats["max_wait"], 6.0)

    def test_waiting_count(self):
        q = QueueManager()
        a = q.issue_ticket(1, 0)
        q.issue_ticket(3, 1)
        self.assertEqual(q.waiting_count, 2)
        q.cancel_ticket(a.ticket_id)
        self.assertEqual(q.waiting_count, 1)


if __name__ == "__main__":
    unittest.main()
