import math
from sys import float_info

def knapsack(items, capacity):
    if type(capacity) is not int or capacity < 0:
        raise ValueError('Capacità negativa')
    if any((type(w) is not int or w <= 0 or (not isinstance(v, (int, float))) or v < 0 or v > float_info.max or not math.isfinite(v) for _, w, v in items)):
        raise ValueError('Item non valido')
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i, (_, w, v) in enumerate(items, 1):
        for c in range(capacity + 1):
            dp[i][c] = dp[i - 1][c]
            if w <= c:
                candidate = dp[i - 1][c - w] + v
                if candidate > float_info.max:
                    raise OverflowError('Il valore ottimo supera il limite numerico del laboratorio (massimo float)')
                dp[i][c] = max(dp[i][c], candidate)
    chosen = []
    c = capacity
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            name, w, v = items[i - 1]
            chosen.append(name)
            c -= w
    chosen.reverse()
    return (dp[n][capacity], chosen)
