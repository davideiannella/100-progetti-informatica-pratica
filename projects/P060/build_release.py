import hashlib
import json
from pathlib import Path
import py_compile
import zipfile

def build():
    root = Path(__file__).resolve().parent
    source = root / "src/calc.py"
    py_compile.compile(str(source), doraise=True)
    artifact = root / "release.zip"
    with zipfile.ZipFile(artifact, "w") as archive:
        info = zipfile.ZipInfo("calc.py", (2026, 1, 1, 0, 0, 0))
        info.external_attr = 0o644 << 16
        archive.writestr(info, source.read_bytes())
    manifest = {"artifact": artifact.name, "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest()}
    (root/"release_manifest.json").write_text(json.dumps(manifest, indent=2))
    return manifest

if __name__ == "__main__":
    print(json.dumps(build(), indent=2))
