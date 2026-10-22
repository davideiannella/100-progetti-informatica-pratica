"""Domanda sintetica: rolling a un passo e previsione ricorsiva sono contratti diversi."""
import json
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def _integer(value, name, low, high):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, np.integer)) or not low <= value <= high:
        raise ValueError(f"{name} deve essere intero tra {low} e {high}.")
    return int(value)

def series(n=240, seed=5):
    n = _integer(n, "n", 8, 1000000)
    seed = _integer(seed, "seed", 0, 2**63 - 1)
    rng = np.random.default_rng(seed)
    t = np.arange(n)
    return np.maximum(0, 50 + 0.08 * t + 8 * np.sin(2 * np.pi * t / 7) + rng.normal(0, 2, n))

def validate_series(values, minimum=8):
    try:
        values = np.asarray(values)
    except (TypeError, ValueError) as exc:
        raise ValueError("Serie numerica monodimensionale richiesta.") from exc
    if values.ndim != 1 or len(values) < minimum or values.dtype.kind not in "iuf":
        raise ValueError(f"Servono almeno {minimum} osservazioni numeriche in ordine giornaliero.")
    values = values.astype(float)
    if not np.isfinite(values).all() or (values < 0).any() or (values > 1e9).any():
        raise ValueError("Domanda finita nell'intervallo 0..1e9 richiesta; dati mancanti non imputati.")
    return values

def make_supervised(values):
    y = validate_series(values)
    times = np.arange(7, len(y))
    X = np.column_stack([y[times - 1], y[times - 7], times])
    return X, y[times].copy(), times

def fit_history(history):
    history = validate_series(history, minimum=21)
    X, y, _ = make_supervised(history)
    return LinearRegression().fit(X, y)

def evaluate_one_step(values, cut=180, stop=None):
    y = validate_series(values, minimum=22)
    cut = _integer(cut, "cut", 21, len(y) - 1)
    stop = len(y) if stop is None else _integer(stop, "stop", cut + 1, len(y))
    model = fit_history(y[:cut])
    times = np.arange(cut, stop)
    # A t osserviamo fino a t-1; i target del test precedenti sono ora disponibili.
    X = np.column_stack([y[times - 1], y[times - 7], times])
    prediction = np.maximum(0, model.predict(X))
    actual, last, week = y[times], y[times - 1], y[times - 7]
    return {
        "protocol": "rolling_one_step_frozen_model",
        "train_time_indices": list(range(7, cut)), "test_time_indices": times.tolist(),
        "train_observations": cut, "train_samples": cut - 7, "test_samples": stop - cut,
        "actual": actual.tolist(), "predicted": prediction.tolist(),
        "naive_last": last.tolist(), "naive_week": week.tolist(),
        "mae": float(mean_absolute_error(actual, prediction)),
        "baseline_mae": float(mean_absolute_error(actual, last)),
        "seasonal_mae": float(mean_absolute_error(actual, week)),
    }

def forecast_recursive(history, horizon):
    history = validate_series(history, minimum=21)
    horizon = _integer(horizon, "horizon", 1, 365)
    model = fit_history(history)
    extended = history.tolist()
    predictions = []
    for _ in range(horizon):
        t = len(extended)
        value = max(0.0, float(model.predict([[extended[t - 1], extended[t - 7], t]])[0]))
        if not np.isfinite(value) or value > 1e9:
            raise ValueError("Previsione ricorsiva fuori intervallo: ridurre l'orizzonte o cambiare modello.")
        predictions.append(value); extended.append(value)
    return np.asarray(predictions)

def experiment(seed=5):
    y = series(seed=seed)
    holdout = evaluate_one_step(y, cut=180)
    recursive = forecast_recursive(y[:180], 60)
    folds = [evaluate_one_step(y, cut=cut, stop=cut + 40) for cut in (120, 160, 200)]
    return {
        "dataset": "240 giorni sintetici; trend 0.08, stagionalità 7 giorni, rumore N(0,2)",
        "seed": seed, "time_indices": list(range(len(y))), "series": y.tolist(),
        **holdout,
        "recursive": {"origin": 180, "horizon": 60, "predicted": recursive.tolist(),
                      "mae": float(mean_absolute_error(y[180:], recursive))},
        "backtest_folds": folds,
    }

if __name__ == "__main__":
    print(json.dumps(experiment(), ensure_ascii=False, indent=2, allow_nan=False))
