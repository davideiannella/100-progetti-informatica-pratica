"""Esegue la suite standard unittest anche da una directory diversa."""
from pathlib import Path
import sys
import unittest

if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    suite = unittest.defaultTestLoader.discover(str(root / "tests"), pattern="test_*.py")
    count = suite.countTestCases()
    if count == 0:
        raise SystemExit("Nessun test scoperto")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print(f"test_methods={count}; executed={result.testsRun}; failures={len(result.failures)}; errors={len(result.errors)}")
    raise SystemExit(0 if result.wasSuccessful() else 1)
