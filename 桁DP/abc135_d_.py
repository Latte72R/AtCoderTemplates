# https://github.com/Latte72R/AtCoderTemplates/blob/main/%E6%A1%81DP/abc135_d_.py
# 問題: 数字と ? からなる文字列を整数にしたとき，13で割って5余る置換の個数を求める．
# 理論: 左から数字 d を追加すると，余り r は (10*r+d)%m に変わる．桁位置と余りごとに場合の数を持つ．
# 使い方: dp[0][0]=1 から，許される数字へ遷移する．法 m・基数 B・桁数 L に対して O(L*m*B)．上限以下の制約は扱わない例．

MOD = 10**9 + 7

S = input()
dp = [[0] * 13 for _ in range(len(S) + 1)]
dp[0][0] = 1

for i in range(len(S)):
    for j in range(13):
        if S[i] == "?":
            for k in range(10):
                mod = (j * 10 + k) % 13
                dp[i + 1][mod] += dp[i][j]
        else:
            k = int(S[i])
            mod = (j * 10 + k) % 13
            dp[i + 1][mod] += dp[i][j]
    for j in range(13):
        dp[i + 1][j] %= MOD


print(dp[-1][5])
