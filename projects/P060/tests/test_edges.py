from pathlib import Path
import sys,unittest,hashlib,json,zipfile
sys.path.insert(0,str(Path(__file__).parents[1]))
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from calc import total
from build_release import build
class Edges(unittest.TestCase):
    def test_iterators(self):self.assertEqual(total(iter([1,2,3])),6)
    def test_empty(self):self.assertEqual(total([]),0)
    def test_invalid(self):
        for value in [True,'x',None]:
            with self.assertRaises(TypeError):total([value])
        for value in [float('nan'),float('inf')]:
            with self.assertRaises(ValueError):total([value])
    def test_reproducible(self):
        a=build();b=build();self.assertEqual(a,b)
        artifact=Path(__file__).parents[1]/a['artifact']
        self.assertEqual(hashlib.sha256(artifact.read_bytes()).hexdigest(),a['sha256'])
        with zipfile.ZipFile(artifact) as z:self.assertEqual(z.read('calc.py'),(Path(__file__).parents[1]/'src/calc.py').read_bytes())
if __name__=='__main__':unittest.main()
