# https://github.com/Latte72R/AtCoderTemplates/blob/main/%E4%B8%AD%E5%9B%BD%E5%89%B0%E4%BD%99%E5%AE%9A%E7%90%86/abc286_f.py
# 問題: 対話型問題で，置換を未知の回数だけ適用した結果から，その回数を特定する．
# 理論: 互いに素な法の剰余条件は，法の積を法として一意に統合できる．逆元は pow(b, -1, d) で求める．
# 使い方: x≡a (mod b)，x≡c (mod d) を x=a+b*((c-a)*pow(b,-1,d)%d) で統合する．この例の C, D は統合済みの剰余と法．

L = [4, 5, 7, 9, 11, 13, 17, 19, 23]

M = sum(L)

A = []
S = 0
for n in L:
    A += list(range(S + 2, S + n + 1)) + [S + 1]
    S += n

print(M)
print(" ".join(map(str, A)))

B = list(map(int, input().split()))

C = 0
D = 1
S = 0
for n in L:
    a = B[S + n - 1] - (S + 1)
    b = n
    c = C
    d = D
    C = a + b * (((c - a) * pow(b, -1, d)) % d)
    D = b * d
    S += n

print(C + 1)
