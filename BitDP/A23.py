# 問題: 各クーポンで無料になる品物が決まっているとき，全品物をそろえる最小クーポン枚数を求める．
# 理論: 取得済み集合 s と追加分 coupon の和集合は s|coupon．集合ごとの最小コストをDPで管理できる．
# 使い方: dp[0][0]=0 から，追加しない遷移と ns=s|coupon へコストを加える遷移を行う．O(M*2^N)．

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
coupons = [0] * M
for i in range(M):
    s = 0
    for j, a in enumerate(A[i]):
        s |= (1 << j) * a
    coupons[i] = s

INF = 10**4
# dp[i][j]: iまでのチケットでjまでを買うのに必要な枚数 (1-indexed)
dp = [[INF] * (1 << N) for _ in range(M + 1)]
dp[0][0] = 0

for i in range(M):
    coupon = coupons[i]
    for s in range(1 << N):
        # クーポン i を使わない
        dp[i + 1][s] = min(dp[i + 1][s], dp[i][s])

        # クーポン i を使う
        ns = s | coupon
        dp[i + 1][ns] = min(dp[i + 1][ns], dp[i][s] + 1)

print(-1 if dp[-1][-1] == INF else dp[-1][-1])
