import json
import math
import sys
import unittest
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import recommender as m


def cosine_oracle(a,b):
    numerator=math.fsum(x*y for x,y in zip(a,b))
    denominator=math.sqrt(math.fsum(x*x for x in a))*math.sqrt(math.fsum(y*y for y in b))
    return min(1.0,max(0.0,numerator/denominator))


class RecommenderContracts(unittest.TestCase):
    def test_reference_ranking(self):
        r=m.recommend([1,0,1,1],5)
        self.assertEqual([name for name,_ in r],['ml','python','sql','java','reti'])
        np.testing.assert_allclose([s for _,s in r],[1,2/math.sqrt(6),2/math.sqrt(6),1/math.sqrt(6),1/math.sqrt(6)],atol=1e-14)

    def test_ties_ignore_catalog_insertion_order(self):
        a={'zeta':[1,0,0,0],'alfa':[1,0,0,0]}
        b=dict(reversed(list(a.items())))
        self.assertEqual(m.recommend([1,0,0,0],courses=a),m.recommend([1,0,0,0],courses=b))
        self.assertEqual(m.recommend([1,0,0,0],courses=a)[0][0],'alfa')

    def test_k_zero_and_larger_than_catalog(self):
        self.assertEqual(m.recommend([1,0,0,0],0),[])
        self.assertEqual(len(m.recommend([1,0,0,0],99)),5)
        self.assertEqual(len(m.recommend([1,0,0,0],np.int64(2))),2)

    def test_exclusions_and_empty_catalog(self):
        self.assertEqual(m.recommend([1,0,1,1],exclude=['ml'])[0][0],'python')
        self.assertEqual(m.recommend([1,0,0,0],courses={}),[])
        self.assertEqual(m.recommend([1,0,0,0],exclude=m.COURSES),[])
        self.assertEqual(m.recommend([1,0,0,0],exclude=['missing']),m.recommend([1,0,0,0]))

    def test_orthogonal_vectors(self):
        self.assertEqual(m.recommend([1,0,0,0],courses={'x':[0,1,0,0]}),[('x',0)])

    def test_extreme_finite_scaling(self):
        a=m.recommend([1,0,1,1],5)
        b=m.recommend([1e308,0,1e308,1e308],5)
        c=m.recommend([1e-300,0,1e-300,1e-300],5)
        self.assertEqual(a,b)
        self.assertEqual(a,c)
        r=m.recommend([1e308,1e308,1e308,1e308],courses={'x':[1e308]*4})
        self.assertEqual(r,[('x',1.0)])

    def test_invalid_profile(self):
        for p in [[],[1],[1,2,3],[[1,0,1,1]],[[1,0],[1,1]],[-1,0,1,1],
                  [0,0,0,0],[np.nan,0,1,1],[np.inf,0,1,1]]:
            with self.subTest(p=p),self.assertRaises(ValueError):
                m.recommend(p)

    def test_invalid_k(self):
        for k in [-1,True,np.bool_(False),1.5,'2',None]:
            with self.subTest(k=k),self.assertRaises(ValueError):
                m.recommend([1,0,1,1],k)

    def test_invalid_catalog(self):
        for catalog in [[],{'x':[]},{'x':[0]*4},{'x':[1,2,np.nan,4]},{'x':[1,2,np.inf,4]},
                        {'x':[-1,0,1,1]},{'':[1,0,0,0]},{3:[1,0,0,0]}]:
            with self.subTest(catalog=catalog),self.assertRaises(ValueError):
                m.recommend([1,0,0,0],courses=catalog)

    def test_invalid_exclude(self):
        for exclude in ['ml',None,[1],[['ml']]]:
            with self.subTest(exclude=exclude),self.assertRaises(ValueError):
                m.recommend([1,0,0,0],exclude=exclude)

    def test_inputs_are_not_modified(self):
        p=np.array([1.,0.,1.,1.]);saved=p.copy()
        c={'x':np.array([1.,2.,3.,4.])};before=c['x'].copy()
        m.recommend(p,courses=c)
        np.testing.assert_array_equal(p,saved)
        np.testing.assert_array_equal(c['x'],before)

    def test_determinism(self):
        self.assertEqual(m.run_example(),m.run_example())


class SeededOracleChecks(unittest.TestCase):
    pass


def seeded_case(seed):
    def test(self):
        rng=np.random.default_rng(seed)
        profile=rng.uniform(.001,10,4).tolist()
        catalog={f'corso_{i}':rng.uniform(.001,10,4).tolist() for i in range(7)}
        k=int(rng.integers(0,10));exclude=['corso_2']
        actual=m.recommend(profile,k,catalog,exclude)
        reference=sorted([(name,cosine_oracle(profile,v)) for name,v in catalog.items() if name not in exclude],key=lambda x:(-x[1],x[0]))[:k]
        self.assertEqual([name for name,_ in actual],[name for name,_ in reference])
        np.testing.assert_allclose([score for _,score in actual],[score for _,score in reference],atol=1e-14,rtol=1e-14)
        scaled=m.recommend(np.array(profile)*37,k,catalog,exclude)
        self.assertEqual([name for name,_ in actual],[name for name,_ in scaled])
        np.testing.assert_allclose([s for _,s in actual],[s for _,s in scaled],atol=1e-14)
        print('SEED_RESULT '+json.dumps({'seed':seed,'k':k,'candidates':6,'returned':len(actual),
                                       'top_score':actual[0][1] if actual else None},sort_keys=True))
    return test


for seed in range(100):
    setattr(SeededOracleChecks,f'test_seed_{seed:03d}',seeded_case(seed))


if __name__=='__main__':
    unittest.main(verbosity=2)
