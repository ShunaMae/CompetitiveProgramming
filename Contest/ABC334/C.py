def main():
    N, K = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    
    # 貪欲に前からペアを作っていくとき
    greedy_pair = 0
    # 0番目を飛ばしてペアを作るとき
    skip = 0
    for i in range(0, K-1, 2):
        greedy_pair += A[i+1]-A[i]
        if i+2 < K:
            skip += A[i+2]-A[i+1]
    
    # あり得る奇妙さの合計のリスト
    skipped_list = [skip]

    # 偶数なら前から貪欲に
    if K%2 == 0:
        print(greedy_pair)
    # 奇数なら除外する靴下を全探索
    else:
        for j in range(1, K, 2):
            # ペアを変更
            skip = skip - (A[j+1] - A[j]) + (A[j] - A[j-1])
            skipped_list.append(skip)

        # Aの要素数が１の時はその靴下を除外するだけ
        if len(skipped_list) == 0:
            print(0)
        else:
            print(min(skipped_list))
            


main()
