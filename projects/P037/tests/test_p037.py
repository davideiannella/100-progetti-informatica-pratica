from fastapi.testclient import TestClient
import sys,pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]/'src'))
from app import app
c=TestClient(app)
assert c.get('/health').status_code==200
assert c.get('/stops/A').json()['name']=='Centro'
assert c.get('/stops/X').status_code==404
assert c.get('/stops/A/arrivals').json()['minutes']==[3,11]
assert c.post('/alerts',json={'stop_id':'A','message':'ritardo linea'}).status_code==201
assert c.post('/alerts',json={'stop_id':'X','message':'ritardo linea'}).status_code==400
print('P037: FastAPI contract PASS')
