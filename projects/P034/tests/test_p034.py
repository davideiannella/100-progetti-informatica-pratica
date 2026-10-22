import sys,pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]/"src"))
from record_linkage import score,match

a={"name":"Maria Rossi","city":"Roma","email":"m.rossi@example.it"}
b={"name":"Maria  Rossi","city":"Roma","email":"mrossi@example.it"}
c={"name":"Luca Bianchi","city":"Milano","email":"luca@example.it"}
assert match(a,b)
assert not match(a,c)
assert score(a,b)>score(a,c)
print("P034: record linkage PASS")
