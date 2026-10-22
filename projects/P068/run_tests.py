"""Esegue tutta la suite, anche se invocato da un'altra cartella."""
import json
import pathlib
import sys
import unittest
sys.dont_write_bytecode = True

if __name__ == "__main__":
    base = pathlib.Path(__file__).resolve().parent
    suite = unittest.defaultTestLoader.discover(str(base / "tests"), pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print(json.dumps({"tests_run": result.testsRun, "failures": len(result.failures),
                      "errors": len(result.errors), "skipped": len(result.skipped)}, sort_keys=True))
    sys.exit(0 if result.wasSuccessful() else 1)
