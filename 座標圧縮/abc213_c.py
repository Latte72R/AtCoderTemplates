# 問題: 点のある行・列だけを残し，各点の圧縮後の座標を求める．
# 理論: 異なる値をソートして連番に置き換えると，大小関係と等値関係を保って添字を小さくできる．
# 使い方: sorted(set(values)) を列挙して元の値から番号への辞書を作る．行・列は独立に圧縮する．O(N log N)．

H, W, N = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
X = set()
Y = set()
for a, b in AB:
    Y.add(a)
    X.add(b)
X = {b: i + 1 for i, b in enumerate(sorted(X))}
Y = {a: i + 1 for i, a in enumerate(sorted(Y))}
for i, (a, b) in enumerate(AB):
    print(Y[a], X[b])
