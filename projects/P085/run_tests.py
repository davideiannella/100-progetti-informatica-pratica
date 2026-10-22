"""Esegue soltanto i test del progetto; richiede la libreria standard."""
from pathlib import Path
import sys
import unittest

if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    suite = unittest.defaultTestLoader.discover(str(root / "tests"), pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
