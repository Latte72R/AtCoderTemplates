# https://github.com/Latte72R/AtCoderTemplates/blob/main/UnionFind/abc228_d.py
# 問題: ハッシュ位置が埋まっていれば次の空き位置へ進む配列への挿入と，値の取得を処理する．
# 理論: 削除済みの位置を次の候補につなぎ，経路圧縮で読み飛ばすと「次の未使用位置」を高速に探せる．
# 使い方: find(x) で空き位置を取得し，使用後は par[x] = find(x + 1)．末尾の番兵を先頭につなぐと巡回できる．

# ABC 228
# D - Linear Probing
# UnionFind 同様に経路圧縮を用いることで O(QlogN) で実装できる


import sys

input = sys.stdin.readline
N = 1 << 20
Q = int(input())
A = [-1] * (N + 1)

par = list(range(N + 1))
par[-1] = 0


# 引数: x=探索開始位置．戻り値: x 以降で最初の空き位置（末尾の次は先頭）．
# par は次の探索先を保持し，呼出し時に経路圧縮する．空き位置が存在することが前提．
# 1回の最悪 O(N)．経路圧縮のみなので，一連の Q 回は O((N + Q) log N) を上界とする．
def find(x):
    while par[x] != x:
        par[x] = par[par[x]]
        x = par[x]
    return x


for _ in range(Q):
    t, x = map(int, input().split())
    h = x % N
    if t == 1:
        idx = find(h)
        dst = find(idx + 1)
        par[idx] = dst
        A[idx] = x
    else:
        sys.stdout.write(str(A[h]) + "\n")
