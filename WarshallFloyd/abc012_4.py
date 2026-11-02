# https://github.com/Latte72R/AtCoderTemplates/blob/main/WarshallFloyd/abc012_4.py
# 問題: 重み付き無向グラフで，他の頂点への最短距離の最大値が最小になる頂点を探す．
# 理論: 経由してよい頂点を1つずつ増やし，dist[i][j] を dist[i][k]+dist[k][j] で更新する．
# 使い方: 対角を0，他を INF，辺の重みを初期値にし，k を最外側にして3重ループする．全点対最短距離を O(N^3) で取得．

N, M = map(int, input().split())

INF = 10**18

# distの初期化
dist = [[INF] * N for _ in range(N)]

for i in range(N):
    dist[i][i] = 0

for _ in range(M):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = min(dist[a][b], w)
    dist[b][a] = min(dist[b][a], w)

# Warshall-Floyd法
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = min(max(d) for d in dist)

print(ans)
