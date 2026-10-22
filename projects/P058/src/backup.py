import hashlib
import os
import re
import tempfile
from pathlib import Path

def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()

def staged_copy(source, parent):
    descriptor, name = tempfile.mkstemp(prefix=".backup-", dir=parent)
    temp = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as output, open(source, "rb") as inp:
            for chunk in iter(lambda: inp.read(65536), b""):
                output.write(chunk)
            output.flush()
            os.fsync(output.fileno())
        return temp
    except BaseException:
        temp.unlink(missing_ok=True)
        raise

def create_backup(src, repo, label):
    if not isinstance(label, str) or not re.fullmatch(r"[A-Za-z0-9_-]+", label):
        raise ValueError("label non valida")
    src, repo = Path(src), Path(repo)
    repo.mkdir(parents=True, exist_ok=True)
    target = repo / f"{label}.bak"
    temp = staged_copy(src, repo)
    try:
        # Hard link atomico senza sovrascrivere un backup con la stessa etichetta.
        os.link(temp, target)
    finally:
        temp.unlink(missing_ok=True)
    return {"path": str(target), "sha256": sha256_file(target), "bytes": target.stat().st_size}

def restore_backup(backup, target, expected_hash):
    backup, target = Path(backup), Path(target)
    if not target.parent.is_dir():
        raise ValueError("cartella di destinazione assente")
    temp = staged_copy(backup, target.parent)
    try:
        if sha256_file(temp) != expected_hash:
            raise ValueError("backup corrotto")
        os.replace(temp, target)
    finally:
        temp.unlink(missing_ok=True)
    return target
