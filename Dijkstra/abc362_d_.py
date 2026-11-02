# https://github.com/Latte72R/AtCoderTemplates/blob/main/Dijkstra/abc362_d_.py
# 問題: 辺と頂点の両方にコストがあるグラフで，頂点1から各頂点への最小コストを求める．
# 理論: 非負コストなら暫定距離が最小の頂点から距離を確定できる．頂点重みは到着時のコストに加える．
# 使い方: dijkstra(N, graph, src=0, weight=A) で始点の重みも含む距離配列を得る．weight 省略時は辺重みのみ．

import heapq

INF = 10**15


# 引数: vertex=頂点数，graph[u]=隣接先と辺重み (v, w) の列．src=始点．
# goal=None なら全頂点を探索．weight=頂点重みの配列で，None なら辺重みのみ．
# 辺重み・頂点重みは非負．戻り値: 始点の重みも含む最短コストの配列 dist．
# goal 指定時，他頂点の距離は未確定の場合がある．時間 O((V + E) log V)．
def dijkstra(vertex, graph, src=0, goal=None, weight=None):
    dist = [INF] * vertex
    if weight is None:
        dist[src] = 0
        pq = [(0, src)]
    else:
        dist[src] = weight[src]
        pq = [(weight[src], src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        if goal is not None and u == goal:
            break
        for v, w in graph[u]:
            nd = d + w
            if weight is not None:
                nd += weight[v]
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


N, M = map(int, input().split())
A = list(map(int, input().split()))
UVB = [tuple(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N)]
for u, v, b in UVB:
    u -= 1
    v -= 1
    graph[u].append((v, b))
    graph[v].append((u, b))

dist = dijkstra(N, graph, weight=A)
for i in range(1, N):
    print(dist[i], end=" ")
print()
