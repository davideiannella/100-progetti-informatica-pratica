from __future__ import annotations
from pathlib import Path
import hashlib, json, py_compile, sys, zipfile

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)


def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(65536),b''):
            h.update(chunk)
    return h.hexdigest()


def build() -> dict:
    # Gate 1: il sorgente deve compilare.
    for py in SRC.rglob('*.py'):
        py_compile.compile(str(py), doraise=True)

    artifact = OUT / "p054_api_release.zip"
    files = sorted([p for p in SRC.rglob('*') if p.is_file() and '__pycache__' not in p.parts] + [ROOT/'requirements.txt', ROOT/'Dockerfile'])
    with zipfile.ZipFile(artifact,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for f in files:
            info=zipfile.ZipInfo(str(f.relative_to(ROOT)))
            info.date_time=(2026,1,1,0,0,0)  # timestamp fisso per build riproducibile
            info.external_attr=0o644 << 16
            z.writestr(info,f.read_bytes())
    manifest={
        "project":"P054",
        "artifact":artifact.name,
        "sha256":sha256(artifact),
        "python":f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        "files":[str(f.relative_to(ROOT)) for f in files],
    }
    (OUT/'release_manifest.json').write_text(json.dumps(manifest,indent=2,sort_keys=True),encoding='utf-8')
    return manifest

if __name__=='__main__':
    print(json.dumps(build(),indent=2,sort_keys=True))
