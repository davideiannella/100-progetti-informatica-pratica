import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from parking import price, Tariff, ParkingLot
for minutes, expected in [(0,0),(1,200),(59,200),(60,200),(61,350),(120,350),(121,500)]:
    assert price(minutes)==expected
for value in [-1,1.2,True]:
    try: price(value)
    except ValueError: pass
    else: raise AssertionError(value)
p=ParkingLot(1)
assert not p.enter(' ') and p.enter('A') and not p.enter('A')
assert not p.enter('B') and p.exit('A') and p.enter('B')
assert not p.exit('A')
print('P043 casi limite PASS')
