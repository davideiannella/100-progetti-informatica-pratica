import sys,pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]/'src'))
from parking import price,ParkingLot
assert price(0)==0 and price(1)==200 and price(60)==200 and price(61)==350
bad=False
try: price(-1)
except ValueError: bad=True
assert bad
p=ParkingLot(1);assert p.enter('AA111AA');assert not p.enter('BB222BB');assert p.exit('AA111AA');assert not p.exit('X')
print('P043: TDD parking PASS')
