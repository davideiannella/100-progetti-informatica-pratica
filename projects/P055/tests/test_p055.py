import sqlite3, sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]/"src"))
from app import init_db, add_item, list_items
import yaml

with sqlite3.connect(":memory:") as con:
    init_db(con)
    add_item(con,"uno"); add_item(con,"due")
    assert [x[1] for x in list_items(con)] == ["uno","due"]
    try: add_item(con,"uno")
    except sqlite3.IntegrityError: pass
    else: raise AssertionError("duplicate accepted")
root = Path(__file__).parents[1]
c = yaml.safe_load((root/'compose.yaml').read_text())
assert set(c['services']) == {'web','api','db'}
for name in ['api']:
    context = root/c['services'][name]['build']
    assert (context/'Dockerfile').is_file() and (context/'app.py').is_file()
assert c['services']['api']['depends_on']['db']['condition'] == 'service_healthy'
assert (root/'web/nginx.conf').is_file()
assert c['services']['db']['image'] == 'postgres:17-alpine'
assert c['services']['api']['environment']['DATABASE_URL'].endswith('@db/appdb')
print('P055 PASS: SQLite e struttura Compose; runtime container separato')
