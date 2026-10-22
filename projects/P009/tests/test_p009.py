import unittest,sys,pandas as pd
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]/'src'))
from p009_main import analyze
class T(unittest.TestCase):
    def test_density(self):
        df=pd.DataFrame([{'provincia':'LT','comune':'A','popolazione':100,'superficie_km2':10}])
        x,a=analyze(df); self.assertEqual(x.iloc[0].densita,10); self.assertEqual(a.iloc[0].densita,10)
    def test_aggregate(self):
        df=pd.DataFrame([{'provincia':'LT','comune':'A','popolazione':100,'superficie_km2':10},{'provincia':'LT','comune':'B','popolazione':200,'superficie_km2':10}])
        _,a=analyze(df); self.assertEqual(int(a.iloc[0].popolazione),300)
    def test_invalid(self):
        df=pd.DataFrame([{'provincia':'LT','comune':'A','popolazione':1,'superficie_km2':0}])
        with self.assertRaises(ValueError): analyze(df)
if __name__=='__main__': unittest.main()
