# https://github.com/Latte72R/AtCoderTemplates/blob/main/%E7%B4%A0%E6%95%B0%E3%83%BB%E7%B4%A0%E5%9B%A0%E6%95%B0%E5%88%86%E8%A7%A3/abc280_d.py
# 問題: K が n! を割り切る最小の正整数 n を求める．
# 理論: 合成数には平方根以下の約数がある．小さい約数から割り切り，残る1より大きい値も素数になる．
# 使い方: factorization(n) で [[素因数, 指数], ...] を取得．例: 60 → [[2, 2], [3, 1], [5, 1]]．

# 引数: n=分解する整数（n >= 2）．戻り値: [[素因数, 指数], ...]（素因数の昇順）．時間 O(√n)．
def factorization(n):
    """
    n を素因数分解 O(√n)
    2 以上の整数 n => [[素因数, 指数], ...] の 2 次元リスト
    """
    arr = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


# 引数: n=正整数，f=素数．戻り値: n を割り切る f の最大のべき指数．時間 O(log_f n)．
def number(n, f):
    c = 0
    while n % f == 0:
        n //= f
        c += 1
    return c


# 引数: f=[素因数 p, 必要な指数 e]（e >= 1）．戻り値: n! が p^e を含む最小の n．時間 O(e)．
def times(f):
    n = f[1]
    idx = 1
    s = 0
    while n > s:
        s += number(idx, f[0]) + 1
        idx += 1
    return (idx - 1) * f[0]


K = int(input())


def brute_force(n):
    import math

    for i in range(1, n + 1):
        if math.factorial(i) % n == 0:
            break
    return i


def main(n):
    fact = factorization(n)
    return max(times(f) for f in fact)


print(main(K))
