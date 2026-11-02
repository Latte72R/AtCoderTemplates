# 問題: 辺の追加と頂点の白黒反転を行い，指定頂点の連結成分に黒い頂点があるか判定する．
# 理論: Union-Find の成分情報は根に持たせる．合算できる情報なら，併合時に2つの根の値をまとめられる．
# 使い方: unite(x, y) で成分を併合し，blacks[root(x)] で成分内の黒頂点数を参照・更新する．

N, Q = map(int, input().split())

par = list(range(N))
rank = [0] * N
blacks = [0] * N
isblack = [False] * N


# 引数: x=頂点番号．戻り値: x の属する成分の根．par を経路圧縮で更新する．
# ランク併合と併用し，1操作あたり償却 O(α(N))（α は逆アッカーマン関数）．
def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
        return par[x]


# 引数: x, y=併合する頂点番号．根の par・rank と成分内の黒頂点数 blacks を更新する．
# 同じ成分なら何もしない．戻り値なし．償却 O(α(N))．
def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        par[x] = y
        blacks[y] += blacks[x]
        blacks[x] = 0
    else:
        par[y] = x
        blacks[x] += blacks[y]
        blacks[y] = 0
        if rank[x] == rank[y]:
            rank[x] += 1


for _ in range(Q):
    q, *args = map(int, input().split())
    if q == 1:
        u, v = args
        unite(u - 1, v - 1)
    elif q == 2:
        v = args[0]
        if isblack[v - 1]:
            blacks[root(v - 1)] -= 1
            isblack[v - 1] = False
        else:
            blacks[root(v - 1)] += 1
            isblack[v - 1] = True
    else:
        v = args[0]
        print("Yes" if blacks[root(v - 1)] > 0 else "No")
