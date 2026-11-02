# 問題: 長さ K の連続区間に含まれる値の種類数の最大値を求める．
# 理論: 区間を1つずらすとき，出る要素と入る要素だけを更新すれば，区間全体を数え直す必要がない．
# 使い方: 辞書に区間内の頻度を持ち，0になったキーを削除する．len(color_count) が種類数．全体で平均 O(N)．

N, K = map(int, input().split())
C = list(map(int, input().split()))

color_count = {}
for i in range(K):
    color = C[i]
    color_count[color] = color_count.get(color, 0) + 1

max_types = len(color_count)

for i in range(K, N):
    left_color = C[i - K]
    color_count[left_color] -= 1
    if color_count[left_color] == 0:
        del color_count[left_color]

    new_color = C[i]
    color_count[new_color] = color_count.get(new_color, 0) + 1

    current_types = len(color_count)
    max_types = max(max_types, current_types)

print(max_types)
