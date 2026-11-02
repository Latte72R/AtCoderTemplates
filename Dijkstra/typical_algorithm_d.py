# 問題: 頂点番号が 0 始まりの重み付き有向グラフで，頂点0から頂点N-1への最短距離を求める．
# 理論: 非負の辺重みでは，暫定距離が最小の頂点から確定する Dijkstra 法で最短距離を求められる．
# 使い方: graph[u] に (v, 重み) を格納し，dist, prev = dijkstra(N, graph, src)．goal 指定で終点確定時に終了する．

import heapq

INF = 10**18


# 引数: vertex=頂点数，graph[u]=隣接先と非負の辺重み (v, w) の列．
# src=始点（0 始まり），goal=終点．None なら全頂点を探索する．
# 戻り値: (dist, prev)．dist は最短距離，prev は経路上の直前の頂点（未設定は -1）．
# goal 指定時，他頂点の距離は未確定の場合がある．時間 O((V + E) log V)．
def dijkstra(vertex, graph, src=0, goal=None):
    dist = [INF] * vertex
    prev = [-1] * vertex
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        if goal is not None and u == goal:
            break
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, prev


# 引数: prev=Dijkstra の直前頂点配列，src=始点，goal=終点（0 始まり）．
# 戻り値: 始点から終点への頂点列．到達不能なら []，同じ頂点なら [src]．
# 時間 O(L)（L は復元する経路の頂点数，最大 V）．
def restore_path(prev, src, goal):
    if src == goal:
        return [src]
    if goal < 0 or goal >= len(prev) or prev[goal] == -1:
        return []
    path = []
    cur = goal
    while cur != -1:
        path.append(cur)
        if cur == src:
            break
        cur = prev[cur]
    return path[::-1]


# 引数: vertex=頂点数，edges=(u, v, w) の列，directed=有向なら True．
# one_indexed=True なら入力の頂点番号から1を引く．戻り値: graph[u]=[(v, w), ...]．
# 時間 O(V + E)．directed=False なら逆向きの辺も追加する．
def build_graph(vertex, edges, directed=True, one_indexed=False):
    graph = [[] for _ in range(vertex)]
    for u, v, w in edges:
        if one_indexed:
            u -= 1
            v -= 1
        graph[u].append((v, w))
        if not directed:
            graph[v].append((u, w))
    return graph


N, M = map(int, input().split())
UVC = [tuple(map(int, input().split())) for _ in range(M)]
G = build_graph(N, UVC)

D, P = dijkstra(N, G, 0, N - 1)

print(D[N - 1])
