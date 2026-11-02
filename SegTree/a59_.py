# 問題: 配列への1点代入と，指定区間の総和を求めるクエリを処理する．
# 理論: 結合則を満たす演算 op と単位元があれば，区間の集約値を木で管理できる．
# 使い方: SegTree(op, e, n, v) を構築し，set(p, x) で代入，prod(l, r) で [l, r) を取得．e は単位元を返す関数．

import sys

input = sys.stdin.readline


# 結合則を満たす演算 op と単位元を使う，1点更新・区間集約用セグメント木．
# 各演算と単位元の生成が O(1) である場合の計算量を以下に記す．
class SegTree:
    # 引数: op(a, b)=二項演算，e()=単位元を返す関数，n=要素数（1以上）．
    # v=長さ n の初期配列．省略時は全要素が単位元．構築 O(n)．
    def __init__(self, op, e, n, v=None):
        # op: 二項演算, e: 単位元, n: 要素数, v: 初期値
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (2 * self._size)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._update(i)

    # 引数: p=更新位置（0 <= p < n），x=新しい値．a[p] に代入する．O(log n)．
    def set(self, p, x):
        # p: 0-indexed
        assert 0 <= p < self._n
        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    # 引数: p=取得位置（0 <= p < n）．戻り値: a[p]．O(1)．
    def get(self, p):
        # p: 0-indexed
        assert 0 <= p < self._n
        return self._d[p + self._size]

    # 引数: l, r=半開区間 [l, r)（0 <= l <= r <= n）．
    # 戻り値: 左から順に op で集約した値．空区間は単位元．O(log n)．
    def prod(self, l, r):
        # l, r: 0-indexed, [l, r)
        assert 0 <= l <= r <= self._n
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)

    # 引数なし．戻り値: 全要素を op で集約した値．O(1)．
    def all_prod(self):
        # すべての要素の演算結果
        return self._d[1]

    # 引数: k=内部ノード番号．左右の子から集約値を再計算する内部処理．O(1)．
    def _update(self, k):
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])


N, Q = map(int, input().split())
segtree = SegTree(lambda a, b: a + b, lambda: 0, N)
ans = []
for _ in range(Q):
    q, *args = map(int, input().split())
    if q == 1:
        pos, x = args
        segtree.set(pos - 1, x)
    else:
        l, r = args
        ans.append(str(segtree.prod(l - 1, r - 1)) + "\n")

sys.stdout.writelines(ans)
