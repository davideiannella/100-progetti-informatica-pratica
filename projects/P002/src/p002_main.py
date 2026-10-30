import csv, statistics, math
from pathlib import Path

def analyze_rows(rows, threshold=None):
    values = []
    missing = 0
    for r in rows:
        raw = (r.get('kwh') or '').strip()
        if not raw:
            missing += 1
            continue
        try:
            v = float(raw)
        except ValueError:
            missing += 1
            continue
        if not math.isfinite(v) or v < 0:
            raise ValueError('Consumo non finito o negativo')
        values.append((r.get('date', ''), v))
    nums = [v for _, v in values]
    result = {'count': len(nums), 'missing': missing, 'mean': statistics.mean(nums) if nums else None, 'min': min(nums) if nums else None, 'max': max(nums) if nums else None}
    if threshold is not None:
        result['peaks'] = [d for d, v in values if v > threshold]
    return result

def analyze_csv(path, threshold=None):
    with open(path, newline='', encoding='utf-8') as f:
        return analyze_rows(csv.DictReader(f), threshold)
