from dataclasses import dataclass

@dataclass(frozen=True)
class Contact:
    name: str
    email: str
    phone: str = ''

class AddressBook:

    def __init__(self):
        self._by_email = {}

    def add(self, c):
        if not c.name.strip():
            raise ValueError('Nome vuoto')
        key = c.email.strip().lower()
        if not key or '@' not in key:
            raise ValueError('Email non valida')
        if key in self._by_email:
            raise ValueError('Duplicato')
        self._by_email[key] = Contact(c.name.strip(), key, c.phone.strip())

    def remove(self, email):
        return self._by_email.pop(email.strip().lower(), None)

    def search(self, text):
        q = text.casefold()
        return sorted([c for c in self._by_email.values() if q in c.name.casefold()], key=lambda c: c.name.casefold())

    def all_sorted(self):
        return sorted(self._by_email.values(), key=lambda c: c.name.casefold())
