"""Classificare palette sintetiche: NON un riconoscitore di rifiuti fotografati."""
import hashlib
import json
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

CLASSES = ("carta", "plastica", "vetro", "organico")
COLORS = {"carta": (220, 220, 210), "plastica": (40, 100, 220),
          "vetro": (60, 180, 100), "organico": (130, 80, 40)}

def _integer(value, name, low, high):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, np.integer)) or not low <= value <= high:
        raise ValueError(f"{name} deve essere intero tra {low} e {high}.")
    return int(value)

def make_image(label, seed, size=24, palette_shift=False):
    if not isinstance(label, str) or label not in CLASSES:
        raise ValueError("Classe sintetica sconosciuta.")
    seed = _integer(seed, "seed", 0, 2**63 - 1)
    size = _integer(size, "size", 2, 256)
    if not isinstance(palette_shift, bool):
        raise ValueError("palette_shift deve essere booleano.")
    rng = np.random.default_rng(seed)
    color_label = CLASSES[(CLASSES.index(label) + 1) % len(CLASSES)] if palette_shift else label
    base = np.array(COLORS[color_label], dtype=float) + rng.normal(0, 10, 3)
    return np.clip(base + rng.normal(0, 6, (size, size, 3)), 0, 255).astype(np.uint8)

def features(image):
    array = np.asarray(image)
    if array.ndim != 3 or array.shape[2] != 3 or min(array.shape[:2]) < 1:
        raise ValueError("Servono immagini RGB non vuote con forma (altezza, larghezza, 3).")
    if array.dtype != np.uint8:
        raise ValueError("I pixel devono avere dtype uint8, da 0 a 255; NaN/inf non ammessi.")
    normalized = array.astype(float) / 255.0
    return np.r_[normalized.mean(axis=(0, 1)), normalized.std(axis=(0, 1))]

def dataset(split, per_class, seed=78, palette_shift=False):
    if not isinstance(split, str) or split not in ("train", "test"):
        raise ValueError("split deve essere train o test.")
    per_class = _integer(per_class, "per_class", 1, 1000)
    seed = _integer(seed, "seed", 0, 2**31 - 1)
    rows, labels, ids, hashes = [], [], [], []
    for ci, label in enumerate(CLASSES):
        for i in range(per_class):
            image_seed = seed * 100000 + (0 if split == "train" else 10000) + ci * 1000 + i
            im = make_image(label, image_seed, palette_shift=palette_shift)
            rows.append(features(im)); labels.append(label)
            ids.append(f"{split}-{label}-{i:04d}")
            hashes.append(hashlib.sha256(im.tobytes()).hexdigest())
    return np.asarray(rows), np.asarray(labels), ids, hashes

def train_model(X, y):
    X, y = np.asarray(X), np.asarray(y)
    if X.ndim != 2 or X.shape[1] != 6 or X.shape[0] == 0 or X.dtype.kind not in "iuf":
        raise ValueError("X deve contenere sei feature numeriche per immagine.")
    if not np.isfinite(X).all() or (X < 0).any() or (X > 1).any():
        raise ValueError("Le feature devono essere finite e comprese tra zero e uno.")
    if y.ndim != 1 or len(y) != len(X) or set(y.tolist()) != set(CLASSES):
        raise ValueError("Etichette incoerenti o classi mancanti.")
    return make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000, random_state=78)).fit(X, y)

def _metrics(y, pred):
    return {"accuracy": float(accuracy_score(y, pred)),
            "f1_macro": float(f1_score(y, pred, labels=CLASSES, average="macro", zero_division=0)),
            "confusion_matrix": confusion_matrix(y, pred, labels=CLASSES).tolist()}

def experiment(seed=78):
    X, y, train_ids, train_hashes = dataset("train", 60, seed)
    Xtest, truth, test_ids, test_hashes = dataset("test", 25, seed)
    if set(train_ids) & set(test_ids) or set(train_hashes) & set(test_hashes):
        raise ValueError("Training e test condividono immagini.")
    model = train_model(X, y)
    pred = model.predict(Xtest)
    shifted, shifted_y, _, _ = dataset("test", 25, seed, palette_shift=True)
    shuffled_y = np.random.default_rng(seed).permutation(y)
    shuffled_model = train_model(X, shuffled_y)
    return {
        "dataset": "Immagini RGB 24x24 da quattro palette; nessuna fotografia di rifiuti",
        "seed": seed, "classes": list(CLASSES),
        "split": {"train": len(y), "test": len(truth), "hash_overlap": 0,
                  "train_ids": train_ids, "test_ids": test_ids},
        **_metrics(truth, pred),
        "baseline_accuracy": float(accuracy_score(truth, [CLASSES[0]] * len(truth))),
        "shifted_palette": _metrics(shifted_y, model.predict(shifted)),
        "shuffled_labels": _metrics(truth, shuffled_model.predict(Xtest)),
        "predictions": [{"id": i, "truth": str(t), "prediction": str(p)} for i, t, p in zip(test_ids, truth, pred)],
        "feature_names": ["media_R", "media_G", "media_B", "std_R", "std_G", "std_B"],
        "sample_features": Xtest[0].tolist(),
    }

if __name__ == "__main__":
    print(json.dumps(experiment(), ensure_ascii=False, indent=2, allow_nan=False))
