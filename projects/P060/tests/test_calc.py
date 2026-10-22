import unittest,sys,pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]/"src"))
from calc import total
class T(unittest.TestCase):
    def test_total(self): self.assertEqual(total([1,2,3]),6)
    def test_bad(self):
        with self.assertRaises(TypeError): total([1,"x"])
if __name__=="__main__": unittest.main()
