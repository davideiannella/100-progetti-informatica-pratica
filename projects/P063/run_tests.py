"""Esegue tutta la suite unittest; exit != 0 se fallisce anche un solo caso."""
from pathlib import Path
import argparse
import json
import sys
import unittest

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

class CountedResult(unittest.TextTestResult):
    subcases = 0
    def addSubTest(self, test, subtest, err):
        self.subcases += 1
        super().addSubTest(test, subtest, err)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, help="salva conteggi effettivi in JSON")
    args = parser.parse_args()
    suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"), pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2, resultclass=CountedResult).run(suite)
    report = {"project": ROOT.name, "tests_run": result.testsRun, "subcases": result.subcases,
              "failures": len(result.failures), "errors": len(result.errors),
              "skipped": len(result.skipped), "successful": result.wasSuccessful()}
    print(json.dumps(report, sort_keys=True))
    if args.json:
        args.json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    sys.exit(0 if result.wasSuccessful() else 1)
