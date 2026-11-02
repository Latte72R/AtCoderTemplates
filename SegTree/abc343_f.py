# https://github.com/Latte72R/AtCoderTemplates/blob/main/SegTree/abc343_f.py
# 問題: 配列の1点更新と，区間内で2番目に大きい値の出現回数の取得を行う．
# 理論: 上位2種類の値と個数を組にし，結合則を満たす op でまとめれば，複数の情報もセグ木に載せられる．
# 使い方: 葉を ((値, 1), (0, 0)) とし，set で更新，prod(l, r)[1][1] で2番目の値の個数を取得．各 O(log N)．

from atcoder.segtree import SegTree


# 引数: a, b=((最大値, 個数), (2番目の異なる値, 個数))．値は正整数を想定する．
# 戻り値: 2区間を合わせた同形式の情報．単位元は ((0, 0), (0, 0))．時間 O(1)．
def op(a, b):
    if a[0][0] > b[0][0]:
        if a[1][0] > b[0][0]:
            return a
        if a[1][0] < b[0][0]:
            return (a[0], b[0])
        return (a[0], (a[1][0], a[1][1] + b[0][1]))
    if a[0][0] < b[0][0]:
        if a[0][0] < b[1][0]:
            return b
        if a[0][0] > b[1][0]:
            return (b[0], a[0])
        return (b[0], (a[0][0], a[0][1] + b[1][1]))
    if a[1][0] > b[1][0]:
        return ((a[0][0], a[0][1] + b[0][1]), a[1])
    if a[1][0] < b[1][0]:
        return ((a[0][0], a[0][1] + b[0][1]), b[1])
    return ((a[0][0], a[0][1] + b[0][1]), (a[1][0], a[1][1] + b[1][1]))


N, Q = map(int, input().split())
A = list(map(int, input().split()))

segtree = SegTree(op, ((0, 0), (0, 0)), N)
for i, a in enumerate(A):
    segtree.set(i, ((a, 1), (0, 0)))

for _ in range(Q):
    q, *args = map(int, input().split())
    if q == 1:
        p, x = args
        p -= 1
        segtree.set(p, ((x, 1), (0, 0)))
    else:
        l, r = args
        l -= 1
        r -= 1
        print(segtree.prod(l, r + 1)[1][1])
