# https://github.com/Latte72R/AtCoderTemplates/blob/main/%E7%B4%A0%E6%95%B0%E3%83%BB%E7%B4%A0%E5%9B%A0%E6%95%B0%E5%88%86%E8%A7%A3/abc412_e.py
# 問題: 階乗に含まれる素因数の総指数を計算し，区間での増加分を求める実装例．
# 理論: 素数の倍数を除外する篩で素数を列挙できる．n! の素因数 p の指数は floor(n/p)+floor(n/p²)+…．
# 使い方: sieve(n) で素数列を得る．count_exp(n) は共有する primes を使い，n! の素因数の総指数を返す．

import sys

input = sys.stdin.readline

L, R = map(int, input().split())


# 1. エラトステネスの篩で素数を列挙
# 引数: n=列挙する上限（n >= 1）．戻り値: n 以下の素数の昇順リスト．時間 O(n log log n)．
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]


primes = sieve(R)


# 2. n! に含まれる全素因数の合計指数を計算
# 引数: n=階乗の引数（n >= 0）．primes に n 以下の素数を事前に用意する．
# 戻り値: n! の全素因数の指数の合計．時間 O(π(n)+√n log n) を上界とする（π(n) は n 以下の素数の個数）．
def count_exp(n):
    total = 0
    for p in primes:
        if p > n:
            break
        # floor(n/p) + floor(n/p^2) + … を合算
        div = p
        while div <= n:
            total += n // div
            div *= p
    return total


exp_L = count_exp(L)
exp_R = count_exp(R)

# 3. 答えを出力
print(exp_R - exp_L + 1)
