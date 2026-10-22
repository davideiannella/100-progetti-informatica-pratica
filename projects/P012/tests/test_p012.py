import unittest,sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]/'src'))
from p012_main import knapsack
class T(unittest.TestCase):
    def test_optimum(self): self.assertEqual(knapsack([('A',2,3),('B',3,4),('C',4,5)],5),(7,['A','B']))
    def test_zero(self): self.assertEqual(knapsack([('A',2,3)],0),(0,[]))
    def test_invalid(self):
        with self.assertRaises(ValueError): knapsack([('A',0,3)],5)
if __name__=='__main__': unittest.main()
