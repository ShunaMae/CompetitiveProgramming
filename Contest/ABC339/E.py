N, D = map(int, input().split())
A = list(map(int, input().split()))

dp = [(0) for _ in range(N)]
dp[0] = 1

for i in range(N):
    dp[i] = 