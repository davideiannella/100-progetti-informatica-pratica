import re, unicodedata, math
from difflib import SequenceMatcher

def normalize(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().casefold()
    return re.sub('[^a-z0-9]+', '', s)

def similarity(a, b):
    a, b = normalize(a), normalize(b)
    return SequenceMatcher(None, a, b).ratio() if a and b else 0.0

def find_pairs(values, threshold=0.85):
    if isinstance(threshold, bool) or not isinstance(threshold, (int, float)) or not math.isfinite(threshold) or not 0 <= threshold <= 1:
        raise ValueError('Soglia non valida')
    out = []
    for i, a in enumerate(values):
        for j in range(i + 1, len(values)):
            score = similarity(a, values[j])
            if score >= threshold:
                out.append((i, j, round(score, 3)))
    return out
