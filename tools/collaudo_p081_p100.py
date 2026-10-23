"""Collauda la copia pubblica dei progetti senza modificare i sorgenti."""
from pathlib import Path
import hashlib
import importlib.metadata
import json
import os
import platform
import py_compile
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_TESTS = [14,12,22,15,17,18,23,22,18,19,13,22,22,20,26,19,14,17,20,24]

def main():
    manifest = json.loads((ROOT / "SOURCE_SHA256.json").read_text())
    mismatches = [name for name, expected in manifest.items()
                  if not (ROOT / name).is_file() or hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != expected]
    if mismatches:
        raise RuntimeError("Sorgenti diversi dal manifest: " + repr(mismatches))
    out = ROOT / "test-results"
    out.mkdir(exist_ok=True)
    summary = {"python": sys.version, "system": platform.system(), "platform": platform.platform(),
               "github_run_id": os.environ.get("GITHUB_RUN_ID"), "github_sha": os.environ.get("GITHUB_SHA"),
               "hashes_verified": len(manifest), "hash_mismatches": mismatches,
               "dependencies": {name: importlib.metadata.version(name) for name in
                    ["numpy", "scipy", "scikit-learn", "joblib", "threadpoolctl", "Pillow"]},
               "projects": [], "compiled_files": 0}
    failures = []
    with tempfile.TemporaryDirectory() as compiled:
        for n, expected in zip(range(81, 101), EXPECTED_TESTS):
            name = f"P{n:03d}"
            project = ROOT / "projects" / name
            for index, path in enumerate(sorted(project.rglob("*.py"))):
                py_compile.compile(str(path), cfile=str(Path(compiled) / f"{name}_{index}.pyc"), doraise=True)
                summary["compiled_files"] += 1
            env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONUTF8="1")
            result = subprocess.run([sys.executable, "-B", "run_tests.py"], cwd=project,
                                    env=env, capture_output=True, text=True, encoding="utf-8", timeout=180)
            (out / f"{name}.stdout.txt").write_text(result.stdout, encoding="utf-8")
            (out / f"{name}.stderr.txt").write_text(result.stderr, encoding="utf-8")
            combined = result.stdout + "\n" + result.stderr
            counts = re.findall(r"Ran (\d+) tests? in", combined)
            skipped = sum(int(x) for x in re.findall(r"skipped=(\d+)", combined))
            count = int(counts[-1]) if counts else 0
            ok = result.returncode == 0 and count == expected and skipped == 0
            row = {"project": name, "returncode": result.returncode, "test_methods": count,
                   "expected_test_methods": expected, "skipped": skipped, "status": "PASS" if ok else "FAIL"}
            summary["projects"].append(row)
            row["stdout_file"] = f"{name}.stdout.txt"
            row["stderr_file"] = f"{name}.stderr.txt"
            print(json.dumps(row), flush=True)
            print(f"=== {name} STDOUT_BEGIN ===", flush=True)
            print(result.stdout if result.stdout else "(nessun testo emesso su stdout)", end="" if result.stdout.endswith("\n") else "\n", flush=True)
            print(f"=== {name} STDOUT_END ===", flush=True)
            print(f"=== {name} STDERR_BEGIN ===", flush=True)
            print(result.stderr if result.stderr else "(nessun testo emesso su stderr)", end="" if result.stderr.endswith("\n") else "\n", flush=True)
            print(f"=== {name} STDERR_END ===", flush=True)
            if not ok:
                failures.append(name)
    summary["test_methods"] = sum(x["test_methods"] for x in summary["projects"])
    summary["status"] = "PASS" if not failures else "FAIL"
    summary["failed_projects"] = failures
    (out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print("COLLAUDO_SUMMARY_BEGIN", flush=True)
    print(json.dumps(summary, indent=2), flush=True)
    print("COLLAUDO_SUMMARY_END", flush=True)
    return 0 if not failures else 1

if __name__ == "__main__":
    sys.exit(main())
