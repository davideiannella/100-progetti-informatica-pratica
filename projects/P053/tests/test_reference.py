from pathlib import Path
from collections import deque
import sys,random
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from page_replacement import fifo,lru,clock
rng=random.Random(53)
def clock_reference(refs,frames):
    q=deque();faults=0
    for page in refs:
        if any(p==page for p,bit in q):
            q=deque((p,1 if p==page else bit) for p,bit in q);continue
        faults+=1
        if len(q)==frames:
            while q[0][1]:
                p,bit=q.popleft();q.append((p,0))
            q.popleft()
        q.append((page,1))
    return faults
for _ in range(400):
    refs=[rng.randrange(7) for _ in range(rng.randrange(30))];frames=rng.randint(1,5)
    queue=[];f=0;recent=[];l=0
    for page in refs:
        if page not in queue:
            f+=1
            if len(queue)==frames:queue.pop(0)
            queue.append(page)
        if page in recent:recent.remove(page)
        else:
            l+=1
            if len(recent)==frames:recent.pop(0)
        recent.append(page)
    assert fifo(iter(refs),frames)==f
    assert lru(iter(refs),frames)==l
    assert clock(iter(refs),frames)==clock_reference(refs,frames)
print('P053 PASS: 400 confronti FIFO LRU e seconda opportunita')
