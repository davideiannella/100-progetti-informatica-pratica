"""Esegue tutti i test del progetto, con exit status non zero in caso di errore."""
import json
import sys
import unittest
from pathlib import Path
sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
suite = unittest.defaultTestLoader.discover(str(ROOT / 'tests'), pattern='test_*.py')
result = unittest.TextTestRunner(verbosity=2).run(suite)
print('TEST_SUMMARY ' + json.dumps({'tests_run': result.testsRun, 'failures': len(result.failures),
    'errors': len(result.errors), 'skipped': len(result.skipped), 'successful': result.wasSuccessful()}))
sys.exit(0 if result.wasSuccessful() else 1)
