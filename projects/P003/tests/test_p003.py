import unittest, sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]/'src'))
from p003_main import *
class T(unittest.TestCase):
    def setUp(self): self.b=AddressBook(); self.b.add(Contact('Mario','MARIO@EXAMPLE.COM','1'))
    def test_normalization(self): self.assertEqual(self.b.all_sorted()[0].email,'mario@example.com')
    def test_duplicate(self):
        with self.assertRaises(ValueError): self.b.add(Contact('X','mario@example.com'))
    def test_search(self): self.b.add(Contact('Anna','a@x.it')); self.assertEqual(self.b.search('ann')[0].name,'Anna')
    def test_remove(self): self.assertIsNotNone(self.b.remove('MARIO@example.com'))
if __name__=='__main__': unittest.main()
