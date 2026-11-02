# https://github.com/Latte72R/AtCoderTemplates/blob/main/01BFS/arc084_b.py
# 問題: 正の整数 K の正の倍数のうち，十進表記の桁和の最小値を求める．
# 理論: 辺重みが0か1なら，重み0の遷移を deque の先頭，重み1の遷移を末尾へ入れて最短距離を求められる．
# 使い方: 隣接リストに (行き先, 0か1) を格納し，距離が改善したときだけ追加する．時間 O(V+E)．

from collections import deque

K = int(input())

pathes = [[] for _ in range(K)]

for i in range(K):
    pathes[i].append(((i * 10) % K, 0))
    pathes[i].append(((i + 1) % K, 1))

INF = 10**18
queue = deque([1])
dist = [INF] * K
dist[1] = 1

while queue:
    p = queue.popleft()
    d = dist[p]
    if p == 0:
        break
    for q, c in pathes[p]:
        if c == 0:
            if dist[q] > d:
                queue.appendleft(q)
                dist[q] = d
        else:
            if dist[q] > d + 1:
                queue.append(q)
                dist[q] = d + 1

print(dist[0])
