import unittest,sys,sqlite3
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]/'src'))
from p010_main import *
class T(unittest.TestCase):
    def test_transform(self): self.assertEqual(transform({'istat':' 1 ','nome':' roma ','provincia':'rm','popolazione':'10'})['provincia'],'RM')
    def test_idempotent(self):
        c=sqlite3.connect(':memory:'); rows=[{'istat':'1','nome':'A','provincia':'LT','popolazione':'10'}]
        load_rows(c,rows); load_rows(c,rows); self.assertEqual(c.execute('select count(*) from comuni').fetchone()[0],1)
    def test_update(self):
        c=sqlite3.connect(':memory:'); load_rows(c,[{'istat':'1','nome':'A','provincia':'LT','popolazione':'10'}]); load_rows(c,[{'istat':'1','nome':'A','provincia':'LT','popolazione':'20'}]); self.assertEqual(c.execute('select popolazione from comuni').fetchone()[0],20)
if __name__=='__main__': unittest.main()
