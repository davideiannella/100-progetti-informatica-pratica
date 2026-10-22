import sys,pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]/"src"))
from wifi_plan import Zone,plan,non_overlapping_24ghz

assert Zone("x",70,25).aps_needed()==3
assert plan()["ricevimento"]==2
assert non_overlapping_24ghz()==[1,6,11]
bad=False
try: Zone("x",0,10).aps_needed()
except ValueError: bad=True
assert bad
print("P050: Wi-Fi capacity planning model PASS")
