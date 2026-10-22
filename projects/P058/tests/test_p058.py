import sys,pathlib,tempfile
sys.path.append(str(pathlib.Path(__file__).parents[1]/"src"))
from backup import create_backup,restore_backup,sha256_file

with tempfile.TemporaryDirectory() as d:
    root=pathlib.Path(d); src=root/"db.txt"; repo=root/"repo"; out=root/"restore.txt"
    src.write_text("versione-1")
    m=create_backup(src,repo,"2026-10-12")
    src.write_text("versione-2")
    restore_backup(m["path"],out,m["sha256"])
    assert out.read_text()=="versione-1"
    assert sha256_file(out)==m["sha256"]
print("P058: backup + integrity + restore PASS")
