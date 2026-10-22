import unittest,sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]/'src'))
from p008_main import *
class T(unittest.TestCase):
    def test_normalize(self): self.assertEqual(normalize('Dàvide Iannella'),'davideiannella')
    def test_exact(self): self.assertEqual(similarity('Mario Rossi','mario-rossi'),1.0)
    def test_pair(self): self.assertTrue(find_pairs(['Mario Rossi','Mario Rosi'],.8))
    def test_no_pair(self): self.assertEqual(find_pairs(['Anna','Giuseppe'],.8),[])
if __name__=='__main__': unittest.main()
