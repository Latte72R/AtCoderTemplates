# https://github.com/Latte72R/AtCoderTemplates/blob/main/%E6%9C%A8DP/abc036_d.py
# 問題: 木の各頂点を白黒に塗り，隣り合う頂点が両方黒にならない塗り方を数える．
# 理論: 木に根を決め，子の部分木の結果を親へ集約する．親の状態ごとに許される子の状態を足し，子同士は掛ける．
# 使い方: 深さの降順で処理し，dp[v][状態] を子の値から計算する．この実装は順序のソート込み O(N log N)．

import sys

sys.setrecursionlimit(300000)

MOD = 10**9 + 7
N = int(input())
path = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    path[a].append(b)
    path[b].append(a)

layer = [-1] * N
layer[0] = 0


# 引数: idx=探索開始頂点（0 始まり）．path をたどり，layer に根からの深さを記録する．
# 戻り値なし．layer[idx] を設定してから呼ぶ．全頂点の探索で O(N)．
def dfs(idx):
    for p in path[idx]:
        if layer[p] != -1:
            continue
        layer[p] = layer[idx] + 1
        dfs(p)


dfs(0)
order = [(i, l) for i, l in enumerate(layer)]
order.sort(key=lambda x: x[1], reverse=True)

# dp[i][j] := i を頂点とする部分木が j (0:白 / 1:黒) である場合の数
dp = [[1, 1] for _ in range(N)]

for i, l in order:
    for p in path[i]:
        if layer[p] < l:
            continue
        dp[i][0] *= dp[p][0] + dp[p][1]
        dp[i][1] *= dp[p][0]
        dp[i][0] %= MOD
        dp[i][1] %= MOD

print((dp[0][0] + dp[0][1]) % MOD)
