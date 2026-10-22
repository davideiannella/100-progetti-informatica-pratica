import sys,pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]/"src"))
from page_replacement import fifo,lru,clock

refs=[7,0,1,2,0,3,0,4,2,3,0,3,2]
assert fifo(refs,3)==10
assert lru(refs,3)==9
assert clock(refs,3) >= 1
assert lru([1,1,1],1)==1
print("P053: FIFO/LRU/Clock page replacement PASS")
