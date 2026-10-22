import sys,pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]/"src"))
from banker import safe_sequence

available=[3,3,2]
allocation=[[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
maximum=[[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
seq=safe_sequence(available,allocation,maximum)
assert seq is not None and len(seq)==5

unsafe=safe_sequence([0], [[1],[1]], [[2],[2]])
assert unsafe is None
print("P052: Banker's safety check PASS; safe sequence =",seq)
