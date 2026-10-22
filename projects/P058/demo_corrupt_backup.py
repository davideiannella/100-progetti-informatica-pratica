from pathlib import Path
from tempfile import TemporaryDirectory
from src.backup import create_backup, restore_backup
with TemporaryDirectory() as directory:
    root = Path(directory)
    source = root / "source.txt"
    source.write_text("versione-1")
    meta = create_backup(source, root / "repo", "prova")
    target = root / "target.txt"
    target.write_text("dato valido")
    Path(meta["path"]).write_text("copia corrotta")
    try:
        restore_backup(meta["path"], target, meta["sha256"])
    except ValueError:
        assert target.read_text() == "dato valido"
        print("Target conservato")
