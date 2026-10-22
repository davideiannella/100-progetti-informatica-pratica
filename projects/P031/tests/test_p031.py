import sys,pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]/"src"))
from telemetry_model import Telemetry
from datetime import datetime
d=Telemetry("sensor-01",datetime(2026,10,1),22.4,51).to_document()
assert d["metrics"]["humidity"]==51
bad=False
try: Telemetry("x",datetime.now(),20,150).to_document()
except ValueError: bad=True
assert bad
print("P031: document model PASS; MongoDB script STATIC QA")
