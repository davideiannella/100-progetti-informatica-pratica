from dataclasses import dataclass

@dataclass(frozen=True)
class Tariff:
    first_hour_cents: int = 200
    next_hour_cents: int = 150

def price(minutes: int, t: Tariff = Tariff()) -> int:
    if type(minutes) is not int or minutes < 0:
        raise ValueError("minutes interi non negativi")
    if any(type(v) is not int or v < 0 for v in (t.first_hour_cents, t.next_hour_cents)):
        raise ValueError("tariffa")
    if minutes == 0:
        return 0
    hours = (minutes + 59) // 60
    return t.first_hour_cents + (hours - 1) * t.next_hour_cents

class ParkingLot:
    def __init__(self, capacity: int):
        if type(capacity) is not int or capacity <= 0:
            raise ValueError("capacity intera positiva")
        self.capacity = capacity
        self.plates = set()

    def enter(self, plate: str):
        if not isinstance(plate, str) or not plate.strip():
            return False
        if plate in self.plates or len(self.plates) >= self.capacity:
            return False
        self.plates.add(plate)
        return True

    def exit(self, plate: str):
        if plate not in self.plates:
            return False
        self.plates.remove(plate)
        return True
