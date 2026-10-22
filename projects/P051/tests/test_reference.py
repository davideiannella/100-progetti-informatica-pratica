from pathlib import Path
import sys, random
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from scheduling import *
rng=random.Random(51)
for _ in range(250):
    bursts=[rng.randint(1,9) for i in range(rng.randint(0,7))]
    assert fcfs(iter(bursts))==[sum(bursts[:i]) for i in range(len(bursts))]
    waits,order=sjf(bursts)
    assert order==sorted(range(len(bursts)),key=lambda i:(bursts[i],i))
    assert waits==[sum(bursts[j] for j in order[:order.index(i)]) for i in range(len(bursts))]
    quantum=rng.randint(1,5)
    remaining=bursts[:]; queue=list(range(len(bursts))); time=0; finish=[0]*len(bursts)
    while queue:
        index=queue.pop(0)
        for tick in range(min(quantum,remaining[index])):
            remaining[index]-=1;time+=1
        if remaining[index]:queue.append(index)
        else:finish[index]=time
    assert round_robin(iter(bursts),quantum)==([finish[i]-bursts[i] for i in range(len(bursts))],finish)
for invalid in [True,1.5,0,-1]:
    try:round_robin([1],invalid)
    except ValueError:pass
    else:raise AssertionError(invalid)
print('P051 PASS: 250 confronti con simulazione a tick indipendente')
