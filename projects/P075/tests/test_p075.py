import json
import math
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import anomaly as m


def confusion_oracle(truth, predicted):
    counts = [[0,0],[0,0]]
    for t,p in zip(truth,predicted):
        counts[t][p] += 1
    return counts


class AnomalyContracts(unittest.TestCase):
    def test_independent_generation_and_no_shared_memory(self):
        s = m.make_splits()
        self.assertFalse(np.shares_memory(s['X_train'],s['X_test']))
        self.assertFalse(set(s['train_ids']) & set(s['test_ids']))
        self.assertFalse({tuple(row) for row in s['X_train']} & {tuple(row) for row in s['X_test']})
        self.assertEqual(np.bincount(s['y_test']).tolist(),[100,30])
        changed = m.make_splits(n_normal_test=200)
        np.testing.assert_array_equal(s['X_train'],changed['X_train'])

    def test_no_test_rows_in_fit(self):
        s = m.make_splits()
        real = m.train_model
        with patch.object(m,'train_model',wraps=real) as spy:
            m.run_experiment()
        np.testing.assert_array_equal(spy.call_args.args[0],s['X_train'])
        self.assertEqual(len(spy.call_args.args[0]),300)

    def test_determinism(self):
        self.assertEqual(m.run_experiment(),m.run_experiment())

    def test_prediction_score_direction(self):
        s = m.make_splits()
        model = m.train_model(s['X_train'])
        pred = m.predict(model,s['X_test'])
        decisions = model.decision_function(s['X_test'])
        np.testing.assert_array_equal(pred,(decisions < 0).astype(int))
        np.testing.assert_allclose(decisions,model.score_samples(s['X_test'])-model.offset_)

    def test_offset_is_training_quantile(self):
        s = m.make_splits()
        model = m.train_model(s['X_train'])
        self.assertAlmostEqual(model.offset_,np.percentile(model.score_samples(s['X_train']),7),places=12)

    def test_hand_metrics_and_no_alert_baseline(self):
        r = m.detection_metrics([0,0,0,1,1],[0,1,0,1,0])
        self.assertEqual(r['confusion_matrix'],[[2,1],[1,1]])
        self.assertEqual(r['precision'],.5)
        self.assertEqual(r['recall'],.5)
        self.assertEqual(r['f1'],.5)
        self.assertEqual(r['false_positive_rate'],1/3)
        self.assertEqual(r['alerts'],2)
        zero = m.detection_metrics([0,1],[0,0])
        self.assertEqual(zero['f1'],0)

    def test_absent_class_has_undefined_auc_and_fpr(self):
        r = m.detection_metrics([1,1],[1,0],[.7,.6])
        self.assertIsNone(r['roc_auc'])
        self.assertIsNone(r['false_positive_rate'])

    def test_invalid_matrices(self):
        for X in [[], [1,2], [[1]], [[1,2,3]], [[np.nan,1]], [[np.inf,1]], [[1,2]]]:
            with self.subTest(X=X),self.assertRaises(ValueError):
                m.train_model(X)
        with self.assertRaises(ValueError):
            m.predict(m.train_model(m.make_splits()['X_train']),[])

    def test_invalid_parameters(self):
        X = m.make_splits()['X_train']
        for contamination in [0,-.1,.51,np.nan,np.inf,True]:
            with self.subTest(contamination=contamination),self.assertRaises(ValueError):
                m.train_model(X,contamination=contamination)
        for seed in [-1,True,1.5,2**32]:
            with self.subTest(seed=seed),self.assertRaises(ValueError):
                m.train_model(X,seed=seed)
        for args in [dict(n_train=1),dict(n_normal_test=0),dict(n_anomalous_test=0),dict(seed=-1),dict(seed=True)]:
            with self.subTest(args=args),self.assertRaises(ValueError):
                m.make_splits(**args)

    def test_invalid_metrics(self):
        for y,p,s in [([],[],None),([0],[0,1],None),([2],[0],None),([np.nan],[0],None),
                      ([0],[np.inf],None),([0],[0],[np.nan]),([0],[0],[]),([[0]],[[0]],None)]:
            with self.subTest(y=y,p=p,s=s),self.assertRaises(ValueError):
                m.detection_metrics(y,p,s)


class SeededOracleChecks(unittest.TestCase):
    pass


def seeded_case(seed):
    def test(self):
        result=m.run_experiment(seed)
        self.assertFalse(set(result['train_ids']) & set(result['test_ids']))
        self.assertFalse({tuple(row) for row in result['X_train']} & {tuple(row) for row in result['X_test']})
        truth,pred=result['y_true'],result['prediction']
        cm=confusion_oracle(truth,pred)
        self.assertEqual(result['metrics']['confusion_matrix'],cm)
        (tn,fp),(fn,tp)=cm
        self.assertEqual(result['metrics']['alerts'],tp+fp)
        self.assertAlmostEqual(result['metrics']['precision'],tp/(tp+fp) if tp+fp else 0)
        self.assertAlmostEqual(result['metrics']['recall'],tp/(tp+fn))
        self.assertAlmostEqual(result['metrics']['f1'],2*tp/(2*tp+fp+fn))
        self.assertAlmostEqual(result['metrics']['false_positive_rate'],fp/(tn+fp))
        positive=[s for t,s in zip(truth,result['anomaly_score']) if t]
        negative=[s for t,s in zip(truth,result['anomaly_score']) if not t]
        auc=math.fsum((p>n)+.5*(p==n) for p in positive for n in negative)/(len(positive)*len(negative))
        self.assertAlmostEqual(result['metrics']['roc_auc'],auc,places=12)
        self.assertEqual(pred,[int(d<0) for d in result['decision_function']])
        print('SEED_RESULT '+json.dumps({'seed':seed,**result['metrics']},sort_keys=True))
    return test


for seed in range(100):
    setattr(SeededOracleChecks,f'test_seed_{seed:03d}',seeded_case(seed))


if __name__=='__main__':
    unittest.main(verbosity=2)
