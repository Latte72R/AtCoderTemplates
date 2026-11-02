# 問題: 盤面上の横棒を落としたとき，各棒が止まる行を求める．
# 理論: 遅延セグメント木は区間全体への操作を保留し，必要なときだけ子へ伝えて区間更新を高速化する．
# 使い方: この設定は区間最小値・区間代入用．prod(l, r) で取得，apply(l, r, x) で代入する（[l, r)）．

from atcoder.lazysegtree import LazySegTree


# 引数: a, b=区間の集約値．戻り値: その最小値．O(1)．
def op(a, b):
    return min(a, b)


# 引数なし．戻り値: min の単位元 H（管理する高さは H 以下）．O(1)．
def e():
    return H


# 引数: f=代入値（-1 は操作なし），s=現在の区間最小値．
# 戻り値: 区間代入後の最小値．O(1)．
def mapping(f, s):
    if f == -1:
        return s
    return f


# 引数: f=後から行う代入，g=先に行う代入（-1 は操作なし）．
# 戻り値: g の後に f を行う合成操作．後の有効な代入を優先する．O(1)．
def composition(f, g):
    if f == -1:
        return g
    return f


# 引数なし．戻り値: 操作なしを表す -1．代入値に -1 を使わないことが前提．O(1)．
def id():
    return -1


H, W, N = map(int, input().split())
RCL = [(i, list(map(int, input().split()))) for i in range(N)]
RCL.sort(key=lambda x: x[1][0], reverse=True)

v = [H] * W

seg = LazySegTree(op=op, e=e(), mapping=mapping, composition=composition, id_=id(), v=v)

res = [-1] * N
for i, (r, c, l) in RCL:
    m = seg.prod(c - 1, c + l - 1)
    res[i] = m
    seg.apply(c - 1, c + l - 1, m - 1)

print("\n".join(map(str, res)))
