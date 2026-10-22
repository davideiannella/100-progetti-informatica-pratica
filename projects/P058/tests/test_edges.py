from pathlib import Path
import sys,tempfile
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from backup import *
with tempfile.TemporaryDirectory() as d:
    r=Path(d);source=r/'source';source.write_bytes(bytes(range(256))*1000)
    m=create_backup(source,r/'repo','one')
    try:create_backup(source,r/'repo','one')
    except FileExistsError:pass
    else:raise AssertionError('backup overwritten')
    target=r/'target';target.write_bytes(b'keep')
    Path(m['path']).write_bytes(b'corrupted')
    try:restore_backup(m['path'],target,m['sha256'])
    except ValueError:pass
    else:raise AssertionError('corrupt backup restored')
    assert target.read_bytes()==b'keep'
    assert not list(r.glob('.backup-*'))
print('P058 PASS: backup duplicato rifiutato e target preservato su corruzione')
