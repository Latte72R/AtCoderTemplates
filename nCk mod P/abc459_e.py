# https://github.com/Latte72R/AtCoderTemplates/blob/main/nCk%20mod%20P/abc459_e.py
# 問題: 根付き木で葉側から親へ余剰を渡し，各頂点で必要数を選ぶ場合の数を求める．
# 理論: nCr = n(n-1)…(n-r+1)/r!．r! の逆元を前計算すれば，n までの階乗表を作らずに計算できる．
# 使い方: calc = LargeNCombination(max_r, mod) を構築し，calc.comb(n, r) を呼ぶ（mod は素数，max_r < mod）．

from collections import deque
import sys


# n が大きく r が小さい場合の組合せ計算．n は mod 以上でもよい．
class LargeNCombination:
    """n が大きく r が小さい場合の nCr (mod M) を計算する"""

    # 引数: max_r=r の最大値，mod=素数（0 <= max_r < mod）．逆階乗を前計算する．
    # 時間 O(max_r + log mod)．
    def __init__(self, max_r, mod):
        """max_r までの階乗と階乗逆元を前計算する"""
        self.mod = mod
        self.inv_fact = [1] * (max_r + 1)

        fact = 1
        for i in range(1, max_r + 1):
            fact = fact * i % mod

        self.inv_fact[max_r] = pow(fact, -1, mod)

        for i in range(max_r, 0, -1):
            self.inv_fact[i - 1] = self.inv_fact[i] * i % mod

    # 引数: n >= 0，0 <= r <= max_r．戻り値: nCr mod mod（n < r なら 0）．時間 O(r)．
    def comb(self, n, r):
        """C(n, r) mod mod を O(r) で計算する"""
        if n < r:
            return 0

        res = 1
        for i in range(r):
            res = res * ((n - i) % self.mod) % self.mod

        return res * self.inv_fact[r] % self.mod


input = sys.stdin.readline

MOD = 998244353

N = int(input())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

combination = LargeNCombination(max(D), MOD)

children = [0] * N
parents = [-1] * N
for i, p in enumerate(P, start=1):
    p -= 1
    parents[i] = p
    children[p] += 1

candy = [0] * N

queue = deque()
for i in range(N):
    if children[i] == 0:
        queue.append(i)
    candy[i] += C[i]

result = 1
found = [0] * N
while queue:
    q = queue.popleft()
    c = candy[q]
    p = parents[q]
    if p != -1:
        candy[p] += c
        candy[p] -= D[q]
        found[p] += 1
        if children[p] == found[p]:
            queue.append(p)
    if c < D[q]:
        result *= 0
        continue
    result *= combination.comb(c, D[q])
    result %= MOD

print(result)
