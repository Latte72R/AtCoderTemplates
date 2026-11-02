# 問題: 文字列で，同じ文字を持ち，添字の差が L 以上 R 以下の組を数える．
# 理論: 現在位置から一定範囲にある過去の要素を，追加・削除しながら頻度配列で管理できる．
# 使い方: 位置 i の集計前に i-L を追加し，集計後に i-R を削除する．count で対応する文字の個数を取得．O(N)．

N, L, R = map(int, input().split())
S = input()
ans = 0
count = [0] * 26
for i in range(N):
    if i >= L:
        count[ord(S[i - L]) - ord("a")] += 1
    ans += count[ord(S[i]) - ord("a")]
    if i >= R:
        count[ord(S[i - R]) - ord("a")] -= 1

print(ans)
