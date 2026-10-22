import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
import json
import recommender as m
print("profilo_sistemi_pratica:", json.dumps(m.recommend([0,1,0,1],5)))
print("profilo_scalato:", json.dumps(m.recommend([2,0,2,2],5)))
print("parita_alfabetica:", json.dumps(m.recommend([1,0,0,0],courses={"zeta":[1,0,0,0],"alfa":[1,0,0,0]})))
print("catalogo_vuoto:", m.recommend([1,0,0,0], courses={}))
print("k_zero:", m.recommend([1,0,0,0], k=0))
print("esercizio:", json.dumps(m.recommend([0,1,0,1],5,exclude=["reti"])))
