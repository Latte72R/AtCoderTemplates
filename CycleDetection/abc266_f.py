# https://github.com/Latte72R/AtCoderTemplates/blob/main/CycleDetection/abc266_f.py
# 問題: 閉路が1つの連結無向グラフで，2頂点間の単純パスが一意かを判定する．
# 理論: 無向 DFS では親への辺を除外し，訪問中の祖先への辺から閉路上の頂点を特定する．
# 使い方: 連結な単一閉路グラフで dfs(0, -1) を呼ぶと，result[v] が閉路への所属を表す．

from collections import deque
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

graph = [set() for _ in range(N)]

for _ in range(N):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].add(v)
    graph[v].add(u)

visited = [False] * N
finished = [False] * N
result = [False] * N
joint = -1


# 引数: x=現在の頂点，f=親頂点（根では -1）．連結な単一閉路の無向グラフ用．
# 閉路上の頂点を result に記録し，joint に閉路の接続点を保存する．
# 戻り値: 閉路の印付けを親へ継続するなら True．探索全体 O(N + M)．
def dfs(x, f):
    global joint
    if visited[x]:
        return False
    visited[x] = True
    for y in graph[x]:
        if finished[y] or y == f:
            continue
        if visited[y]:
            joint = y
            result[x] = True
            return True
        if dfs(y, x):
            result[x] = True
            return x != joint
    finished[x] = True
    return False


dfs(0, -1)

groups = {}
queue = deque()
visited = result.copy()

for i in range(N):
    if result[i]:
        groups[i] = -1
    else:
        continue
    for j in graph[i]:
        if visited[j]:
            continue
        queue.append(j)
        visited[j] = True
        groups[j] = i
    while queue:
        j = queue.popleft()
        for k in graph[j]:
            if visited[k]:
                continue
            visited[k] = True
            groups[k] = i
            queue.append(k)


Q = int(input())

for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    gx = groups[x]
    gy = groups[y]
    if (gy == x or gx == y) or (gx == gy and gx != -1):
        print("Yes")
    else:
        print("No")
