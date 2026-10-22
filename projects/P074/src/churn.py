"""Classificazione binaria su clienti immaginari, senza dati personali."""
from numbers import Integral, Real
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, brier_score_loss, confusion_matrix,
                             log_loss, precision_recall_fscore_support, roc_auc_score)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def _integer(v, name, minimum=0):
    if isinstance(v, (bool, np.bool_)) or not isinstance(v, Integral) or v < minimum:
        raise ValueError(f'{name}: atteso intero >= {minimum}')
    return int(v)


def _matrix(X):
    a = np.asarray(X, dtype=float)
    if a.ndim != 2 or a.shape[1] != 3 or not len(a) or not np.isfinite(a).all():
        raise ValueError('X: matrice finita non vuota con 3 colonne')
    if (a < 0).any() or (a[:, 0] < 1).any() or not np.equal(a[:, :2], np.floor(a[:, :2])).all():
        raise ValueError('mesi interi >= 1, ticket interi >= 0, utilizzo >= 0')
    return a


def _labels(y, n):
    a = np.asarray(y)
    if a.shape != (n,) or not np.isin(a, [0, 1]).all():
        raise ValueError('y: un valore 0 o 1 per riga')
    return a.astype(int)


def data(n=500, seed=11):
    n, seed = _integer(n, 'n', 4), _integer(seed, 'seed')
    rng = np.random.default_rng(seed)
    months = rng.integers(1, 49, n)
    tickets = rng.poisson(2, n)
    usage = rng.normal(50, 15, n).clip(0)
    logit = -0.5 - 0.02 * months + 0.45 * tickets - 0.005 * usage
    prob = 1 / (1 + np.exp(-logit))
    y = (rng.random(n) < prob).astype(int)
    return np.column_stack([months, tickets, usage]), y


def train_model(X_train, y_train):
    X_train = _matrix(X_train)
    y_train = _labels(y_train, len(X_train))
    if len(np.unique(y_train)) != 2:
        raise ValueError('il training richiede entrambe le classi')
    model = make_pipeline(
        StandardScaler(),
        LogisticRegression(C=1.0, max_iter=1000, random_state=0),
    )
    return model.fit(X_train, y_train)


def predict_probability(model, X):
    return model.predict_proba(_matrix(X))[:, 1]


def classification_metrics(y_true, probability, threshold=0.5):
    prob = np.asarray(probability, dtype=float)
    if prob.ndim != 1 or not len(prob) or not np.isfinite(prob).all() or ((prob < 0) | (prob > 1)).any():
        raise ValueError('probability: vettore finito non vuoto in [0,1]')
    if isinstance(threshold, bool) or not isinstance(threshold, Real) or not np.isfinite(threshold) or not 0 <= threshold <= 1:
        raise ValueError('threshold deve essere finita in [0,1]')
    truth = _labels(y_true, len(prob))
    pred = (prob >= threshold).astype(int)
    precision, recall, f1, _ = precision_recall_fscore_support(truth, pred, average='binary', zero_division=0)
    return {'accuracy': float(accuracy_score(truth, pred)), 'precision': float(precision),
            'recall': float(recall), 'f1': float(f1), 'positive_rate': float(truth.mean()),
            'brier': float(brier_score_loss(truth, prob)), 'log_loss': float(log_loss(truth, prob, labels=[0, 1])),
            'roc_auc': float(roc_auc_score(truth, prob)) if len(np.unique(truth)) == 2 else None,
            'confusion_matrix': confusion_matrix(truth, pred, labels=[0, 1]).tolist()}


def run_experiment(seed=11, n=500, cut=380):
    X, y = data(n, seed)
    cut = _integer(cut, 'cut', 2)
    if cut > len(X) - 2:
        raise ValueError('servono almeno 2 esempi di test')
    train_ids, test_ids = np.arange(cut), np.arange(cut, len(X))
    model = train_model(X[train_ids], y[train_ids])
    prob = predict_probability(model, X[test_ids])
    baseline_prob = np.full(len(test_ids), y[train_ids].mean())
    estimator = model.named_steps['logisticregression']
    scaler = model.named_steps['standardscaler']
    return {'seed': int(seed), 'train_ids': train_ids.tolist(), 'test_ids': test_ids.tolist(),
            'y_true': y[test_ids].tolist(), 'probability': prob.tolist(), 'prediction': (prob >= 0.5).astype(int).tolist(),
            'metrics': classification_metrics(y[test_ids], prob),
            'baseline_metrics': classification_metrics(y[test_ids], baseline_prob),
            'baseline_train_prevalence': float(y[train_ids].mean()),
            'threshold': 0.5, 'scaler_mean': scaler.mean_.tolist(),
            'scaler_scale': scaler.scale_.tolist(), 'learned_coefficients_standardized': estimator.coef_[0].tolist(),
            'learned_intercept_standardized': float(estimator.intercept_[0])}


def experiment(seed=11, n=500, cut=380):
    return run_experiment(seed, n, cut)['metrics']


def main():
    r = run_experiment()
    print('P074 — 380 esempi di training; 120 esempi di test sintetici; soglia 0.5')
    for key in ('accuracy', 'precision', 'recall', 'f1', 'brier', 'log_loss', 'roc_auc'):
        print(f"{key}: {r['metrics'][key]:.6f}")
    print('matrice [[TN, FP], [FN, TP]]:', r['metrics']['confusion_matrix'])
    print('baseline_accuracy:', f"{r['baseline_metrics']['accuracy']:.6f}")
    print('baseline_brier:', f"{r['baseline_metrics']['brier']:.6f}")
    print('prima probabilità:', f"{r['probability'][0]:.6f}", 'etichetta:', r['y_true'][0])


if __name__ == '__main__':
    main()
