"""Autenticazione HMAC e aggiornamenti simulati esclusivamente in memoria."""
import copy
import hashlib
import hmac
import json
import re
import secrets

ALGORITHM = "HMAC-SHA256"
MAX_VERSION = 2**31 - 1


def _version(value):
    if type(value) is not int or not 1 <= value <= MAX_VERSION:
        raise ValueError("Versione intera fra 1 e 2**31-1 richiesta.")
    return value


def _secret(value):
    if type(value) is not bytes or len(value) < 32:
        raise ValueError("Chiave condivisa bytes di almeno 32 byte richiesta.")
    return value


def _payload(value):
    if type(value) is not bytes or not value:
        raise ValueError("Artifact non vuoto di tipo bytes richiesto.")
    return value


def _raw(body):
    return json.dumps(body, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True, allow_nan=False).encode("ascii")


def manifest(version, payload, secret):
    body = {"version": _version(version), "algorithm": ALGORITHM,
            "sha256": hashlib.sha256(_payload(payload)).hexdigest()}
    return body | {"mac": hmac.new(_secret(secret), _raw(body), hashlib.sha256).hexdigest()}


def verify(m, payload, secret, current_version):
    """Un manifest malformato è rifiutato; non si legge alcun percorso/file."""
    try:
        _version(current_version)
        _secret(secret)
        _payload(payload)
        if type(m) is not dict or set(m) != {"version", "algorithm", "sha256", "mac"}:
            return False
        _version(m["version"])
        if m["algorithm"] != ALGORITHM:
            return False
        for field in ("sha256", "mac"):
            if type(m[field]) is not str or not re.fullmatch(r"[0-9a-f]{64}", m[field]):
                return False
        body = {field: m[field] for field in ("version", "algorithm", "sha256")}
        expected = hmac.new(secret, _raw(body), hashlib.sha256).hexdigest()
        return (hmac.compare_digest(expected, m["mac"])
                and hmac.compare_digest(hashlib.sha256(payload).hexdigest(), m["sha256"])
                and m["version"] > current_version)
    except (ValueError, TypeError, OverflowError):
        return False


class Device:
    def __init__(self, id, version=1, payload=b"firmware-v1"):
        if type(id) is not str or not id.strip() or len(id) > 64:
            raise ValueError("Identificativo dispositivo richiesto, massimo 64 caratteri.")
        self.id = id
        self.version = _version(version)
        self.payload = _payload(payload)
        self.highest_version = version
        self.previous = None
        self._audit = []

    @property
    def audit(self):
        return copy.deepcopy(self._audit)

    def apply(self, m, payload, secret, healthy=True):
        if type(healthy) is not bool:
            raise ValueError("healthy è un esito booleano simulato.")
        if not verify(m, payload, secret, self.highest_version):
            self._audit.append({"action": "reject", "version": self.version})
            return False
        before = (self.version, self.payload, self.previous)
        self.previous = (self.version, self.payload)
        self.version, self.payload = m["version"], payload
        if not healthy:
            self.version, self.payload, self.previous = before
            self._audit.append({"action": "health_failed_restored", "version": self.version})
            return False
        self.highest_version = self.version
        self._audit.append({"action": "applied", "version": self.version})
        return True

    def rollback(self):
        if self.previous is None:
            return False
        self.version, self.payload = self.previous
        self.previous = None
        # Il massimo accettato non scende: il vecchio manifest non è riutilizzabile.
        self._audit.append({"action": "rollback", "version": self.version})
        return True


def demo():
    secret = secrets.token_bytes(32)  # Mai stampato o salvato; non è una chiave pubblica.
    payload = b"firmware-v2"
    m = manifest(2, payload, secret)
    device = Device("dev-demo")
    applied = device.apply(m, payload, secret)
    version_after_apply = device.version
    rolled_back = device.rollback()
    replay = device.apply(m, payload, secret)
    candidate = manifest(3, b"firmware-v3", secret)
    unhealthy = device.apply(candidate, b"firmware-v3", secret, healthy=False)
    return {"simulation_only": True, "algorithm": ALGORITHM,
            "artifact_sha256": m["sha256"], "applied": applied,
            "version_after_apply": version_after_apply, "rollback": rolled_back,
            "replay_accepted": replay, "unhealthy_accepted": unhealthy,
            "final_version": device.version, "highest_version": device.highest_version,
            "audit": device.audit}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2))
