import sys,pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]/"src"))
from scheduling import fcfs,sjf,round_robin

bursts=[5,3,1]
assert fcfs(bursts)==[0,5,8]
waits,order=sjf(bursts)
assert order==[2,1,0]
assert waits==[4,1,0]
rr,finish=round_robin(bursts,2)
assert finish==[9,8,5]
assert rr==[4,5,4]
print("P051: FCFS/SJF/RR scheduling PASS")
