from collections import deque

def validated(bursts):
    values = list(bursts)
    if any(type(x) is not int or x <= 0 for x in values):
        raise ValueError("burst interi positivi")
    return values

def fcfs(bursts):
    bursts = validated(bursts)
    if any(x<=0 for x in bursts): raise ValueError("burst")
    t=0; waits=[]
    for b in bursts:
        waits.append(t); t+=b
    return waits

def sjf(bursts):
    bursts = validated(bursts)
    if any(x<=0 for x in bursts): raise ValueError("burst")
    order=sorted(range(len(bursts)), key=lambda i:(bursts[i],i))
    t=0; waits=[0]*len(bursts)
    for i in order:
        waits[i]=t; t+=bursts[i]
    return waits,order

def round_robin(bursts, quantum):
    bursts = validated(bursts)
    if type(quantum) is not int:
        raise ValueError("quantum intero")
    if quantum<=0 or any(x<=0 for x in bursts): raise ValueError("input")
    rem=list(bursts); q=deque(range(len(rem))); t=0; finish=[0]*len(rem)
    while q:
        i=q.popleft()
        used=min(quantum,rem[i])
        t+=used; rem[i]-=used
        if rem[i]: q.append(i)
        else: finish[i]=t
    waits=[finish[i]-bursts[i] for i in range(len(bursts))]
    return waits,finish
