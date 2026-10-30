import sys,pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]/"src"))
from wifi_plan import Zone,plan,non_overlapping_24ghz

assert Zone("x",70,25).aps_needed()==3
assert Zone("x",25,25).aps_needed()==1
assert Zone("x",26,25).aps_needed()==2
assert plan()=={"ricevimento":2,"corsie A-B":3,"corsie C-D":3,"spedizioni":2}
assert non_overlapping_24ghz()==[1,6,11]
for invalid in [0,-1,True,1.2,float("nan"),float("inf"),"25",None]:
    for devices,target in [(invalid,25),(25,invalid)]:
        try: Zone("x",devices,target).aps_needed()
        except ValueError: pass
        else: raise AssertionError((devices,target))
print("P050: Wi-Fi capacity planning model PASS")
