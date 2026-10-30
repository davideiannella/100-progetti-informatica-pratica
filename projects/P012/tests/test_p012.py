import unittest,sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]/'src'))
from p012_main import knapsack
class T(unittest.TestCase):
    def test_optimum(self): self.assertEqual(knapsack([('A',2,3),('B',3,4),('C',4,5)],5),(7,['A','B']))
    def test_zero(self): self.assertEqual(knapsack([('A',2,3)],0),(0,[]))
    def test_invalid(self):
        with self.assertRaises(ValueError): knapsack([('A',0,3)],5)
    def test_optimum_overflow_is_explicit(self):
        for value in (1e308, 10**308):
            with self.subTest(value=value):
                items=[('A',1,value),('B',1,value),('C',1,1.5e308)]
                with self.assertRaisesRegex(OverflowError, 'valore ottimo'):
                    knapsack(items,2)
    def test_large_values_that_cannot_be_combined(self):
        items=[('A',1,1e308),('B',1,1e308),('C',1,1.5e308)]
        self.assertEqual(knapsack(items,1),(1.5e308,['C']))
    def test_items_too_heavy_do_not_cause_overflow(self):
        items=[('A',1,3),('B',2,1e308),('C',2,1e308)]
        self.assertEqual(knapsack(items,1),(3,['A']))
    def test_maximum_finite_value_is_allowed(self):
        items=[('A',1,sys.float_info.max)]
        self.assertEqual(knapsack(items,1),(sys.float_info.max,['A']))
if __name__=='__main__': unittest.main()
