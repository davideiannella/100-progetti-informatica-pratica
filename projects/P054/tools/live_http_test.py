from __future__ import annotations
from pathlib import Path
import json, subprocess, sys, time, urllib.request

ROOT=Path(__file__).resolve().parents[1]
PORT=18054
proc=subprocess.Popen(
    [sys.executable,'-m','uvicorn','src.app:app','--host','127.0.0.1','--port',str(PORT),'--log-level','warning'],
    cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
)
try:
    base=f'http://127.0.0.1:{PORT}'
    deadline=time.time()+10
    while True:
        try:
            with urllib.request.urlopen(base+'/health',timeout=1) as r:
                health=json.loads(r.read())
            break
        except Exception:
            if time.time()>deadline:
                raise RuntimeError('API non avviata entro timeout')
            time.sleep(0.2)
    if health!={'status':'ok'}:
        raise AssertionError(health)

    payload=json.dumps({'name':'router','quantity':2}).encode()
    req=urllib.request.Request(base+'/items/1',data=payload,headers={'Content-Type':'application/json'},method='POST')
    with urllib.request.urlopen(req,timeout=2) as r:
        created=json.loads(r.read())
    with urllib.request.urlopen(base+'/items/1',timeout=2) as r:
        fetched=json.loads(r.read())
    assert created['name']=='router' and fetched['quantity']==2
    print(json.dumps({'health':health,'created':created,'fetched':fetched},indent=2))
finally:
    proc.terminate()
    try: proc.wait(timeout=5)
    except subprocess.TimeoutExpired: proc.kill()
