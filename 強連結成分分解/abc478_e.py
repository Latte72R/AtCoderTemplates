# https://github.com/Latte72R/AtCoderTemplates/blob/main/%E5%BC%B7%E9%80%A3%E7%B5%90%E6%88%90%E5%88%86%E5%88%86%E8%A7%A3/abc478_e.py
# 問題: 頂点間の大小制約を満たす整数の割当が可能か判定し，可能なら割当例を出力する．
# 理論: 有向グラフの相互に到達可能な頂点をまとめると，成分間のグラフは DAG（閉路のない有向グラフ）になる．
# 使い方: label, group = scc(N, G, RG) で成分数・所属を得る．RG は逆向きのグラフ．construct で縮約グラフも作れる．

import sys

# DFS するので再帰深度に注意
sys.setrecursionlimit(1 << 20)


# 引数: N=頂点数，G=有向グラフの隣接リスト，RG=辺を逆向きにした隣接リスト．
# 戻り値: (label, group)．label は成分数，group[v] は頂点 v の成分番号．
# 成分番号は縮約グラフのトポロジカル順．時間 O(N + M)．
def scc(N, G, RG):
    order = []
    used = [0] * N
    group = [-1] * N

    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)

    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)

    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0] * N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group


# 引数: N=頂点数，G=隣接リスト，label・group=scc の戻り値．
# 戻り値: (G0, GP)．G0[c] は成分 c から出る隣接成分の集合，GP[c] は所属頂点列．
# 集合への追加を平均 O(1) として，時間 O(N + M)．
def construct(N, G, label, group):
    G0 = [set() for i in range(label)]
    GP = [[] for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP


N, Q = map(int, input().split())
TUV = [list(map(int, input().split())) for _ in range(Q)]

G = [[] for _ in range(N)]
RG = [[] for _ in range(N)]
lt = [[] for _ in range(N)]

for t, u, v in TUV:
    u -= 1
    v -= 1
    G[u].append(v)
    RG[v].append(u)
    if t == 1:
        lt[u].append(v)

label, group = scc(N, G, RG)
ans = [set() for _ in range(N)]

for i, g in enumerate(group):
    for j in lt[i]:
        ans[j].add(g)

for i, g in enumerate(group):
    if g in ans[i]:
        print("No")
        break
else:
    print("Yes")
    print(*[g + 1 for g in group])
