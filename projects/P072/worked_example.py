from pathlib import Path
import json, sys
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from mini_soc import Correlator, parse, normalize, process_lines
lines=[f"ts={ts} event=login_failed src_ip=203.0.113.9 user=alice" for ts in (0,5,10)]
lines += ["ts=11 event=admin_login src_ip=198.51.100.2 user=alice country=US","ts=12 event=admin_login src_ip=198.51.100.2 user=alice","ts=13 event=login_failed event=admin_login"]
results=list(process_lines(lines,Correlator(3,10)))
quoted='ts=14 event=login_success src_ip=2001:0db8:0:0:0:0:0:1 user="Alice B" note=a=b'
normalized=normalize(parse(quoted))
exercise=["ts=0 event=login_failed src_ip=203.0.113.1 user=alice","ts=5 event=login_success src_ip=203.0.113.1 user=alice","ts=10 event=login_failed src_ip=203.0.113.1 user=alice","ts=21 event=login_failed src_ip=203.0.113.1 user=alice"]
exercise_result=list(process_lines(exercise,Correlator(2,10)))
assert [[a["rule"] for a in r["alerts"]] for r in results]==[[],[],["repeated_login_failures"],["admin_login_unusual_country"],["missing_country"],["invalid_event"]]
assert normalized["src_ip"]=="2001:db8::1" and normalized["user"]=="Alice B"
print(json.dumps({"threshold":3,"window":10,"allowed_countries":["IT","SM","VA"],"input_lines":lines,"results":results,"quoted_input":quoted,"normalized":normalized,"exercise_lines":exercise,"exercise_results":exercise_result},ensure_ascii=False,indent=2))
