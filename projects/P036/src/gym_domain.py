from dataclasses import dataclass, field
from datetime import date
from typing import Dict, Set

@dataclass(frozen=True)
class Customer:
    customer_id: str
    name: str

@dataclass(frozen=True)
class Instructor:
    instructor_id: str
    name: str

@dataclass
class Subscription:
    customer_id: str
    start_date: date
    end_date: date

    def is_valid_on(self, day: date) -> bool:
        return self.start_date <= day <= self.end_date

@dataclass
class Course:
    course_id: str
    name: str
    instructor_id: str
    capacity: int
    bookings: Set[str] = field(default_factory=set)

    def book(self, customer_id: str) -> None:
        if customer_id in self.bookings:
            raise ValueError('Cliente già prenotato')
        if len(self.bookings) >= self.capacity:
            raise ValueError('Corso al completo')
        self.bookings.add(customer_id)

    def cancel(self, customer_id: str) -> None:
        if customer_id not in self.bookings:
            raise ValueError('Prenotazione inesistente')
        self.bookings.remove(customer_id)

class GymService:

    def __init__(self):
        self.customers: Dict[str, Customer] = {}
        self.instructors: Dict[str, Instructor] = {}
        self.subscriptions: Dict[str, Subscription] = {}
        self.courses: Dict[str, Course] = {}

    def register_customer(self, customer: Customer) -> None:
        if customer.customer_id in self.customers:
            raise ValueError('Cliente già presente')
        self.customers[customer.customer_id] = customer

    def register_instructor(self, instructor: Instructor) -> None:
        if instructor.instructor_id in self.instructors:
            raise ValueError('Istruttore già presente')
        self.instructors[instructor.instructor_id] = instructor

    def activate_subscription(self, subscription: Subscription) -> None:
        if subscription.customer_id not in self.customers:
            raise ValueError('Cliente inesistente')
        if subscription.end_date < subscription.start_date:
            raise ValueError('Intervallo abbonamento non valido')
        self.subscriptions[subscription.customer_id] = subscription

    def add_course(self, course: Course) -> None:
        if course.instructor_id not in self.instructors:
            raise ValueError('Istruttore inesistente')
        if type(course.capacity) is not int or course.capacity <= 0:
            raise ValueError('Capienza non valida')
        if course.course_id in self.courses:
            raise ValueError('Corso già presente')
        self.courses[course.course_id] = course

    def can_enter(self, customer_id: str, day: date) -> bool:
        if customer_id not in self.customers:
            return False
        subscription = self.subscriptions.get(customer_id)
        return bool(subscription and subscription.is_valid_on(day))

    def book_course(self, customer_id: str, course_id: str, day: date) -> None:
        if not self.can_enter(customer_id, day):
            raise PermissionError('Abbonamento non valido')
        if course_id not in self.courses:
            raise ValueError('Corso inesistente')
        self.courses[course_id].book(customer_id)

    def cancel_booking(self, customer_id: str, course_id: str) -> None:
        if course_id not in self.courses:
            raise ValueError('Corso inesistente')
        self.courses[course_id].cancel(customer_id)
