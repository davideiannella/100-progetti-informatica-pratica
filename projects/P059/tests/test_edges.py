from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from ha import *
a,b=Backend('A'),Backend('B');lb=LoadBalancer([a,b])
for i in range(10):lb.request('x')
assert (a.calls,b.calls)==(5,5)
a.healthy=b.healthy=False
try:lb.request('x')
except RuntimeError:pass
else:raise AssertionError('all down')
c=Cache();calls=[]
def fail():calls.append(1);raise RuntimeError('loader')
for _ in range(2):
    try:c.get_or_set('x',fail)
    except RuntimeError:pass
assert len(calls)==2 and 'x' not in c.data
print('P059 PASS: bilanciamento, tutti down e errore loader non memorizzato')
