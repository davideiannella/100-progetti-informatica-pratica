import unittest, tempfile, csv
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]/'src'))
from p002_main import analyze_rows

class T(unittest.TestCase):
    def test_stats(self):
        r=analyze_rows([{'date':'a','kwh':'2'},{'date':'b','kwh':'4'}],3)
        self.assertEqual(r['mean'],3); self.assertEqual(r['peaks'],['b'])
    def test_missing(self):
        r=analyze_rows([{'date':'a','kwh':''},{'date':'b','kwh':'x'}])
        self.assertEqual(r['missing'],2); self.assertEqual(r['count'],0)
    def test_negative(self):
        with self.assertRaises(ValueError): analyze_rows([{'date':'a','kwh':'-1'}])
if __name__=='__main__': unittest.main()
