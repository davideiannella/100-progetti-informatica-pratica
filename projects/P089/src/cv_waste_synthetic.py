"""Rifiuti disegnati da zero: nessuna foto reale e nessun dataset TrashNet."""
from __future__ import annotations
import json
import numbers
import numpy as np
from PIL import Image, ImageDraw
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split

CLASSES = ("carta", "plastica", "vetro", "metallo")
FEATURE_NAMES = ("mean_r", "mean_g", "mean_b", "std_r", "std_g", "std_b",
                 "edge_x", "edge_y", "q25_r", "q25_g", "q25_b", "q75_r", "q75_g", "q75_b")


def _integer(value, name, low, high):
    if isinstance(value, bool) or not isinstance(value, numbers.Integral) or not low <= value <= high:
        raise ValueError(f"{name}: intero tra {low} e {high} richiesto")
    return int(value)


def _threshold(value):
    if isinstance(value, bool) or not isinstance(value, numbers.Real):
        raise ValueError("min_confidence deve essere un numero finito tra zero e uno")
    try:
        value = float(value)
    except (ValueError, OverflowError) as exc:
        raise ValueError("min_confidence non finita") from exc
    if not np.isfinite(value) or not 0 <= value <= 1:
        raise ValueError("min_confidence deve essere tra zero e uno")
    return value


def _noise(rng, shape, scale=10):
    return rng.normal(0, scale, shape)


def synthetic_image(label: str, rng: np.random.Generator, size: int = 64) -> Image.Image:
    if not isinstance(label, str) or label not in CLASSES:
        raise ValueError("classe sconosciuta")
    if not isinstance(rng, np.random.Generator):
        raise ValueError("rng deve essere numpy.random.Generator")
    size = _integer(size, "size", 64, 256)
    bg = np.clip(np.ones((size, size, 3))*235 + _noise(rng,(size,size,3),5),0,255).astype(np.uint8)
    img = Image.fromarray(bg)
    d = ImageDraw.Draw(img, "RGBA")
    cx, cy = size//2 + int(rng.integers(-5,6)), size//2 + int(rng.integers(-5,6))
    if label == "carta":
        w,h = int(rng.integers(26,38)), int(rng.integers(30,44))
        d.rectangle((cx-w//2,cy-h//2,cx+w//2,cy+h//2), fill=(225,210,165,255), outline=(135,120,90,255), width=2)
        for k in range(-10,11,7): d.line((cx-w//3,cy+k,cx+w//3,cy+k), fill=(150,135,110,180), width=1)
    elif label == "plastica":
        d.rounded_rectangle((cx-13,cy-23,cx+13,cy+23), radius=9, fill=(65,145,225,230), outline=(20,80,145,255), width=2)
        d.rectangle((cx-5,cy-28,cx+5,cy-22), fill=(50,110,190,255))
    elif label == "vetro":
        d.ellipse((cx-17,cy-25,cx+17,cy+25), fill=(70,175,105,150), outline=(25,105,55,255), width=3)
        d.ellipse((cx-8,cy-15,cx+2,cy+10), fill=(220,255,230,100))
    elif label == "metallo":
        d.ellipse((cx-21,cy-21,cx+21,cy+21), fill=(155,160,168,255), outline=(70,75,85,255), width=3)
        d.ellipse((cx-12,cy-12,cx+12,cy+12), outline=(215,220,225,255), width=3)
    else:
        raise ValueError(label)
    return img



def features(img: Image.Image) -> np.ndarray:
    if not isinstance(img, Image.Image) or img.mode != "RGB" or min(img.size) < 2:
        raise ValueError("immagine RGB di almeno 2 x 2 pixel richiesta")
    a = np.asarray(img, dtype=np.float64) / 255.0
    mean = a.mean(axis=(0, 1))
    std = a.std(axis=(0, 1))
    gray = a.mean(axis=2)
    dx = np.abs(np.diff(gray, axis=1)).mean()
    dy = np.abs(np.diff(gray, axis=0)).mean()
    q25 = np.quantile(a, 0.25, axis=(0, 1))
    q75 = np.quantile(a, 0.75, axis=(0, 1))
    return np.concatenate([mean, std, [dx, dy], q25, q75]).astype(np.float64)


def build_dataset(samples_per_class=80, seed=123):
    samples_per_class = _integer(samples_per_class, "samples_per_class", 1, 1000)
    seed = _integer(seed, "seed", 0, 2**32 - 1)
    rng = np.random.default_rng(seed)
    X, y = [], []
    for label in CLASSES:
        for _ in range(samples_per_class):
            X.append(features(synthetic_image(label, rng)))
            y.append(label)
    return np.stack(X), np.asarray(y)


def classify_probabilities(probabilities, labels=CLASSES, min_confidence=0.75):
    min_confidence = _threshold(min_confidence)
    if (not isinstance(labels, (tuple, list)) or len(labels) != len(CLASSES)
            or any(not isinstance(label, str) for label in labels)
            or set(labels) != set(CLASSES)):
        raise ValueError("labels deve contenere ciascuna classe una volta")
    try:
        original = np.asarray(probabilities, dtype=object)
        if any(isinstance(value, (bool, np.bool_)) for value in original.flat):
            raise ValueError("i booleani non sono probabilità")
        p = np.asarray(probabilities)
    except (TypeError, ValueError) as exc:
        raise ValueError("vettore di probabilità non valido") from exc
    if (p.dtype.kind not in "iuf" or p.shape != (len(labels),)
            or not np.isfinite(p).all() or (p < 0).any() or (p > 1).any()
            or not np.isclose(p.sum(), 1.0, rtol=0, atol=1e-9)):
        raise ValueError("probabilità finite, non negative e con somma uno richieste")
    top = int(np.argmax(p))
    confidence = float(p[top])
    return {"label": labels[top], "confidence": confidence,
            "decision": "automatico" if confidence >= min_confidence else "revisione"}


def train_evaluate(samples_per_class=80, seed=123, min_confidence=0.75):
    samples_per_class = _integer(samples_per_class, "samples_per_class", 4, 1000)
    seed = _integer(seed, "seed", 0, 2**32 - 1)
    min_confidence = _threshold(min_confidence)
    X, y = build_dataset(samples_per_class, seed)
    train, test = train_test_split(np.arange(len(y)), test_size=0.25,
                                   random_state=seed, stratify=y)
    model = RandomForestClassifier(n_estimators=120, max_depth=10,
                                   random_state=seed, n_jobs=1)
    baseline = DummyClassifier(strategy="most_frequent")
    model.fit(X[train], y[train])
    baseline.fit(X[train], y[train])
    decisions = [classify_probabilities(p, model.classes_.tolist(), min_confidence)
                 for p in model.predict_proba(X[test])]
    pred = np.asarray([d["label"] for d in decisions])
    base_pred = baseline.predict(X[test])
    return {"dataset": "rifiuti_sintetici_disegnati", "seed": seed,
            "samples_per_class": samples_per_class, "feature_count": X.shape[1],
            "feature_names": list(FEATURE_NAMES), "classes": list(CLASSES),
            "train_samples": len(train), "test_samples": len(test),
            "train_indices": train.tolist(), "test_indices": test.tolist(),
            "accuracy": float(accuracy_score(y[test], pred)),
            "f1_macro": float(f1_score(y[test], pred, average="macro", zero_division=0)),
            "confusion_matrix": confusion_matrix(y[test], pred, labels=CLASSES).tolist(),
            "baseline": {"strategy": "most_frequent", "class": str(baseline.classes_[np.argmax(baseline.class_prior_)]),
                         "accuracy": float(accuracy_score(y[test], base_pred)),
                         "f1_macro": float(f1_score(y[test], base_pred, average="macro", zero_division=0)),
                         "confusion_matrix": confusion_matrix(y[test], base_pred, labels=CLASSES).tolist()},
            "min_confidence": min_confidence,
            "automatic_samples": sum(d["decision"] == "automatico" for d in decisions),
            "review_samples": sum(d["decision"] == "revisione" for d in decisions),
            "min_test_confidence": min(d["confidence"] for d in decisions), "model": model}


if __name__ == "__main__":
    result = train_evaluate()
    print(json.dumps({k: v for k, v in result.items() if k != "model"},
                     indent=2, ensure_ascii=False, allow_nan=False))
