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
    def test_mean_at_float_limits(self):
        for value in (1e308, sys.float_info.max, float.fromhex('0x0.0000000000001p-1022')):
            with self.subTest(value=value):
                rows = [{'date':'a','kwh':str(value)}, {'date':'b','kwh':str(value)}]
                r = analyze_rows(rows)
                self.assertEqual(r['mean'], value)
                self.assertEqual(r['min'], value)
                self.assertEqual(r['max'], value)
                self.assertEqual(r['count'], 2)
if __name__=='__main__': unittest.main()
