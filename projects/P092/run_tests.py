"""Esegue i metodi unittest del progetto senza dipendenze esterne."""
from pathlib import Path
import sys
import unittest

if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    suite = unittest.defaultTestLoader.discover(str(root / "tests"), pattern="test_*.py")
    if suite.countTestCases() == 0:
        raise SystemExit("Nessun metodo unittest trovato.")
    result = unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(suite)
    raise SystemExit(0 if result.wasSuccessful() else 1)
