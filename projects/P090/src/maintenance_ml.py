"""Classificazione di finestre sintetiche, non previsione del tempo al guasto."""
import hashlib
import json
import numbers
import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

SAMPLE_RATE_HZ = 256
WINDOW_SAMPLES = 256
FEATURE_NAMES = ("rms_au", "peak_au", "crest_factor", "high_frequency_ratio")


def _seed(seed):
    if isinstance(seed, bool) or not isinstance(seed, numbers.Integral) or not 0 <= seed < 2**32:
        raise ValueError("seed deve essere un intero tra 0 e 2**32-1")
    return int(seed)


def _finite_real(value, name):
    if isinstance(value, bool) or not isinstance(value, numbers.Real):
        raise ValueError(f"{name}: numero reale richiesto")
    try:
        value = float(value)
    except (ValueError, OverflowError) as exc:
        raise ValueError(f"{name}: numero non finito") from exc
    if not np.isfinite(value):
        raise ValueError(f"{name}: numero non finito")
    return value


def features(signal, sample_rate_hz=SAMPLE_RATE_HZ):
    sample_rate_hz = _finite_real(sample_rate_hz, "sample_rate_hz")
    if sample_rate_hz <= 80:
        raise ValueError("frequenza di campionamento maggiore di 80 Hz richiesta")
    try:
        original = np.asarray(signal, dtype=object)
        if any(isinstance(value, (bool, np.bool_)) for value in original.flat):
            raise ValueError("i booleani non sono campioni")
        raw = np.asarray(signal)
    except (TypeError, ValueError) as exc:
        raise ValueError("segnale non valido") from exc
    if raw.dtype.kind not in "iuf" or raw.ndim != 1 or len(raw) < 8:
        raise ValueError("segnale reale monodimensionale con almeno 8 campioni richiesto")
    x = raw.astype(np.float64)
    if not np.isfinite(x).all():
        raise ValueError("il segnale contiene valori non finiti")
    peak = float(np.max(np.abs(x)))
    if peak == 0:
        return np.zeros(4, dtype=np.float64)
    normalized = x / peak
    normalized_rms = float(np.sqrt(np.mean(normalized**2)))
    rms = peak * normalized_rms
    if rms == 0:
        raise ValueError("RMS non rappresentabile in float64")
    crest = 1 / normalized_rms
    centered = normalized - normalized.mean()
    power = np.abs(np.fft.rfft(centered))**2
    weights = np.full(len(power), 2.0)
    weights[0] = 1.0
    if len(x) % 2 == 0:
        weights[-1] = 1.0
    power *= weights
    frequencies = np.fft.rfftfreq(len(x), d=1 / sample_rate_hz)
    total = float(power.sum())
    high_ratio = float(power[frequencies >= 40].sum() / total) if total else 0.0
    return np.array([rms, peak, crest, high_ratio], dtype=np.float64)


def generate_signal(label, rng):
    if isinstance(label, bool) or not isinstance(label, numbers.Integral) or label not in (0, 1):
        raise ValueError("label deve essere 0 o 1")
    if not isinstance(rng, np.random.Generator):
        raise ValueError("rng deve essere numpy.random.Generator")
    t = np.arange(WINDOW_SAMPLES) / SAMPLE_RATE_HZ
    amplitude = rng.uniform(0.8, 1.5)
    phase = rng.uniform(0, 2 * np.pi)
    noise = rng.normal(0, rng.uniform(0.15, 0.5), WINDOW_SAMPLES)
    high_amplitude = rng.uniform(0.10, 0.55) if label else rng.uniform(0, 0.25)
    signal = amplitude * np.sin(2 * np.pi * 16 * t + phase) + noise
    signal += high_amplitude * np.sin(2 * np.pi * 64 * t + phase)
    if label:
        locations = rng.choice(WINDOW_SAMPLES, size=2, replace=False)
        signal[locations] += rng.uniform(0.5, 2.0, 2)
    return signal


def build_signals(seed=9):
    rng = np.random.default_rng(_seed(seed))
    labels = np.array([0] * 180 + [1] * 60, dtype=int)
    signals = np.stack([generate_signal(int(label), rng) for label in labels])
    return signals, labels


def _metrics(expected, predicted):
    return {"accuracy": float(accuracy_score(expected, predicted)),
            "precision": float(precision_score(expected, predicted, zero_division=0)),
            "recall": float(recall_score(expected, predicted, zero_division=0)),
            "f1": float(f1_score(expected, predicted, zero_division=0)),
            "confusion_matrix": confusion_matrix(expected, predicted, labels=[0, 1]).tolist()}


def experiment(seed=9, attention_threshold=0.5):
    seed = _seed(seed)
    attention_threshold = _finite_real(attention_threshold, "attention_threshold")
    if not 0 < attention_threshold <= 1:
        raise ValueError("attention_threshold deve essere finita in (0, 1]")
    signals, y = build_signals(seed)
    X = np.stack([features(signal) for signal in signals])
    train, test = train_test_split(np.arange(len(y)), test_size=0.25,
                                   random_state=seed, stratify=y)
    model = make_pipeline(StandardScaler(), LogisticRegression(C=1, max_iter=1000,
                                                                random_state=seed))
    baseline = DummyClassifier(strategy="most_frequent")
    model.fit(X[train], y[train])
    baseline.fit(X[train], y[train])
    probabilities = model.predict_proba(X[test])[:, 1]
    pred = (probabilities >= attention_threshold).astype(int)
    result = _metrics(y[test], pred)
    result.update({"dataset": "finestre_indipendenti_sintetiche", "seed": seed,
                   "sample_rate_hz": SAMPLE_RATE_HZ, "window_samples": WINDOW_SAMPLES,
                   "feature_names": list(FEATURE_NAMES), "attention_threshold": float(attention_threshold),
                   "train_samples": len(train), "test_samples": len(test),
                   "train_indices": train.tolist(), "test_indices": test.tolist(),
                   "train_class_counts": np.bincount(y[train], minlength=2).tolist(),
                   "test_class_counts": np.bincount(y[test], minlength=2).tolist(),
                   "signal_sha256": [hashlib.sha256(s.tobytes()).hexdigest() for s in signals],
                   "baseline": _metrics(y[test], baseline.predict(X[test])), "model": model})
    return result


if __name__ == "__main__":
    result = experiment()
    print(json.dumps({k: v for k, v in result.items() if k != "model"},
                     ensure_ascii=False, indent=2, allow_nan=False))
