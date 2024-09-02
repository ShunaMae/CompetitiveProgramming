N = int(input())
A = list(map(int, input().split()))

# dp配列を初期化
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for k in range(i + 1):
        dp[i][k] = dp[i-1][k]  # モンスターを殺さない場合
        if k > 0:
            if k % 2 == 1:  # 奇数回目の殺害
                dp[i][k] = max(dp[i][k], dp[i-1][k-1] + A[i-1])
            else:  # 偶数回目の殺害
                dp[i][k] = max(dp[i][k], dp[i-1][k-1] + 2 * A[i-1])

# 最終結果を計算
result = max(dp[N])
print(result)