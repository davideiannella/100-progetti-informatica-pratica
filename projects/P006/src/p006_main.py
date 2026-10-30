import heapq, math
from itertools import count
from sys import float_info

def dijkstra(graph, start, goal):
    if start not in graph or goal not in graph:
        raise KeyError('Nodo inesistente')
    for edges in graph.values():
        for node, weight in edges.items():
            if node not in graph:
                raise KeyError('Arco verso nodo assente')
            if isinstance(weight, bool) or not isinstance(weight, (int, float)) or weight < 0 or weight > float_info.max or not math.isfinite(weight):
                raise ValueError('Usa pesi finiti non negativi, entro il massimo float')
    # dist contiene solo i nodi raggiunti; inf indica un costo fuori limite.
    dist = {start: 0}
    prev = {}
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
            if nd > float_info.max:
                nd = math.inf
            if v not in dist or nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, next(order), v))
    if goal not in dist:
        return (math.inf, [])
    if dist[goal] == math.inf:
        raise OverflowError('Il costo minimo supera il limite numerico del laboratorio (massimo float)')
    path = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = prev[cur]
    path.append(start)
    path.reverse()
    return (dist[goal], path)
