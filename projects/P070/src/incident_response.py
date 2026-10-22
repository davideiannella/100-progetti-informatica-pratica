"""Tabletop IR e verifica SHA-256 di un ripristino in memoria, senza malware."""
from collections.abc import Mapping
from dataclasses import dataclass
import hashlib
import hmac
import re

STATES = ("DETECTED", "CONTAINED", "ERADICATED", "RECOVERED", "LESSONS_LEARNED")


def _text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label}: testo non vuoto")
    return value.strip()


@dataclass(frozen=True)
class RestoreEvidence:
    """Esito locale, non attestazione firmata né prova di assenza di malware."""
    sha256: str
    size: int

    def __post_init__(self):
        if (not isinstance(self.sha256, str) or re.fullmatch(r"[0-9a-f]{64}", self.sha256) is None
                or type(self.size) is not int or self.size < 0):
            raise ValueError("evidenza non valida")


def restore_verified(backup, trusted_sha256):
    """Confronta byte con un digest fidato separato e restituisce dati + evidenza."""
    if type(backup) is not bytes:
        raise ValueError("backup: bytes richiesti")
    if not isinstance(trusted_sha256, str) or re.fullmatch(r"[0-9a-fA-F]{64}", trusted_sha256) is None:
        raise ValueError("digest SHA-256 non valido")
    actual = hashlib.sha256(backup).hexdigest()
    if not hmac.compare_digest(actual, trusted_sha256.lower()):
        raise ValueError("integrità del backup non verificata")
    return backup, RestoreEvidence(actual, len(backup))


class Incident:
    def __init__(self):
        self._i = 0
        self._actions = []

    @property
    def state(self):
        return STATES[self._i]

    @property
    def actions(self):
        return tuple(self._actions)

    def advance(self, action, *, recovery_evidence=None):
        """Una sola transizione; Recover richiede evidenza del laboratorio."""
        action = _text(action, "action")
        if self._i == len(STATES) - 1:
            raise ValueError("incidente già concluso")
        if self.state == "ERADICATED":
            if not isinstance(recovery_evidence, RestoreEvidence):
                raise ValueError("RECOVERED richiede evidenza del ripristino")
            if (re.fullmatch(r"[0-9a-f]{64}", recovery_evidence.sha256 or "") is None
                    or type(recovery_evidence.size) is not int or recovery_evidence.size < 0):
                raise ValueError("evidenza non valida")
        elif recovery_evidence is not None:
            raise ValueError("evidenza ammessa solo nella transizione di recupero")
        before = self.state
        after = STATES[self._i + 1]
        self._actions.append((before, after, action, recovery_evidence))
        self._i += 1
        return self.state


def recovery_priority(assets):
    """1 = massima criticità; poi minore downtime; parità mantiene ordine input."""
    records = list(assets)
    names = set()
    for asset in records:
        if not isinstance(asset, Mapping):
            raise ValueError("asset: mapping richiesto")
        name = _text(asset.get("name"), "name")
        if name in names:
            raise ValueError("nome asset duplicato")
        names.add(name)
        value = asset.get("criticality")
        if type(value) is not int or not 1 <= value <= 5:
            raise ValueError("criticality: intero 1..5")
        value = asset.get("max_downtime_min")
        if type(value) is not int or value < 0:
            raise ValueError("max_downtime_min: intero non negativo")
    return sorted((dict(a) for a in records), key=lambda x: (x["criticality"], x["max_downtime_min"]))


def main():
    backup = b"ordine=42\n"
    restored, evidence = restore_verified(backup, hashlib.sha256(backup).hexdigest())
    incident = Incident()
    print(incident.state)
    print(incident.advance("isolare nel tabletop"))
    print(incident.advance("documentare rimozione della causa"))
    print(incident.advance("ripristino provato", recovery_evidence=evidence))
    print(incident.advance("registrare miglioramenti"))
    print("Byte ripristinati:", len(restored))
    try:
        restore_verified(backup + b"alterazione", evidence.sha256)
    except ValueError:
        print("Backup alterato: RIFIUTATO")


if __name__ == "__main__":
    main()
