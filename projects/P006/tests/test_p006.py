import unittest,sys,math
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]/'src'))
from p006_main import dijkstra
class T(unittest.TestCase):
    def test_shortest(self):
        g={'A':{'B':1,'C':5},'B':{'C':2},'C':{}}
        self.assertEqual(dijkstra(g,'A','C'),(3,['A','B','C']))
    def test_unreachable(self):
        g={'A':{},'B':{}}; d,p=dijkstra(g,'A','B'); self.assertTrue(math.isinf(d)); self.assertEqual(p,[])
    def test_negative(self):
        g={'A':{'B':-1},'B':{}}
        with self.assertRaises(ValueError): dijkstra(g,'A','B')
if __name__=='__main__': unittest.main()
