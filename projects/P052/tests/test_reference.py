from pathlib import Path
from itertools import permutations
import sys, random
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from banker import safe_sequence
rng=random.Random(52)
for _ in range(400):
    n,m=rng.randint(0,4),rng.randint(1,3)
    available=[rng.randint(0,3) for _ in range(m)]
    allocation=[[rng.randint(0,3) for _ in range(m)] for _ in range(n)]
    maximum=[[x+rng.randint(0,4) for x in row] for row in allocation]
    def feasible(order):
        work=available[:]
        for i in order:
            if any(maximum[i][j]-allocation[i][j]>work[j] for j in range(m)):return False
            work=[work[j]+allocation[i][j] for j in range(m)]
        return True
    expected=any(feasible(order) for order in permutations(range(n)))
    before=repr((available,allocation,maximum))
    result=safe_sequence(available,allocation,maximum)
    assert (result is not None)==expected
    assert result is None or (set(result)==set(range(n)) and feasible(result))
    assert repr((available,allocation,maximum))==before
print('P052 PASS: 400 stati confrontati con tutte le permutazioni')
