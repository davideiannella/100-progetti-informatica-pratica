import sys,pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]/"src"))
from ha import Backend,LoadBalancer,Cache

a,b=Backend("A"),Backend("B"); lb=LoadBalancer([a,b])
assert lb.request("x").startswith("A:")
assert lb.request("x").startswith("B:")
b.healthy=False
assert lb.request("x").startswith("A:")
c=Cache()
first=c.get_or_set("home",lambda:lb.request("home"))
calls=a.calls+b.calls
second=c.get_or_set("home",lambda:lb.request("home"))
assert first==second and a.calls+b.calls==calls
print("P059: load balancing + failover + cache model PASS")
