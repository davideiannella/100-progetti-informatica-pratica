"""Regressione didattica su dati sintetici; non stima consumi reali."""
import json
from numbers import Integral, Real
import numpy as np
from sklearn.linear_model import LinearRegression


def _integer(value, name, minimum=0):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, Integral) or value < minimum:
        raise ValueError(f'{name}: atteso intero >= {minimum}')
    return int(value)


def _matrix(X):
    a = np.asarray(X, dtype=float)
    if a.ndim != 2 or a.shape[1] != 3 or len(a) == 0 or not np.isfinite(a).all():
        raise ValueError('X: matrice finita non vuota con 3 colonne')
    if not np.isin(a[:, 1], [0, 1]).all():
        raise ValueError('occupazione deve essere 0 o 1')
    hours = a[:, 2]
    if not ((hours >= 0) & (hours <= 23) & (hours == np.floor(hours))).all():
        raise ValueError('ora deve essere un intero fra 0 e 23')
    return a


def _targets(y, n):
    a = np.asarray(y, dtype=float)
    if a.shape != (n,) or not np.isfinite(a).all():
        raise ValueError('y: un valore finito per riga')
    return a


def make_data(n=240, seed=7, noise=1.2):
    n = _integer(n, 'n', 8)
    seed = _integer(seed, 'seed')
    if isinstance(noise, bool) or not isinstance(noise, Real) or not np.isfinite(noise) or noise < 0:
        raise ValueError('noise: deviazione standard finita non negativa')
    rng = np.random.default_rng(seed)
    temp = rng.uniform(0, 35, n)
    occupied = rng.integers(0, 2, n)
    hour = rng.integers(0, 24, n)
    y = 18 + 0.8 * np.abs(temp - 20) + 8 * occupied + 0.08 * hour + rng.normal(0, noise, n)
    return np.column_stack([temp, occupied, hour]), y


def design_matrix(X):
    """Caratteristica fissata prima del test: nessuna stima."""
    a = _matrix(X)
    return np.column_stack([np.abs(a[:, 0] - 20), a[:, 1], a[:, 2]])


def train_model(X_train, y_train):
    X_train = design_matrix(X_train)
    if len(X_train) < 4:
        raise ValueError('servono almeno 4 esempi per il training')
    y_train = _targets(y_train, len(X_train))
    return LinearRegression().fit(X_train, y_train)


def predict(model, X):
    return model.predict(design_matrix(X))


def regression_metrics(y_true, y_pred):
    truth = np.asarray(y_true, dtype=float)
    if truth.ndim != 1 or not len(truth):
        raise ValueError('y_true deve essere un vettore non vuoto')
    truth = _targets(truth, len(truth))
    pred = _targets(y_pred, len(truth))
    errors = truth - pred
    return {'mae': float(np.mean(np.abs(errors))), 'rmse': float(np.sqrt(np.mean(errors ** 2)))}


def run_experiment(seed=7, n=240, cut=180):
    X, y = make_data(n=n, seed=seed)
    cut = _integer(cut, 'cut', 4)
    if cut > len(X) - 2:
        raise ValueError('servono almeno 2 esempi di test')
    train_ids, test_ids = np.arange(cut), np.arange(cut, len(X))
    model = train_model(X[train_ids], y[train_ids])
    pred = predict(model, X[test_ids])
    baseline = np.full(len(test_ids), y[train_ids].mean())
    metrics = regression_metrics(y[test_ids], pred)
    metrics.update({'baseline_' + k: v for k, v in regression_metrics(y[test_ids], baseline).items()})
    raw = LinearRegression().fit(X[train_ids], y[train_ids]).predict(X[test_ids])
    metrics['raw_temperature_mae'] = regression_metrics(y[test_ids], raw)['mae']
    return {'seed': int(seed), 'train_ids': train_ids.tolist(), 'test_ids': test_ids.tolist(),
            'X_test': X[test_ids].tolist(), 'y_true': y[test_ids].tolist(),
            'y_pred': pred.tolist(), 'baseline_predictions': baseline.tolist(), 'metrics': metrics,
            'learned_intercept': float(model.intercept_), 'learned_coefficients': model.coef_.tolist(),
            'feature_names': ['abs(temperatura-20)', 'occupazione', 'ora']}


def experiment(seed=7, n=240, cut=180):
    return run_experiment(seed=seed, n=n, cut=cut)['metrics']


def main():
    r = run_experiment()
    print('P073 — 180 esempi di training; 60 esempi di test sintetici')
    for key, value in r['metrics'].items():
        print(f'{key}: {value:.6f}')
    print('intercetta:', f"{r['learned_intercept']:.6f}")
    print('coefficienti:', ', '.join(f'{v:.6f}' for v in r['learned_coefficients']))
    print('prima previsione:', f"{r['y_pred'][0]:.6f}", 'vero:', f"{r['y_true'][0]:.6f}")


if __name__ == '__main__':
    main()
