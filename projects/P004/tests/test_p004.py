import unittest,sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]/'src'))
from p004_main import *
class T(unittest.TestCase):
    def test_priority(self):
        s=Scheduler(); s.add(Job('a',3)); s.add(Job('b',1)); self.assertEqual(s.pop().id,'b')
    def test_stable(self):
        s=Scheduler(); s.add(Job('a',2)); s.add(Job('b',2)); self.assertEqual([s.pop().id,s.pop().id],['a','b'])
    def test_empty(self): self.assertIsNone(Scheduler().pop())
    def test_invalid(self):
        with self.assertRaises(ValueError): Scheduler().add(Job('x',0))
if __name__=='__main__': unittest.main()
