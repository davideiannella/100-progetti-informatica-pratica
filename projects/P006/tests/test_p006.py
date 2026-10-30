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
    def test_overflow_reaches_goal_through_later_edges(self):
        for weight in (1e308, 10**308):
            with self.subTest(weight=weight):
                g={'A':{'B':weight},'B':{'C':weight},'C':{'D':1},'D':{}}
                with self.assertRaisesRegex(OverflowError, 'costo minimo'):
                    dijkstra(g,'A','D')
    def test_finite_alternative_replaces_overflow(self):
        g={'S':{'A':1e308,'B':1.2e308},'A':{'C':1e308},
           'B':{'G':1},'C':{'G':1},'G':{}}
        self.assertEqual(dijkstra(g,'S','G'), (1.2e308,['S','B','G']))
    def test_unreachable_goal_with_overflow_elsewhere(self):
        g={'A':{'B':1e308},'B':{'C':1e308},'C':{},'G':{}}
        self.assertEqual(dijkstra(g,'A','G'), (math.inf,[]))
    def test_maximum_finite_cost_is_allowed(self):
        g={'A':{'B':sys.float_info.max},'B':{}}
        self.assertEqual(dijkstra(g,'A','B'), (sys.float_info.max,['A','B']))
    def test_mixed_paths_use_the_same_cost_limit(self):
        big = 10**308
        g={'S':{'A':big,'C':big},'A':{'B':big},'B':{'G':0.0},
           'C':{'D':big},'D':{'G':big},'G':{}}
        with self.assertRaisesRegex(OverflowError, 'costo minimo'):
            dijkstra(g,'S','G')
if __name__=='__main__': unittest.main()
