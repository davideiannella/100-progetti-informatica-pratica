from pathlib import Path
import json, sys
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
import hashlib
from incident_response import Incident, restore_verified, recovery_priority
backup=b"ordine=42\n"
trusted=hashlib.sha256(backup).hexdigest()
restored,evidence=restore_verified(backup,trusted)
incident=Incident(); states=[incident.state]
states.append(incident.advance("isolare nel tabletop"))
states.append(incident.advance("documentare rimozione della causa"))
states.append(incident.advance("ripristino provato",recovery_evidence=evidence))
states.append(incident.advance("registrare miglioramenti"))
try:
    restore_verified(backup+b"alterazione",trusted)
except ValueError as exc:
    corruption={"status":"RIFIUTATO","reason":str(exc)}
else:
    raise AssertionError("alterazione accettata")
assets=[{"name":"ordini","criticality":1,"max_downtime_min":30},{"name":"pagamenti","criticality":1,"max_downtime_min":10},{"name":"catalogo","criticality":2,"max_downtime_min":5}]
exercise=[{"name":"checkout","criticality":1,"max_downtime_min":20},{"name":"backup","criticality":1,"max_downtime_min":5},{"name":"analytics","criticality":3,"max_downtime_min":0}]
result={"backup_hex":backup.hex(),"bytes_restored":len(restored),"trusted_sha256":trusted,"evidence":{"sha256":evidence.sha256,"size":evidence.size},"states":states,"actions":[{"from":a,"to":b,"action":c,"has_evidence":d is not None} for a,b,c,d in incident.actions],"alteration":corruption,"assets":assets,"priority":[a["name"] for a in recovery_priority(assets)],"exercise_priority":[a["name"] for a in recovery_priority(exercise)]}
assert result["priority"]==["pagamenti","ordini","catalogo"] and result["exercise_priority"]==["backup","checkout","analytics"]
print(json.dumps(result,ensure_ascii=False,indent=2))
