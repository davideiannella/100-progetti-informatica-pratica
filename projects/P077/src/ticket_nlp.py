"""Ticket inventati, holdout distinto, nessuna promessa sul mondo reale."""
import json
import re
import unicodedata
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.pipeline import Pipeline

CLASSES = ("accesso", "fatturazione", "tecnico")
# Testi originali del laboratorio: non sono conversazioni di clienti.
TRAIN_DATA = (
    ("a01", "non riesco ad accedere account password", "accesso"),
    ("a02", "login bloccato credenziali errate", "accesso"),
    ("a03", "reset password utente", "accesso"),
    ("a04", "codice autenticazione non ricevuto per accesso", "accesso"),
    ("a05", "account sospeso impossibile entrare", "accesso"),
    ("a06", "recuperare password dimenticata", "accesso"),
    ("a07", "autenticazione a due fattori fallita", "accesso"),
    ("a08", "credenziali scadute per login", "accesso"),
    ("f01", "fattura errata importo pagamento", "fatturazione"),
    ("f02", "non trovo la fattura del mese", "fatturazione"),
    ("f03", "addebito duplicato in fattura", "fatturazione"),
    ("f04", "pagamento abbonamento rifiutato", "fatturazione"),
    ("f05", "richiesta rimborso addebito", "fatturazione"),
    ("f06", "importo totale fattura sbagliato", "fatturazione"),
    ("f07", "ricevuta del pagamento non disponibile", "fatturazione"),
    ("f08", "modificare indirizzo di fatturazione", "fatturazione"),
    ("t01", "applicazione lenta e si blocca", "tecnico"),
    ("t02", "errore server durante salvataggio", "tecnico"),
    ("t03", "pagina non carica errore rete", "tecnico"),
    ("t04", "crash applicazione durante esportazione", "tecnico"),
    ("t05", "connessione rete interrotta", "tecnico"),
    ("t06", "schermata vuota dopo aggiornamento", "tecnico"),
    ("t07", "salvataggio documento restituisce errore", "tecnico"),
    ("t08", "server lento e caricamento infinito", "tecnico"),
)
TEST_DATA = (
    ("ha01", "ho dimenticato la password del mio account", "accesso"),
    ("ha02", "non arriva il codice per autenticazione", "accesso"),
    ("ha03", "le credenziali impediscono il login", "accesso"),
    ("ha04", "devo entrare ma account sospeso", "accesso"),
    ("hf01", "il pagamento ha un importo diverso dalla fattura", "fatturazione"),
    ("hf02", "vorrei rimborso per addebito doppio", "fatturazione"),
    ("hf03", "dove recupero la ricevuta del pagamento", "fatturazione"),
    ("hf04", "correggere indirizzo sulla fattura", "fatturazione"),
    ("ht01", "il server risponde lentamente durante salvataggio", "tecnico"),
    ("ht02", "dopo aggiornamento vedo schermata bianca", "tecnico"),
    ("ht03", "la connessione cade e la pagina non carica", "tecnico"),
    ("ht04", "crash durante esportazione del documento", "tecnico"),
)

def normalize_text(text):
    if not isinstance(text, str) or len(text) > 5000:
        raise ValueError("Il ticket deve essere una stringa entro 5000 caratteri.")
    value = " ".join(unicodedata.normalize("NFKC", text).casefold().split())
    if not value or not any(len(t) >= 2 and any(c.isalpha() for c in t)
                            for t in re.findall(r"\w+", value)):
        raise ValueError("Serve almeno una parola di due caratteri.")
    return value

def validate_rows(rows):
    if not isinstance(rows, (tuple, list)) or not rows:
        raise ValueError("Servono righe (id, testo, classe) non vuote.")
    ids, texts, clean = set(), set(), []
    for row in rows:
        if not isinstance(row, (tuple, list)) or len(row) != 3:
            raise ValueError("Ogni riga deve avere id, testo e classe.")
        identity, text, label = row
        if not isinstance(identity, str) or not identity.strip() or identity != identity.strip():
            raise ValueError("ID non valido.")
        if not isinstance(label, str) or label not in CLASSES:
            raise ValueError("Classe sconosciuta.")
        clean_text = normalize_text(text)
        token_key = tuple(re.findall(r"(?u)\b\w\w+\b", clean_text))
        if identity in ids or token_key in texts:
            raise ValueError("ID o testo duplicato dopo normalizzazione.")
        ids.add(identity); texts.add(token_key)
        clean.append((identity, clean_text, label))
    return clean

def validate_split(train, test):
    train, test = validate_rows(train), validate_rows(test)
    if {r[0] for r in train} & {r[0] for r in test}:
        raise ValueError("Leakage: ID condiviso tra training e test.")
    train_keys = {tuple(re.findall(r"(?u)\b\w\w+\b", r[1])) for r in train}
    test_keys = {tuple(re.findall(r"(?u)\b\w\w+\b", r[1])) for r in test}
    if train_keys & test_keys:
        raise ValueError("Leakage: testo condiviso tra training e test dopo tokenizzazione.")
    return train, test

def train_model(rows=TRAIN_DATA):
    clean = validate_rows(rows)
    if set(r[2] for r in clean) != set(CLASSES):
        raise ValueError("Il training deve contenere tutte e tre le classi.")
    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
        ("clf", LogisticRegression(max_iter=1000, random_state=77)),
    ])
    model.fit([r[1] for r in clean], [r[2] for r in clean])
    return model

def classify(model, text):
    text = normalize_text(text)
    if model.named_steps["tfidf"].transform([text]).nnz == 0:
        return {"label": None, "reason": "nessun_termine_noto"}
    return {"label": str(model.predict([text])[0]), "reason": "classificato"}

def experiment(train=TRAIN_DATA, test=TEST_DATA):
    train, test = validate_split(train, test)
    model = train_model(train)
    truth = [r[2] for r in test]
    pred = model.predict([r[1] for r in test]).tolist()
    counts = Counter(r[2] for r in train)
    majority = sorted(counts, key=lambda c: (-counts[c], c))[0]
    return {
        "dataset": f"{len(train) + len(test)} ticket inventati manualmente; nessun dato cliente",
        "split": {"train": len(train), "test": len(test), "text_overlap": 0,
                  "train_ids": [r[0] for r in train], "test_ids": [r[0] for r in test]},
        "classes": list(CLASSES), "accuracy": float(accuracy_score(truth, pred)),
        "f1_macro": float(f1_score(truth, pred, labels=CLASSES, average="macro", zero_division=0)),
        "baseline_accuracy": float(accuracy_score(truth, [majority] * len(test))),
        "confusion_matrix": confusion_matrix(truth, pred, labels=CLASSES).tolist(),
        "predictions": [{"id": r[0], "text": r[1], "truth": r[2], "prediction": p}
                        for r, p in zip(test, pred)],
        "example": {"input": "ho dimenticato la password", **classify(model, "ho dimenticato la password")},
        "oov_example": classify(model, "astronave quantistica"),
    }

if __name__ == "__main__":
    print(json.dumps(experiment(), ensure_ascii=False, indent=2, allow_nan=False))
