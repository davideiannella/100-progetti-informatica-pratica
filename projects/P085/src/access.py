"""Autorizzazione di badge virtuali: non autentica il loro possessore."""

from dataclasses import dataclass, replace
import json
import re
from types import MappingProxyType

PERMISSIONS = MappingProxyType({
    "employee": frozenset({"office"}),
    "admin": frozenset({"office", "server"}),
    "guest": frozenset({"lobby"}),
})
ZONES = frozenset(zone for zones in PERMISSIONS.values() for zone in zones)


def _text(value, name, maximum=120):
    if not isinstance(value, str) or not value.strip() or len(value) > maximum:
        raise ValueError(f"{name}: serve un testo non vuoto di massimo {maximum} caratteri.")
    return value.strip()


def _badge_id(value):
    value = _text(value, "badge_id", 64)
    if re.fullmatch(r"[A-Za-z0-9_-]+", value) is None:
        raise ValueError("badge_id: usare lettere ASCII, cifre, _ o -.")
    return value


@dataclass(frozen=True)
class Badge:
    id: str
    owner: str
    role: str
    active: bool = True

    def __post_init__(self):
        object.__setattr__(self, "id", _badge_id(self.id))
        object.__setattr__(self, "owner", _text(self.owner, "owner"))
        role = _text(self.role, "role", 32)
        if role not in PERMISSIONS or type(self.active) is not bool:
            raise ValueError("Ruolo sconosciuto o active diverso da un booleano.")
        object.__setattr__(self, "role", role)


class AccessControl:
    def __init__(self):
        self._badges = {}
        self._audit = []

    @property
    def badges(self):
        return MappingProxyType(self._badges)

    @property
    def permissions(self):
        return PERMISSIONS

    @property
    def audit(self):
        return [record.copy() for record in self._audit]

    def register(self, badge):
        if not isinstance(badge, Badge):
            raise ValueError("Serve un Badge validato.")
        if badge.id in self._badges:
            raise ValueError("Identificativo già registrato: nessuna sovrascrittura.")
        self._badges[badge.id] = badge

    def revoke(self, badge_id):
        badge_id = _badge_id(badge_id)
        if badge_id not in self._badges:
            raise ValueError("Badge sconosciuto.")
        badge = self._badges[badge_id]
        self._badges[badge_id] = replace(badge, active=False)
        return badge.active

    def authorize(self, badge_id, zone, ts):
        badge_id = _badge_id(badge_id)
        zone = _text(zone, "zone", 64)
        if type(ts) is not int or ts < 0:
            raise ValueError("ts deve essere un intero non negativo: secondi Unix forniti dal chiamante.")
        badge = self._badges.get(badge_id)
        if badge is None:
            reason = "unknown_badge"
        elif not badge.active:
            reason = "inactive_badge"
        elif zone not in ZONES:
            reason = "unknown_zone"
        elif zone not in PERMISSIONS[badge.role]:
            reason = "role_not_permitted"
        else:
            reason = "granted"
        allowed = reason == "granted"
        self._audit.append({"badge": badge_id, "zone": zone, "ts": ts,
                            "allowed": allowed, "reason": reason})
        return allowed


def demo():
    system = AccessControl()
    for badge in (Badge("B1", "Anna", "employee"), Badge("B2", "Luca", "admin"),
                  Badge("B3", "Sara", "guest")):
        system.register(badge)
    system.revoke("B3")
    for index, (badge_id, zone) in enumerate((
        ("B1", "office"), ("B1", "server"), ("B2", "server"),
        ("B3", "lobby"), ("NO", "office"), ("B1", "warehouse"))):
        system.authorize(badge_id, zone, 1_700_000_000 + index)
    records = system.audit
    return {"allowed": sum(record["allowed"] for record in records),
            "denied": sum(not record["allowed"] for record in records), "audit": records}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2))
