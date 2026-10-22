from pathlib import Path
import sys,zipfile
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from fastapi.testclient import TestClient
import app
c=TestClient(app.app);app.items.clear()
assert c.get('/health').json()=={'status':'ok'}
assert c.post('/items/1',json={'name':'router','quantity':2}).status_code==200
assert c.get('/items/1').json()['quantity']==2
for body in [{'name':' ','quantity':1},{'name':'x','quantity':True},{'name':'x','quantity':1.2},{'name':'x','quantity':-1}]:
    assert c.post('/items/2',json=body).status_code==422
assert c.get('/items/0').status_code==400
assert c.get('/items/99').status_code==404
sys.path.insert(0,str(Path(__file__).parents[1]/'tools'))
from build_release import build
m=build()
with zipfile.ZipFile(Path(__file__).parents[1]/'output'/m['artifact']) as z:
    assert {'src/app.py','requirements.txt','Dockerfile'}<=set(z.namelist())
print('P054 PASS: HTTP e dipendenze dentro la release')
