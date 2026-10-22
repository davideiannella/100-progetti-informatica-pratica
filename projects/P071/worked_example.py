from pathlib import Path
import json, sys
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from itertools import product
from collections import Counter
from threat_model import STRIDE, make_threat, risk
threat=make_threat("login","S",4,4,"MFA + rate limit",rationale="Credenziali riutilizzate; accesso agli ordini")
matrix=[{"likelihood":a,"impact":b,"score":risk(a,b)[0],"band":risk(a,b)[1]} for a,b in product(range(1,6),repeat=2)]
residual=[]
for a,b in product(range(1,6),repeat=2):
    for ar,br in product(range(1,a+1),range(1,b+1)):
        assert risk(ar,br)[0]<=risk(a,b)[0]
        residual.append({"before":[a,b],"after":[ar,br],"score":risk(ar,br)[0],"band":risk(ar,br)[1]})
try:
    risk(True,4)
except ValueError as exc:
    invalid={"status":"RIFIUTATO","reason":str(exc)}
else:
    raise AssertionError("bool accettato")
result={"threat":threat,"mitigation_hypothesis":{"likelihood":2,"impact":4,"score":risk(2,4)[0],"band":risk(2,4)[1]},"categories":dict(STRIDE),"matrix":matrix,"band_counts":dict(Counter(r["band"] for r in matrix)),"residual_combinations":len(residual),"exercise_initial":list(risk(3,5)),"exercise_residual":list(risk(2,5)),"invalid_scale":invalid}
assert len(matrix)==25 and len(residual)==225
print(json.dumps(result,ensure_ascii=False,indent=2))
