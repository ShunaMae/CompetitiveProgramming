from collections import deque
from bisect import bisect_right

for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    # 最強選手はだれで何番目なのか
    strongest_player = max(a)
    strongest_player_ind = a.index(strongest_player)
    # 先頭と末尾にしかアクセスしないため、それらにO(1)でアクセスできるdequeを使います。
    a = deque([(i+1, a[i]) for i in range(n)])
    # n-1ラウンド目までで勝利したラウンド
    wins = [[] for j in range(n)]
    for t in range(1, n+1):
        # ここからは試合の愚直シミュレーションです
        p1_ind, p1 = a.popleft()
        p2_ind, p2 = a.popleft()
        if p1 > p2:
            a.appendleft((p1_ind, p1))
            a.append((p2_ind, p2))
            # 勝った選手の配列にラウンドを追加します
            wins[p1_ind-1].append(t)
        else:
            a.appendleft((p2_ind, p2))
            a.append((p1_ind, p1))
            wins[p2_ind-1].append(t)
    
    # 質問に答えていきます
    for _ in range(q):
        i, k = map(int, input().split())
        # 選手番号は0-indexで処理しているので
        # １引いておきます
        i -= 1 
        if k < n:
            ans = bisect_right(wins[i], k)
            print(ans)
        else:
            if i == strongest_player_ind:
                print(len(wins[i]) + (k-n))
            else:
                print(len(wins[i]))