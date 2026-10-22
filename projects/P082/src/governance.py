"""Checklist didattica: nessuna classificazione normativa automatica."""

from collections.abc import Mapping
import json

CONTROLS = {
    "data": ("provenance", "quality", "privacy"),
    "model": ("evaluation", "robustness", "limitations"),
    "human": ("oversight", "appeal"),
    "operations": ("logging", "monitoring", "incident_response"),
}
CONTROL_NAMES = frozenset(name for names in CONTROLS.values() for name in names)


def governance_check(system):
    if not isinstance(system, Mapping):
        raise ValueError("I controlli devono essere una mappa nome-bool.")
    if set(system) - CONTROL_NAMES:
        raise ValueError("Controllo sconosciuto: verificare i nomi della checklist.")
    if any(type(value) is not bool for value in system.values()):
        raise ValueError("Ogni controllo presente deve valere True oppure False.")
    missing = [f"{area}:{control}"
               for area, controls in CONTROLS.items()
               for control in controls if system.get(control, False) is not True]
    return {"complete": not missing, "missing": missing,
            "satisfied": len(CONTROL_NAMES) - len(missing),
            "total": len(CONTROL_NAMES)}


def _required(value, name):
    if not isinstance(value, str) or not value.strip() or len(value) > 2000:
        raise ValueError(f"{name}: serve un testo non vuoto di massimo 2000 caratteri.")
    return value.strip()


def decision_record(name, purpose, owner, limitations):
    return {key: _required(value, key) for key, value in (
        ("name", name), ("purpose", purpose),
        ("owner", owner), ("limitations", limitations))}


def demo():
    controls = {name: True for names in CONTROLS.values() for name in names}
    controls["monitoring"] = False
    controls["incident_response"] = False
    return {
        "record": decision_record("TicketAI", "Suggerire una coda per ticket sintetici",
                                  "Responsabile del servizio",
                                  "Il suggerimento richiede revisione umana; nessun invio automatico"),
        "checklist": governance_check(controls),
        "scope": "Completezza dei flag dichiarati, non conformità legale o efficacia dei controlli.",
    }


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2))
