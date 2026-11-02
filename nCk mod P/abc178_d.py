# 問題: 3以上の整数を並べて和を S にする数列の個数を，素数 P で割った余りで求める．
# 理論: 素数 P と n < P に対し，nCk = n! / (k!(n-k)!) を階乗と逆階乗の積として mod P で計算する．
# 使い方: MAX を必要な n より大きく設定して前計算し，comb(n, k) を呼ぶ．前計算 O(MAX)，各問合せ O(1)．

MAX = 10**4  # n の取りうる最大値( ただし, Pより小さいものとする )を取る

P = 10**9 + 7  # P は十分大きく，かつ素数である
fac = [1] + [1]
finv = [1] + [1]
inv = [0] + [1]

for i in range(2, MAX):
    fac += [fac[-1] * i % P]
    inv += [P - inv[P % i] * (P // i) % P]
    finv += [finv[-1] * inv[i] % P]


# 引数: n, k=組合せの引数．前提: 有効な n は n < MAX < P，P は素数．
# 戻り値: nCk mod P．n < 0，k < 0，n < k なら 0．
# fac・finv・inv の前計算は時間 O(MAX)，1回の計算は O(1)．
def comb(n, k):
    if n < 0 or k < 0 or n < k:
        return 0
    return (fac[n] * finv[k] * finv[n - k]) % P


S = int(input())

count = 0
for num in range(1, int(S // 3) + 1):
    copy = S - num * 3
    count = (count + comb(copy + num - 1, num - 1)) % P

print(count)
