"""Retrieval TF-IDF e risposta estrattiva con astensione. Nessun modello generativo."""
import json
import math
import numbers
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DOCS = (
    ("reti", "DNS traduce nomi di dominio in indirizzi IP."),
    ("db", "Una chiave esterna collega una riga a una chiave di un’altra relazione."),
    ("security", "Le query parametrizzate separano il codice SQL dai dati dell’utente."),
    ("cloud", "Un health check consente di valutare se un’istanza è disponibile per ricevere traffico."),
)
STOP_WORDS = ["a", "ad", "al", "alla", "che", "come", "con", "cosa", "da", "dal", "dai", "del",
              "della", "di", "e", "è", "gli", "i", "il", "in", "la", "le", "lo", "mi", "nel",
              "per", "quale", "quali", "se", "si", "su", "un", "una", "uno"]
ABSTENTION = "Non ho una fonte sufficientemente pertinente e univoca nel corpus."

def _text(value, maximum, allow_empty=False):
    if not isinstance(value, str) or len(value) > maximum:
        raise ValueError(f"Testo richiesto, massimo {maximum} caratteri.")
    value = " ".join(value.split())
    if not value and not allow_empty:
        raise ValueError("Testo vuoto non ammesso nel corpus.")
    return value

class MiniRAG:
    """Nome storico del progetto; implementa solo retrieval ed estrazione."""
    def __init__(self, docs=DOCS, min_score=0.15, min_margin=0.05):
        for value in (min_score, min_margin):
            if isinstance(value, bool) or not isinstance(value, numbers.Real) or not math.isfinite(value) or not 0 <= value <= 1:
                raise ValueError("Soglie finite tra zero e uno richieste.")
        if not isinstance(docs, (list, tuple)) or not docs:
            raise ValueError("Il corpus deve contenere almeno un documento.")
        clean, ids = [], set()
        for row in docs:
            if not isinstance(row, (list, tuple)) or len(row) != 2:
                raise ValueError("Servono coppie (id, testo).")
            identity = _text(row[0], 100)
            if identity in ids:
                raise ValueError("ID di fonte duplicato.")
            ids.add(identity); clean.append((identity, _text(row[1], 20000)))
        self.docs = tuple(clean)
        self.min_score, self.min_margin = float(min_score), float(min_margin)
        self.vec = TfidfVectorizer(stop_words=STOP_WORDS)
        try:
            self.X = self.vec.fit_transform([t for _, t in self.docs])
        except ValueError as exc:
            raise ValueError("Il corpus non contiene termini indicizzabili.") from exc

    def retrieve(self, query, k=2):
        query = _text(query, 2000, allow_empty=True)
        if isinstance(k, bool) or not isinstance(k, numbers.Integral) or k < 1:
            raise ValueError("k deve essere un intero positivo.")
        q = self.vec.transform([query])
        if q.nnz == 0:
            return []
        scores = cosine_similarity(q, self.X)[0]
        order = sorted(range(len(self.docs)), key=lambda i: (-float(scores[i]), self.docs[i][0]))
        return [(self.docs[i][0], self.docs[i][1], float(scores[i]))
                for i in order[:min(k, len(order))] if scores[i] > 0]

    def answer(self, query):
        ranking = self.retrieve(query, 2)
        top = ranking[0][2] if ranking else 0.0
        second = ranking[1][2] if len(ranking) > 1 else 0.0
        reason = None
        if not ranking:
            reason = "nessun_termine_noto"
        elif top < self.min_score:
            reason = "pertinenza_insufficiente"
        elif len(ranking) > 1 and top - second < self.min_margin:
            reason = "fonti_ambigue"
        return {
            "answer": ABSTENTION if reason else ranking[0][1],
            "citation": None if reason else ranking[0][0],
            "score": top, "abstained": reason is not None,
            "reason": reason or "estratto_letterale",
            "ranking": [{"source": sid, "score": score} for sid, _, score in ranking],
        }

EVALUATION_QUERIES = (
    ("a cosa serve DNS?", "reti"),
    ("nomi di dominio e indirizzi IP", "reti"),
    ("che cosa collega una chiave esterna?", "db"),
    ("collegare una riga a una relazione", "db"),
    ("come evitare SQL injection con query e parametri?", "security"),
    ("query parametrizzate e dati utente", "security"),
    ("health check istanza disponibile", "cloud"),
    ("ricevere traffico e valutare istanza", "cloud"),
    ("unicorno galattico", None), ("ricetta risotto funghi", None),
    ("", None), ("e la di un per", None),
)

def experiment():
    assistant = MiniRAG()
    outcomes = []
    for query, expected in EVALUATION_QUERIES:
        result = assistant.answer(query)
        outcomes.append({"query": query, "expected_citation": expected, **result,
                         "correct": result["citation"] == expected})
    tied = MiniRAG((("a", "protocollo DNS"), ("b", "protocollo DNS"))).answer("DNS")
    return {
        "dataset": "Quattro documenti tecnici originali; dodici query manuali distinte dai testi",
        "mode": "retrieval_estrattivo_senza_LLM", "documents": len(DOCS),
        "thresholds": {"min_score": assistant.min_score, "min_margin": assistant.min_margin,
                       "selection": "costanti didattiche fissate prima della valutazione; non calibrate"},
        "queries": outcomes, "correct": sum(r["correct"] for r in outcomes),
        "total": len(outcomes), "abstentions": sum(r["abstained"] for r in outcomes),
        "ambiguous_example": tied,
    }

if __name__ == "__main__":
    print(json.dumps(experiment(), ensure_ascii=False, indent=2, allow_nan=False))
