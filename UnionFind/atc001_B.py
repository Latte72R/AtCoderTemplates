# 問題: 頂点の連結成分を併合し，2頂点が同じ成分に属するかを判定する．
# 理論: 頂点を根付き木で成分ごとに管理する．経路圧縮とランク併合により各操作は償却 O(α(N))．
# 使い方: par・rank を初期化し，unite(x, y) で併合，same(x, y) で同一成分判定，root(x) で代表元を得る．

N, Q = map(int, input().split())
PAB = [list(map(int, input().split())) for _ in range(Q)]

par = list(range(N))
rank = [0] * N


# 引数: x=頂点番号．戻り値: x の属する成分の根．par を経路圧縮で更新する．
# ランク併合と併用し，1操作あたり償却 O(α(N))（α は逆アッカーマン関数）．
def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
        return par[x]


# 引数: x, y=頂点番号．戻り値: 同じ成分なら True．償却 O(α(N))．
def same(x, y):
    return root(x) == root(y)


# 引数: x, y=併合する頂点番号．par・rank を更新し，同じ成分なら何もしない．
# 戻り値なし．経路圧縮とランク併合により償却 O(α(N))．
def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


for p, a, b in PAB:
    if p == 0:
        unite(a - 1, b - 1)
    else:
        if same(a - 1, b - 1):
            print("Yes")
        else:
            print("No")
