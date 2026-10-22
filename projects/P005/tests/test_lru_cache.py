import unittest,sys,random
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]/"src"))
from lru_cache import LRUCache
class T(unittest.TestCase):
 def test_hit(self): c=LRUCache(2); c.put('a',1); self.assertEqual(c.get('a'),1)
 def test_miss(self): self.assertIsNone(LRUCache(1).get('x'))
 def test_eviction(self): c=LRUCache(2); c.put('a',1); c.put('b',2); c.get('a'); c.put('c',3); self.assertIsNone(c.get('b')); self.assertEqual(c.keys_mru_to_lru(),['c','a'])
 def test_update(self): c=LRUCache(1); c.put('a',1); c.put('a',2); self.assertEqual(c.get('a'),2)
 def test_capacity_zero(self): c=LRUCache(0); c.put('a',1); self.assertIsNone(c.get('a'))
 def test_invalid_capacity(self):
  with self.assertRaises(ValueError): LRUCache(-1)
 def test_order(self): c=LRUCache(3); [c.put(x,x) for x in 'abc']; self.assertEqual(c.keys_mru_to_lru(),['c','b','a'])
 def test_random_invariants(self):
  c=LRUCache(5)
  for i in range(1000):
   k=random.randint(0,9)
   if random.random()<.6:c.put(k,i)
   else:c.get(k)
   self.assertLessEqual(len(c.map),5)
if __name__=='__main__':unittest.main()
