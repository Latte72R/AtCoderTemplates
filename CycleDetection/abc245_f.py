# https://github.com/Latte72R/AtCoderTemplates/blob/main/CycleDetection/abc245_f.py
# 問題: 有向グラフで，辺をたどり続けられる始点の個数を求める．
# 理論: DFS の訪問中の頂点への辺は閉路を表す．探索完了の頂点への辺とは区別する．
# 使い方: graph と状態配列を用意して各頂点から dfs(x) を呼ぶ．result に閉路へ到達できる頂点が残る．

import sys

sys.setrecursionlimit(2000000)


N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)

visited = [False] * N
finished = [False] * N
result = [False] * N


# 引数: x=探索開始頂点（0 始まり）．graph・visited・finished・result を共有する．
# 戻り値: 今回の探索で閉路への到達を検出したら True（既訪問の頂点への直接呼出しは False）．
# 閉路へ到達できる頂点を result に記録する．全始点の探索合計 O(N + M)．
def dfs(x):
    if visited[x]:
        return False
    visited[x] = True
    for y in graph[x]:
        if finished[y]:
            continue
        if visited[y] or dfs(y):
            result[x] = True
            return True
    finished[x] = True
    return False


for i in range(N):
    dfs(i)
print(sum(result))
