"""Verifica HTTP reale. Passare il percorso del dotnet SDK come primo argomento."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json, os, socket, subprocess, sys, time
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

root = Path(__file__).resolve().parents[1]
dotnet = sys.argv[1] if len(sys.argv) > 1 else 'dotnet'
with socket.socket() as s:
    s.bind(('127.0.0.1', 0)); port = s.getsockname()[1]
base = f'http://127.0.0.1:{port}'
def request(method, path, data=None):
    body = json.dumps(data).encode() if data is not None else None
    req = Request(base + path, data=body, method=method, headers={'Content-Type': 'application/json'})
    try:
        with urlopen(req, timeout=5) as response:
            raw = response.read(); return response.status, json.loads(raw) if raw else None
    except HTTPError as error:
        raw = error.read()
        try: value = json.loads(raw)
        except ValueError: value = raw.decode()
        return error.code, value

env = dict(os.environ, DOTNET_CLI_TELEMETRY_OPTOUT='1')
log = root/'tests/http_test.log'
with log.open('w') as stream:
    proc = subprocess.Popen([dotnet, str(root/'src/bin/Debug/net8.0/P023.dll'), '--urls', base], stdout=stream, stderr=stream, env=env)
    try:
        deadline = time.monotonic() + 25
        while True:
            try:
                if request('GET', '/health')[0] == 200: break
            except (URLError, OSError): pass
            if proc.poll() is not None or time.monotonic() > deadline: raise RuntimeError('Avvio API non riuscito')
            time.sleep(.1)
        assert request('GET', '/tasks') == (200, [])
        assert request('POST', '/tasks', {'title':' '})[0] == 400
        assert request('POST', '/tasks', {})[0] == 400
        code, task = request('POST', '/tasks', {'title':' Prima attività '})
        assert code == 201 and task['title'] == 'Prima attività' and task['completed'] is False
        assert request('PUT', '/tasks/9999/complete')[0] == 404
        assert request('PUT', '/tasks/abc/complete')[0] == 404
        with ThreadPoolExecutor(max_workers=12) as pool:
            created = list(pool.map(lambda i: request('POST', '/tasks', {'title':f'Task {i}'}), range(100)))
        assert all(code == 201 for code, _ in created)
        ids = [obj['id'] for _, obj in created]
        assert len(set(ids)) == 100
        with ThreadPoolExecutor(max_workers=12) as pool:
            completed = list(pool.map(lambda _: request('PUT', f'/tasks/{task["id"]}/complete'), range(30)))
        assert all(code in (200,409) for code, _ in completed)
        code, tasks = request('GET', '/tasks')
        assert code == 200 and len(tasks) == 101
        assert tasks[0]['completed'] is True
        print('P023: HTTP reale, input invalidi, 100 creazioni concorrenti, 30 completamenti PASS')
    finally:
        proc.terminate()
        try: proc.wait(timeout=8)
        except subprocess.TimeoutExpired: proc.kill(); proc.wait()
