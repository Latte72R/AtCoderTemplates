# 問題: 禁止された集合を避け，1要素ずつ追加して全要素を選べるか判定する．
# 理論: 選択済み集合をビットで表すと，集合 s の直前の状態は，立っているビットを1つ除いた集合になる．
# 使い方: 各集合の到達可否を要素数別の data に記録する．許可された集合に到達可能な直前状態があれば追加．1ケース O(N*2^N)．

T = int(input())


# 引数: n=非負整数のビット集合．戻り値: (立っているビット数, ビット長)．O(log(n+1))．
# 同じ値は n.bit_count() と n.bit_length() でも取得できる．
def count(n):
    cnt = 0
    log = 0
    while n > 0:
        if n % 2 == 1:
            cnt += 1
        n //= 2
        log += 1
    return cnt, log


for _ in range(T):
    N = int(input())
    S = input()
    data = [set() for _ in range(N)]
    for i, c in enumerate(S):
        if c == "0":
            d = i + 1
            cnt, log = count(d)
            if cnt == 1:
                data[0].add(d)
                continue
            flag = False
            for e in range(log):
                if d & (1 << e):
                    if d - (1 << e) in data[cnt - 2]:
                        flag = True
                        break
            if flag:
                data[cnt - 1].add(d)
    print("Yes" if data[-1] else "No")
