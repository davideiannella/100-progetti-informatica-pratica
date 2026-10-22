from pathlib import Path
import json, sys
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from itertools import product
from network_defense import firewall, FailedLoginDetector
zones = ("internet", "dmz", "app", "db", "guest", "management")
services = ("https", "postgres", "ssh", "unknown")
policy = [{"src": a, "dst": b, "service": s, "allowed": firewall(a,b,s)} for a,b,s in product(zones,zones,services)]
detector = FailedLoginDetector(3,10)
timeline = []
for ts in (0,5,10,21):
    alert = detector.record("203.0.113.1",ts)
    timeline.append({"ts": ts, "alert": alert, "retained": list(detector.events["203.0.113.1"])})
exercise = FailedLoginDetector(3,10)
exercise_values = [exercise.record("203.0.113.2",ts) for ts in (20,25,30,31)]
assert [r["alert"] for r in timeline] == [False,False,True,False]
assert sum(r["allowed"] for r in policy) == 3
print(json.dumps({"policy_matrix": policy, "allowed_count":3, "denied_count":141, "threshold":3,"window":10,"timeline":timeline,"exercise_ts":[20,25,30,31],"exercise_alerts":exercise_values},ensure_ascii=False,indent=2))
