import json
import math
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import energy_regression as m


class EnergyContracts(unittest.TestCase):
    def test_noiseless_known_coefficients(self):
        X, y = m.make_data(n=400, noise=0)
        model = m.train_model(X[:300], y[:300])
        np.testing.assert_allclose(model.coef_, [.8, 8, .08], atol=1e-10)
        self.assertAlmostEqual(model.intercept_, 18, places=10)
        np.testing.assert_allclose(m.predict(model, X[300:]), y[300:], atol=1e-10)

    def test_symmetric_temperature_feature(self):
        np.testing.assert_array_equal(m.design_matrix([[10, 1, 12]]), m.design_matrix([[30, 1, 12]]))

    def test_metric_hand_calculation(self):
        result = m.regression_metrics([1, 3, 5], [2, 3, 3])
        self.assertEqual(result['mae'], 1)
        self.assertAlmostEqual(result['rmse'], math.sqrt(5/3))

    def test_determinism(self):
        self.assertEqual(m.run_experiment(), m.run_experiment())

    def test_default_model_beats_predeclared_baselines(self):
        r = m.experiment()
        self.assertLess(r['mae'], r['baseline_mae'])
        self.assertLess(r['mae'], r['raw_temperature_mae'])

    def test_no_test_rows_or_targets_in_fit(self):
        X, y = m.make_data()
        real = m.train_model
        with patch.object(m, 'train_model', wraps=real) as spy:
            m.run_experiment()
        args = spy.call_args.args
        np.testing.assert_array_equal(args[0], X[:180])
        np.testing.assert_array_equal(args[1], y[:180])

    def test_changed_training_targets_change_model(self):
        X, y = m.make_data()
        a = m.train_model(X[:180], y[:180])
        b = m.train_model(X[:180], y[:180] + 5)
        self.assertAlmostEqual(b.intercept_ - a.intercept_, 5)

    def test_invalid_X(self):
        cases = [[], [1, 0, 3], [[1, 0]], [[1, 0, 3, 4]], [[np.nan, 0, 3]], [[np.inf, 0, 3]],
                 [[1, 2, 3]], [[1, 0, -1]], [[1, 0, 24]], [[1, 0, 2.5]]]
        for X in cases:
            with self.subTest(X=X), self.assertRaises(ValueError):
                m.design_matrix(X)

    def test_invalid_targets(self):
        X, y = m.make_data(n=8)
        for bad in [[], y[:-1], y.reshape(8, 1), [np.nan]*8, [np.inf]*8]:
            with self.subTest(y=bad), self.assertRaises(ValueError):
                m.train_model(X, bad)
        with self.assertRaises(ValueError):
            m.train_model(X[:3], y[:3])

    def test_invalid_generator_and_split(self):
        for args in [dict(n=0), dict(n=7), dict(n=True), dict(n=10.5), dict(seed=-1), dict(seed=True),
                     dict(noise=-1), dict(noise=np.nan), dict(noise=np.inf), dict(noise=True)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                m.make_data(**args)
        for cut in [0, 3, 239, 240, True, 1.5]:
            with self.subTest(cut=cut), self.assertRaises(ValueError):
                m.run_experiment(cut=cut)

    def test_invalid_metric_inputs(self):
        for truth, pred in [([], []), ([1], []), ([1], [np.inf]), ([np.nan], [1]), ([[1]], [[1]])]:
            with self.subTest(truth=truth, pred=pred), self.assertRaises(ValueError):
                m.regression_metrics(truth, pred)


class SeededOracleChecks(unittest.TestCase):
    pass


def seeded_case(seed):
    def test(self):
        r = m.run_experiment(seed=seed)
        X, y = m.make_data(seed=seed)
        train, test = np.array(r['train_ids']), np.array(r['test_ids'])
        self.assertEqual(len(set(train) & set(test)), 0)
        self.assertEqual(sorted(list(train) + list(test)), list(range(240)))
        # Oracolo numerico indipendente: equazioni least squares con intercetta esplicita.
        A = np.column_stack([np.ones(240), np.abs(X[:, 0]-20), X[:, 1:]])
        beta = np.linalg.lstsq(A[train], y[train], rcond=None)[0]
        oracle = A[test] @ beta
        np.testing.assert_allclose(r['y_pred'], oracle, rtol=1e-11, atol=1e-10)
        errors = [float(t-p) for t, p in zip(y[test], oracle)]
        self.assertAlmostEqual(r['metrics']['mae'], math.fsum(abs(e) for e in errors)/len(errors), places=10)
        self.assertAlmostEqual(r['metrics']['rmse'], math.sqrt(math.fsum(e*e for e in errors)/len(errors)), places=10)
        np.testing.assert_allclose(r['baseline_predictions'], np.repeat(np.mean(y[train]), 60))
        print('SEED_RESULT ' + json.dumps({'seed': seed, **r['metrics']}, sort_keys=True))
    return test


for seed in range(100):
    setattr(SeededOracleChecks, f'test_seed_{seed:03d}', seeded_case(seed))


if __name__ == '__main__':
    unittest.main(verbosity=2)
