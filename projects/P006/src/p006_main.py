import heapq, math
from itertools import count

def dijkstra(graph, start, goal):
    if start not in graph or goal not in graph:
        raise KeyError('Nodo inesistente')
    for edges in graph.values():
        for node, weight in edges.items():
            if node not in graph:
                raise KeyError('Arco verso nodo assente')
            if isinstance(weight, bool) or not isinstance(weight, (int, float)) or (not math.isfinite(weight)) or (weight < 0):
                raise ValueError('Pesi finiti e non negativi richiesti')
    dist = {n: math.inf for n in graph}
    prev = {}
    dist[start] = 0
    order = count()
    pq = [(0, next(order), start)]
    while pq:
        d, _, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        if u == goal:
            break
        for v, w in graph[u].items():
            if w < 0:
                raise ValueError('Dijkstra richiede pesi non negativi')
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, next(order), v))
    if math.isinf(dist[goal]):
        return (math.inf, [])
    path = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = prev[cur]
    path.append(start)
    path.reverse()
    return (dist[goal], path)
