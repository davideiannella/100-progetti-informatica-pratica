"""Isolation Forest: training normale e test indipendente entrambi sintetici."""
from numbers import Integral, Real
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support, roc_auc_score


def _integer(v, name, minimum=0):
    if isinstance(v, (bool, np.bool_)) or not isinstance(v, Integral) or v < minimum:
        raise ValueError(f'{name}: atteso intero >= {minimum}')
    return int(v)


def _matrix(X):
    a = np.asarray(X, dtype=float)
    if a.ndim != 2 or a.shape[1] != 2 or not len(a) or not np.isfinite(a).all():
        raise ValueError('X: matrice finita non vuota con 2 colonne')
    return a


def make_splits(seed=21, n_train=300, n_normal_test=100, n_anomalous_test=30):
    seed = _integer(seed, 'seed')
    sizes = [_integer(n_train, 'n_train', 2), _integer(n_normal_test, 'n_normal_test', 1),
             _integer(n_anomalous_test, 'n_anomalous_test', 1)]
    train_rng, test_rng = [np.random.default_rng(s) for s in np.random.SeedSequence(seed).spawn(2)]
    train = train_rng.normal([50, 3], [10, 1], size=(sizes[0], 2))
    normal = test_rng.normal([50, 3], [10, 1], size=(sizes[1], 2))
    unusual = test_rng.normal([150, 15], [12, 2], size=(sizes[2], 2))
    test = np.vstack([normal, unusual])
    labels = np.r_[np.zeros(sizes[1], int), np.ones(sizes[2], int)]
    permutation = test_rng.permutation(len(test))
    return {'X_train': train, 'X_test': test[permutation], 'y_test': labels[permutation],
            'train_ids': np.arange(sizes[0]), 'test_ids': np.arange(sizes[0], sum(sizes))[permutation]}


def train_model(X_train, seed=21, contamination=0.07):
    X_train = _matrix(X_train)
    if len(X_train) < 2:
        raise ValueError('servono almeno 2 esempi di training')
    seed = _integer(seed, 'seed')
    if seed > 2**32 - 1:
        raise ValueError('seed deve essere <= 2**32-1')
    if (isinstance(contamination, bool)
            or not isinstance(contamination, Real)
            or not np.isfinite(contamination)
            or not 0 < contamination <= 0.5):
        raise ValueError('contamination deve essere finita in (0,0.5]')
    return IsolationForest(
        n_estimators=100, contamination=contamination,
        random_state=seed, n_jobs=1,
    ).fit(X_train)


def predict(model, X):
    a = _matrix(X)
    return (model.predict(a) == -1).astype(int)


def detection_metrics(y_true, prediction, scores=None):
    truth, pred = np.asarray(y_true), np.asarray(prediction)
    if truth.ndim != 1 or not len(truth) or pred.shape != truth.shape:
        raise ValueError('etichette e predizioni: vettori non vuoti di uguale lunghezza')
    if not np.isin(truth, [0, 1]).all() or not np.isin(pred, [0, 1]).all():
        raise ValueError('etichette e predizioni devono essere 0 o 1')
    precision, recall, f1, _ = precision_recall_fscore_support(truth, pred, average='binary', zero_division=0)
    cm = confusion_matrix(truth, pred, labels=[0, 1])
    tn, fp, fn, tp = cm.ravel()
    auc = None
    if scores is not None:
        score = np.asarray(scores, dtype=float)
        if score.shape != truth.shape or not np.isfinite(score).all():
            raise ValueError('scores: un valore finito per riga')
        if len(np.unique(truth)) == 2:
            auc = float(roc_auc_score(truth, score))
    return {'precision': float(precision), 'recall': float(recall), 'f1': float(f1),
            'false_positive_rate': float(fp / (tn + fp)) if tn + fp else None,
            'alerts': int(pred.sum()), 'confusion_matrix': cm.tolist(), 'roc_auc': auc}


def run_experiment(seed=21):
    split = make_splits(seed)
    model = train_model(split['X_train'], seed)
    prediction = predict(model, split['X_test'])
    # Punteggio maggiore = esempio più anomalo; decision_function usa il verso opposto.
    scores = -model.score_samples(split['X_test'])
    return {'seed': int(seed), 'train_ids': split['train_ids'].tolist(), 'test_ids': split['test_ids'].tolist(),
            'X_train': split['X_train'].tolist(), 'X_test': split['X_test'].tolist(),
            'y_true': split['y_test'].tolist(), 'prediction': prediction.tolist(), 'anomaly_score': scores.tolist(),
            'decision_function': model.decision_function(split['X_test']).tolist(),
            'metrics': detection_metrics(split['y_test'], prediction, scores),
            'baseline_metrics': detection_metrics(split['y_test'], np.zeros(len(prediction), int)),
            'learned_offset': float(model.offset_), 'contamination': 0.07, 'n_estimators': 100}


def experiment(seed=21):
    return run_experiment(seed)['metrics']


def main():
    r = run_experiment()
    print('P075 — 300 normali in training; test indipendente: 100 normali e 30 anomalie')
    for key in ('precision', 'recall', 'f1', 'false_positive_rate', 'roc_auc'):
        print(f"{key}: {r['metrics'][key]:.6f}")
    print('alerts:', r['metrics']['alerts'])
    print('matrice [[TN, FP], [FN, TP]]:', r['metrics']['confusion_matrix'])
    print('offset appreso:', f"{r['learned_offset']:.6f}")
    print('baseline senza allarmi: recall 0.000000; f1 0.000000')


if __name__ == '__main__':
    main()
