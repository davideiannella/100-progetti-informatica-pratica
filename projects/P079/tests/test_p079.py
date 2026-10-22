import pathlib, sys, unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

import numpy as np
import forecast as m

class TestForecast(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=m.experiment()

    def test_features_exactly_past(self):
        X,y,t=m.make_supervised(np.arange(30,dtype=float))
        np.testing.assert_array_equal(X[:,0],t-1)
        np.testing.assert_array_equal(X[:,1],t-7)
        np.testing.assert_array_equal(X[:,2],t)
        np.testing.assert_array_equal(y,t)

    def test_time_split(self):
        r=self.result
        self.assertEqual((r['train_samples'],r['test_samples']),(173,60))
        self.assertLess(max(r['train_time_indices']),min(r['test_time_indices']))
        self.assertEqual(r['test_time_indices'],list(range(180,240)))

    def test_backtests_are_chronological(self):
        previous=set()
        for fold in self.result['backtest_folds']:
            self.assertLess(max(fold['train_time_indices']),min(fold['test_time_indices']))
            self.assertFalse(previous&set(fold['test_time_indices']))
            previous.update(fold['test_time_indices'])

    def test_mae_recomputed(self):
        r=self.result
        expected=sum(abs(a-p) for a,p in zip(r['actual'],r['predicted']))/60
        self.assertAlmostEqual(r['mae'],expected)
        self.assertGreaterEqual(r['mae'],0)

    def test_baselines_use_past_observations(self):
        r=self.result;y=r['series']
        self.assertEqual(r['naive_last'],y[179:239])
        self.assertEqual(r['naive_week'],y[173:233])
        self.assertLess(r['mae'],r['baseline_mae'])

    def test_constant_demand(self):
        r=m.evaluate_one_step(np.full(60,7.0),cut=40)
        np.testing.assert_allclose(r['predicted'],7)
        self.assertAlmostEqual(r['mae'],0)

    def test_recursive_and_rolling_first_prediction_agree(self):
        y=m.series()
        p=m.forecast_recursive(y[:180],60)
        self.assertAlmostEqual(p[0],self.result['predicted'][0])
        self.assertFalse(np.allclose(p,self.result['predicted']))

    def test_recursive_linear_demand(self):
        y=np.arange(1,61,dtype=float)
        np.testing.assert_allclose(m.forecast_recursive(y,10),np.arange(61,71),atol=1e-8)

    def test_invalid_series(self):
        for y in [[],[1]*7,[[1]*30],[True]*30,['2']*30,[None]*30,[1]*29+[float('nan')],[1]*29+[float('inf')],[-1]*30,[1e308]*30]:
            with self.subTest(y=repr(y)[:50]),self.assertRaises(ValueError):m.evaluate_one_step(y,cut=21)

    def test_invalid_boundaries(self):
        for cut in [-1,7,20,240,241,True,23.5,None]:
            with self.subTest(cut=cut),self.assertRaises(ValueError):m.evaluate_one_step(m.series(),cut=cut)
        for stop in [180,241,False]:
            with self.subTest(stop=stop),self.assertRaises(ValueError):m.evaluate_one_step(m.series(),stop=stop)

    def test_invalid_generator_or_horizon(self):
        for n in [-1,0,7,8.1,True]:
            with self.subTest(n=n),self.assertRaises(ValueError):m.series(n)
        for h in [0,-1,366,1.5,True,float('inf')]:
            with self.subTest(h=h),self.assertRaises(ValueError):m.forecast_recursive(m.series()[:40],h)

    def test_generator_is_deterministic(self):
        np.testing.assert_array_equal(m.series(seed=123),m.series(seed=123))
        self.assertFalse(np.array_equal(m.series(seed=123),m.series(seed=124)))

    def test_training_prefix_independent_of_future(self):
        y=m.series();altered=y.copy();altered[180:]+=1000
        a=m.fit_history(y[:180]);b=m.fit_history(altered[:180])
        np.testing.assert_array_equal(a.coef_,b.coef_)


def seeded_case(seed):
    def test(self):
        rng=np.random.default_rng(seed);n=int(rng.integers(65,140));cut=int(rng.integers(30,n-12))
        t=np.arange(n);y=30+rng.uniform(0,.3)*t+rng.uniform(1,8)*np.sin(2*np.pi*t/7)+rng.normal(0,1,n)
        boundary=int(rng.integers(cut,n-1));altered=y.copy();altered[boundary:]+=rng.uniform(5,50,n-boundary)
        a=m.evaluate_one_step(y,cut=cut);b=m.evaluate_one_step(altered,cut=cut)
        count=boundary-cut+1
        np.testing.assert_allclose(a['predicted'][:count],b['predicted'][:count],rtol=0,atol=0)
        self.assertTrue(np.isfinite(a['predicted']).all())
        self.assertEqual(a['test_samples'],n-cut)
    return test
for seed in range(100):
    setattr(TestForecast,f'test_seed_{seed:03d}',seeded_case(seed))

if __name__ == "__main__": unittest.main(verbosity=2)
