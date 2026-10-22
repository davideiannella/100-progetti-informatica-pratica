import unittest,sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]/'src'))
from p011_main import analyze
class T(unittest.TestCase):
    def test_parse(self):
        r=analyze(['INFO GET /health 200','ERROR POST /items 500']); self.assertEqual(r['levels']['ERROR'],1); self.assertEqual(r['status'][200],1)
    def test_malformed(self): self.assertEqual(analyze(['bad'])['malformed'],1)
    def test_empty(self): self.assertEqual(sum(analyze([])['levels'].values()),0)
if __name__=='__main__': unittest.main()
