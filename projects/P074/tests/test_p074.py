import json
import math
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import churn as m


def oracle(y, p):
    pairs = list(zip(y, p))
    tn = sum(t == 0 and s < .5 for t, s in pairs)
    fp = sum(t == 0 and s >= .5 for t, s in pairs)
    fn = sum(t == 1 and s < .5 for t, s in pairs)
    tp = sum(t == 1 and s >= .5 for t, s in pairs)
    positives, negatives = [s for t, s in pairs if t == 1], [s for t, s in pairs if t == 0]
    return {'confusion_matrix': [[tn, fp], [fn, tp]], 'accuracy': (tn+tp)/len(y),
            'precision': tp/(tp+fp) if tp+fp else 0, 'recall': tp/(tp+fn) if tp+fn else 0,
            'f1': 2*tp/(2*tp+fp+fn) if 2*tp+fp+fn else 0,
            'brier': math.fsum((t-s)**2 for t,s in pairs)/len(y),
            'log_loss': -math.fsum(t*math.log(s)+(1-t)*math.log1p(-s) for t,s in pairs)/len(y),
            'roc_auc': math.fsum((p>n)+.5*(p==n) for p in positives for n in negatives)/(len(positives)*len(negatives))}


class ChurnContracts(unittest.TestCase):
    def test_hand_calculated_metrics(self):
        r = m.classification_metrics([0, 0, 1, 1], [.1, .7, .4, .9])
        self.assertEqual(r['confusion_matrix'], [[1, 1], [1, 1]])
        self.assertEqual(r['accuracy'], .5)
        self.assertEqual(r['precision'], .5)
        self.assertEqual(r['recall'], .5)
        self.assertEqual(r['f1'], .5)
        self.assertAlmostEqual(r['brier'], .2175)

    def test_training_learns_generator_direction_and_weights(self):
        X, y = m.data(n=20000, seed=51)
        model = m.train_model(X, y)
        scaler = model.named_steps['standardscaler']
        logistic = model.named_steps['logisticregression']
        raw = logistic.coef_[0] / scaler.scale_
        np.testing.assert_allclose(raw, [-.02, .45, -.005], atol=.008, rtol=.15)
        intercept = float(logistic.intercept_[0] - raw @ scaler.mean_)
        self.assertAlmostEqual(intercept, -.5, delta=.2)

    def test_determinism(self):
        self.assertEqual(m.run_experiment(), m.run_experiment())

    def test_training_preprocessor_never_receives_test(self):
        X, y = m.data()
        real = m.train_model
        with patch.object(m, 'train_model', wraps=real) as spy:
            result = m.run_experiment()
        np.testing.assert_array_equal(spy.call_args.args[0], X[:380])
        np.testing.assert_array_equal(spy.call_args.args[1], y[:380])
        np.testing.assert_allclose(result['scaler_mean'], X[:380].mean(axis=0))
        self.assertFalse(np.allclose(result['scaler_mean'], X.mean(axis=0)))

    def test_predict_does_not_change_scaler(self):
        X, y = m.data()
        model = m.train_model(X[:380], y[:380])
        before = model.named_steps['standardscaler'].mean_.copy()
        altered_test = X[380:].copy(); altered_test[:, 2] += 1e6
        m.predict_probability(model, altered_test)
        np.testing.assert_array_equal(model.named_steps['standardscaler'].mean_, before)

    def test_all_negative_and_single_class(self):
        r = m.classification_metrics([0, 1], [.1, .1])
        self.assertEqual(r['recall'], 0)
        self.assertEqual(r['precision'], 0)
        self.assertEqual(r['f1'], 0)
        one = m.classification_metrics([0, 0], [.1, .2])
        self.assertIsNone(one['roc_auc'])
        self.assertTrue(math.isfinite(one['log_loss']))

    def test_threshold_includes_equality(self):
        self.assertEqual(m.classification_metrics([1], [.5])['confusion_matrix'], [[0, 0], [0, 1]])

    def test_invalid_training_X(self):
        cases = [[], [1, 0, 30], [[1, 0]], [[1, 0, np.nan]], [[1, 0, np.inf]],
                 [[0, 0, 1]], [[1, -1, 1]], [[1.5, 1, 2]], [[1, 1.5, 2]], [[1, 0, -1]]]
        for X in cases:
            with self.subTest(X=X), self.assertRaises(ValueError):
                m.train_model(X, [0])

    def test_invalid_labels(self):
        X, y = m.data(n=8)
        for labels in [[], [0]*8, [1]*8, [2]*8, [np.nan]*8, [np.inf]*8, y.reshape(8,1)]:
            with self.subTest(y=labels), self.assertRaises(ValueError):
                m.train_model(X, labels)

    def test_invalid_probability_and_threshold(self):
        for p in [[], [np.nan], [np.inf], [-.1], [1.1], [[.5]]]:
            with self.subTest(p=p), self.assertRaises(ValueError):
                m.classification_metrics([1], p)
        for threshold in [-.1, 1.1, np.nan, np.inf, True]:
            with self.subTest(threshold=threshold), self.assertRaises(ValueError):
                m.classification_metrics([1], [.5], threshold)

    def test_invalid_generator_and_split(self):
        for args in [dict(n=0),dict(n=True),dict(n=3),dict(n=5.5),dict(seed=-1),dict(seed=True)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                m.data(**args)
        for cut in [1, 499, 500, True, 1.5]:
            with self.subTest(cut=cut), self.assertRaises(ValueError):
                m.run_experiment(cut=cut)


class SeededOracleChecks(unittest.TestCase):
    pass


def seeded_case(seed):
    def test(self):
        result = m.run_experiment(seed=seed)
        X, y = m.data(seed=seed)
        train, test = np.array(result['train_ids']), np.array(result['test_ids'])
        self.assertFalse(set(train) & set(test))
        self.assertEqual(len(train)+len(test),500)
        np.testing.assert_allclose(result['scaler_mean'], X[train].mean(axis=0))
        self.assertEqual(result['baseline_train_prevalence'],float(y[train].mean()))
        np.testing.assert_array_equal(result['y_true'], y[test])
        # Oracolo della probabilità: formula della sigmoide applicata ai pesi appresi.
        standardized = (X[test] - result['scaler_mean']) / result['scaler_scale']
        z = standardized @ result['learned_coefficients_standardized'] + result['learned_intercept_standardized']
        np.testing.assert_allclose(result['probability'], 1/(1+np.exp(-z)), rtol=1e-14, atol=1e-14)
        checked = oracle(result['y_true'], result['probability'])
        for key, value in checked.items():
            if key == 'confusion_matrix':
                self.assertEqual(result['metrics'][key], value)
            else:
                self.assertAlmostEqual(result['metrics'][key], value, places=12)
        print('SEED_RESULT ' + json.dumps({'seed':seed, **result['metrics'],
                                            'baseline_accuracy':result['baseline_metrics']['accuracy']},sort_keys=True))
    return test


for seed in range(100):
    setattr(SeededOracleChecks, f'test_seed_{seed:03d}', seeded_case(seed))


if __name__ == '__main__':
    unittest.main(verbosity=2)
