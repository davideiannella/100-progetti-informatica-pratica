import unittest
from datetime import date
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))
from gym_domain import Customer, Instructor, Subscription, Course, GymService

class GymDomainTest(unittest.TestCase):
    def setUp(self):
        self.service = GymService()
        self.service.register_customer(Customer('C1','Anna'))
        self.service.register_customer(Customer('C2','Luca'))
        self.service.register_instructor(Instructor('I1','Marta'))
        self.service.activate_subscription(Subscription('C1', date(2026,10,1), date(2026,10,31)))
        self.service.add_course(Course('K1','Functional Training','I1',1))
    def test_access_with_valid_subscription(self): self.assertTrue(self.service.can_enter('C1', date(2026,10,15)))
    def test_access_without_subscription(self): self.assertFalse(self.service.can_enter('C2', date(2026,10,15)))
    def test_access_after_expiry(self): self.assertFalse(self.service.can_enter('C1', date(2026,11,1)))
    def test_booking_requires_valid_subscription(self):
        with self.assertRaises(PermissionError): self.service.book_course('C2','K1',date(2026,10,15))
    def test_booking_and_capacity(self):
        self.service.book_course('C1','K1',date(2026,10,15))
        self.service.activate_subscription(Subscription('C2', date(2026,10,1), date(2026,10,31)))
        with self.assertRaises(ValueError): self.service.book_course('C2','K1',date(2026,10,15))
    def test_duplicate_booking_rejected(self):
        self.service.book_course('C1','K1',date(2026,10,15))
        with self.assertRaises(ValueError): self.service.book_course('C1','K1',date(2026,10,15))
    def test_cancel_booking(self):
        self.service.book_course('C1','K1',date(2026,10,15))
        self.service.cancel_booking('C1','K1')
        self.assertNotIn('C1', self.service.courses['K1'].bookings)
if __name__ == '__main__': unittest.main()
