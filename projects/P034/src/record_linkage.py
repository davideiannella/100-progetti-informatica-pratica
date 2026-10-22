import re, unicodedata, math
from difflib import SequenceMatcher

def norm(s):
    if s is None:
        return ''
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub('[^a-z0-9]', '', s)

def score(a, b):
    fields = ('name', 'city', 'email')
    vals = [SequenceMatcher(None, norm(a.get(f, '')), norm(b.get(f, ''))).ratio() if norm(a.get(f, '')) and norm(b.get(f, '')) else 0.0 for f in fields]
    return sum(vals) / len(vals)

def match(a, b, threshold=0.82):
    if isinstance(threshold, bool) or not isinstance(threshold, (int, float)) or not math.isfinite(threshold) or not 0 <= threshold <= 1:
        raise ValueError('Soglia non valida')
    return score(a, b) >= threshold
