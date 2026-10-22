"""Registro STRIDE e matrice ordinale didattica; nessun risk score scientifico."""
from types import MappingProxyType

STRIDE = MappingProxyType({
    "S": "Spoofing", "T": "Tampering", "R": "Repudiation",
    "I": "Information Disclosure", "D": "Denial of Service", "E": "Elevation of Privilege",
})


def risk(likelihood, impact):
    if any(type(value) is not int or not 1 <= value <= 5 for value in (likelihood, impact)):
        raise ValueError("likelihood e impact: interi 1..5; bool e float esclusi")
    score = likelihood * impact
    band = "low" if score <= 5 else "medium" if score <= 12 else "high"
    return score, band


def _text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label}: testo non vuoto")
    return value.strip()


def make_threat(component, category, likelihood, impact, mitigation, *, rationale=None):
    component = _text(component, "component")
    mitigation = _text(mitigation, "mitigation")
    if not isinstance(category, str) or category not in STRIDE:
        raise ValueError("category: una lettera maiuscola STRIDE")
    if rationale is not None:
        rationale = _text(rationale, "rationale")
    score, band = risk(likelihood, impact)
    return {"component": component, "category": STRIDE[category], "likelihood": likelihood,
            "impact": impact, "score": score, "band": band, "mitigation": mitigation,
            "rationale": rationale}


def main():
    threat = make_threat("login", "S", 4, 4, "MFA + rate limit",
                         rationale="Credenziali riutilizzate; accesso agli ordini")
    print("Categoria:", threat["category"])
    print("Rischio iniziale:", threat["score"], threat["band"])
    print("Ipotesi dopo mitigazione:", *risk(2, 4))
    try:
        risk(True, 4)
    except ValueError:
        print("Scala booleana: RIFIUTATA")


if __name__ == "__main__":
    main()
