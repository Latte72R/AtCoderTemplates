# 問題: 環状の橋を1本取り除いたとき，指定された順路の移動距離の合計を最小化する．
# 理論: 候補ごとの評価値に対する区間加算も，差分配列でまとめて処理できる．環状区間は端で分割する．
# 使い方: 各移動が候補区間へ与えるコストを psum に加減算し，累積和で全候補の評価値を得る．O(N+M)．

N, M = map(int, input().split())
X = list(map(int, input().split()))

psum = [0] * (N + 1)

for i in range(M - 1):
    x1, x2 = X[i] - 1, X[i + 1] - 1
    y1, y2 = (x1, x2) if x1 < x2 else (x2, x1)
    psum[y1] += N - (y2 - y1)
    psum[y2] -= N - (y2 - y1)
    psum[y2] += y2 - y1
    psum[0] += y2 - y1
    psum[y1] -= y2 - y1

count = [0] * N
count[0] = psum[0]
for i in range(1, N):
    count[i] = count[i - 1] + psum[i]

print(min(count))
