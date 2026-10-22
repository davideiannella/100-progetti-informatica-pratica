from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
app = FastAPI(title='Transit API')
STOPS = {'A': {'id': 'A', 'name': 'Centro'}, 'B': {'id': 'B', 'name': 'Stazione'}}
ARRIVALS = {'A': [3, 11], 'B': [5]}

class Alert(BaseModel):
    stop_id: str
    message: str = Field(min_length=3, max_length=120)

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.get('/stops/{stop_id}')
def stop(stop_id: str):
    if stop_id not in STOPS:
        raise HTTPException(404, 'stop not found')
    return STOPS[stop_id]

@app.get('/stops/{stop_id}/arrivals')
def arrivals(stop_id: str):
    if stop_id not in STOPS:
        raise HTTPException(404, 'stop not found')
    return {'stopId': stop_id, 'minutes': ARRIVALS[stop_id]}

@app.post('/alerts', status_code=201)
def create_alert(alert: Alert):
    if alert.stop_id not in STOPS:
        raise HTTPException(400, 'invalid stop')
    return alert
