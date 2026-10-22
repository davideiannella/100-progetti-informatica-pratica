import unittest,sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]/'src'))
from p007_main import Trie
class T(unittest.TestCase):
    def setUp(self):
        self.t=Trie(); [self.t.insert(x) for x in ['python','pytest','pyramid','java']]
    def test_prefix(self): self.assertEqual(self.t.autocomplete('py'),['pyramid','pytest','python'])
    def test_limit(self): self.assertEqual(len(self.t.autocomplete('py',2)),2)
    def test_none(self): self.assertEqual(self.t.autocomplete('zz'),[])
    def test_empty_word(self):
        with self.assertRaises(ValueError): Trie().insert(' ')
if __name__=='__main__': unittest.main()
