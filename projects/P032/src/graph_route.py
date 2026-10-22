import heapq
import math
from itertools import count

def shortest(graph, start, target):
    if start not in graph or target not in graph:
        raise KeyError('stop not found')
    for edges in graph.values():
        for node, weight in edges:
            if node not in graph:
                raise KeyError('edge to missing stop')
            if isinstance(weight, bool) or not isinstance(weight, (int, float)) or weight < 0 or not math.isfinite(weight):
                raise ValueError('weight')
    order = count()
    q = [(0, next(order), start, [])]
    seen = set()
    while q:
        cost, _, node, path = heapq.heappop(q)
        if node in seen:
            continue
        seen.add(node)
        path = path + [node]
        if node == target:
            return (cost, path)
        for nxt, w in graph.get(node, []):
            heapq.heappush(q, (cost + w, next(order), nxt, path))
    raise ValueError('unreachable')
