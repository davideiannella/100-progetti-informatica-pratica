import sys,pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]/"src"))
from graph_route import shortest
g={"A":[("B",5),("C",20)],"B":[("C",7)],"C":[]}
assert shortest(g,"A","C")== (12,["A","B","C"])
print("P032: shortest path PASS; Cypher STATIC QA")
