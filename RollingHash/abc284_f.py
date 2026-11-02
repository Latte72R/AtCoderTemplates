# https://github.com/Latte72R/AtCoderTemplates/blob/main/RollingHash/abc284_f.py
# 問題: 長さ 2N の文字列から連続する N 文字を除き，残りが除いた部分の逆順になる位置を探す．
# 理論: 文字列を多項式の値として扱い，累積ハッシュと基数のべき乗から部分文字列のハッシュを取り出す．
# 使い方: rh = RollingHash(s, base, mod)，rh.get(l, r) で s[l:r] を取得．同じ基数・法で比較する（衝突の可能性あり）．


# 部分文字列を O(1) で比較するためのハッシュ．同じ base・mod のインスタンス間で比較する．
# ハッシュの一致には衝突の可能性がある．
class RollingHash:
    # 引数: s=対象文字列，base=基数，mod=法（base と mod は互いに素な正整数）．
    # 累積ハッシュと基数のべき乗を前計算する．時間 O(len(s))．
    def __init__(self, s, base, mod):
        self.mod = mod
        self.pw = pw = [1] * (len(s) + 1)

        l = len(s)
        self.h = h = [0] * (l + 1)

        v = 0
        for i in range(l):
            h[i + 1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(l):
            pw[i + 1] = v = v * base % mod

    # 引数: l, r=半開区間 [l, r)（0 <= l <= r <= len(s)）．
    # 戻り値: s[l:r] のハッシュ値．空区間は 0．O(1)．
    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r - l]) % self.mod


base = 911382323
mod = 10**9 + 7

N = int(input())
T = input()

s1 = T[:N]
s2 = "".join(reversed(T[N:]))

rh1 = RollingHash(s1, base, mod)
rh2 = RollingHash(s2, base, mod)

for i in range(N + 1):
    if rh1.get(0, i) == rh2.get(N - i, N) and rh1.get(i, N) == rh2.get(0, N - i):
        print(T[:i] + T[N + i :])
        print(i)
        break
else:
    print(-1)
