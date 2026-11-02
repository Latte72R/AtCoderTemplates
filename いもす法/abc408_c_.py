# https://github.com/Latte72R/AtCoderTemplates/blob/main/%E3%81%84%E3%82%82%E3%81%99%E6%B3%95/abc408_c_.py
# 問題: 区間ごとに守られている地点について，地点を守る区間数の最小値を求める．
# 理論: 区間加算は差分配列の左端に +x，右端の次に -x を記録し，最後に累積和で復元できる．
# 使い方: 長さ N+1 の配列に区間 [l, r) ごとに diff[l]+=x，diff[r]-=x．まとめて復元する場合は O(N+M)．

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(M)]

data = [0] * (N + 1)
for l, r in LR:
    l -= 1
    r -= 1
    data[l] += 1
    data[r + 1] -= 1

for i in range(N):
    data[i + 1] += data[i]

data[-1] = M
print(min(data))
