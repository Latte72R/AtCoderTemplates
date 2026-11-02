# アルゴリズム・データ構造テンプレート

## [CycleDetection](CycleDetection/)

グラフの閉路検出・閉路への到達判定．

- [abc245_f.py](CycleDetection/abc245_f.py)：有向グラフで閉路へ到達できる頂点を判定．
- [abc266_f.py](CycleDetection/abc266_f.py)：連結な単一閉路の無向グラフで閉路上の頂点を特定し，付随する木を分類．

## [Dijkstra](Dijkstra/)

非負重みのグラフで最短距離・最短経路を求める．

- [typical_algorithm_d.py](Dijkstra/typical_algorithm_d.py)：辺重みのみの基本例．
- [tessoku_book_ek.py](Dijkstra/tessoku_book_ek.py)：最短経路の復元例．
- [abc362_d_.py](Dijkstra/abc362_d_.py)：辺重みに加えて頂点重みも扱う．

## [LazySegTree](LazySegTree/)

区間への一括代入と区間最小値の取得．

- [abc382_f.py](LazySegTree/abc382_f.py)：`atcoder.lazysegtree` の演算・遅延操作の設定例．

## [SegTree](SegTree/)

1点更新と区間の集約．演算と単位元を変えて流用できる．

- [a59_.py](SegTree/a59_.py)：1点代入・区間和の基本例．
- [abc157_E.py](SegTree/abc157_E.py)：区間 OR でビット集合・文字の種類数を管理．
- [chokudai_S001_j.py](SegTree/chokudai_S001_j.py)：値ごとの出現数を区間和で管理し，転倒数を数える．

## [UnionFind](UnionFind/)

成分の併合・同一成分判定，成分情報の管理．

- [atc001_B.py](UnionFind/atc001_B.py)：経路圧縮・ランク併合の基本例．
- [abc420_e.py](UnionFind/abc420_e.py)：根に成分内の黒頂点数を保持．
- [abc228_d.py](UnionFind/abc228_d.py)：経路圧縮で次の未使用位置を探索．

## [RollingHash](RollingHash/)

部分文字列のハッシュを O(1) で取得し，一致を比較する．

- [abc284_f.py](RollingHash/abc284_f.py)：累積ハッシュと基数のべき乗を前計算．ハッシュ衝突の可能性がある．

## [nCk mod P](<nCk mod P/>)

素数 P を法とした組合せ数を求める．

- [abc178_d.py](<nCk mod P/abc178_d.py>)：階乗・逆階乗を前計算し，`comb(n, k)` を O(1) で計算（n < MAX < P）．

## [中国剰余定理](中国剰余定理/)

互いに素な法の剰余条件を統合し，法の積を法とする値を復元する．

- [abc286_f.py](中国剰余定理/abc286_f.py)：逆元を使って剰余を順に統合．全体は対話型問題のため，統合部分を流用する．

## [強連結成分分解](強連結成分分解/)

有向グラフの相互に到達可能な頂点をまとめ，DAG に縮約する．

- [abc478_e.py](強連結成分分解/abc478_e.py)：`scc` で成分数・所属を取得し，`construct` で縮約グラフを構築．

## [いもす法](いもす法/)

多数の区間加算を差分配列へ記録し，累積和で各位置の値をまとめて求める．

- [abc408_c_.py](<いもす法/abc408_c_.py>)：閉区間への加算と，被覆数の復元の基本例．
- [abc338_d.py](<いもす法/abc338_d.py>)：環状区間の分割と，各候補へのコスト加算．

## [SlidingWindow](SlidingWindow/)

区間に出入りする要素だけを更新し，頻度や種類数を効率よく管理する．

- [abc210_c (解説).py](<SlidingWindow/abc210_c (解説).py>)：固定長の窓に含まれる値の頻度・種類数を管理．
- [abc449_c_しゃくとり.py](<SlidingWindow/abc449_c_しゃくとり.py>)：現在位置からの距離が指定範囲内にある要素を管理．

## [01BFS](01BFS/)

辺重みが0か1のグラフで，最短距離を O(V+E) で求める．

- [arc084_b.py](<01BFS/arc084_b.py>)：deque を使う，辺重みが0か1のグラフの最短距離．

## [WarshallFloyd](WarshallFloyd/)

距離行列から全頂点間の最短距離を O(N^3) で求める．

- [abc012_4.py](<WarshallFloyd/abc012_4.py>)：距離行列を更新し，全頂点間の最短距離を取得．

## [座標圧縮](座標圧縮/)

値の大小関係と等値関係を保ち，小さい連番へ置き換える．元の値同士の距離は保たれない．

- [abc213_c.py](<座標圧縮/abc213_c.py>)：辞書による番号付けで，行と列を独立に圧縮．

## [桁DP](桁DP/)

数字を1桁ずつ決め，余りなどの状態ごとに条件を満たす整数を数える．

- [abc135_d_.py](<桁DP/abc135_d_.py>)：左から数字を追加する，剰余を状態に持つ桁DP．

## [木DP](木DP/)

子の部分木の結果を親へ集約し，木全体の数え上げや最適化を行う．

- [abc036_d.py](<木DP/abc036_d.py>)：頂点の白黒を状態にし，子の数え上げ結果を親へ集約．

## [BitDP](BitDP/)

集合をビットで表し，到達可否や最小コストを集合ごとに計算する．

- [abc415_c.py](<BitDP/abc415_c.py>)：1要素ずつ増やす集合の到達可否を判定．
- [A23.py](<BitDP/A23.py>)：ビット OR による集合の合併と，最小コストの計算．
