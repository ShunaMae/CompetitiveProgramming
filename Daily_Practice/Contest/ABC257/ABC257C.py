from operator import itemgetter
from bisect import bisect_left
def solve():
    N = int(input())
    S = list(input())
    sorted_s = sorted(S)
    adult = bisect_left(sorted_s, '1') + 1
    children = N - adult 
    W = list(map(int, input().split()))
    li = []
    for gen, wei in zip(S, W):
        li.append([gen, wei]) 
    li = sorted(li, key = itemgetter(1))
    right = 0
    dp = [[10**7, 10**7, 10**7] for _ in range(N)]
    if li[0][0] == '1':
        dp[0][0] = children
        dp[0][1] = 1
        dp[0][2] = dp[0][0] + dp[0][1]
        right = max(right, N - dp[0][2])
    else:
        dp[0][0] = 1
        dp[0][1] = 0
        dp[0][2] = dp[0][0] + dp[0][1]
        right = max(right, N - dp[0][2])   
    for person in range(1, N):
        if li[person][0] == '0':
            dp[person][0] = max(dp[person-1][0] - 1, 0)
            dp[person][1] = dp[person-1][1]
            dp[person][2] = dp[person][0] + dp[person][1]
            right = max(right, N - dp[person][2])
        else: 
            dp[person][0] = dp[person-1][0] 
            dp[person][1] = min(dp[person-1][1] + 1, adult)
            dp[person][2] = dp[person][0] + dp[person][1]
            right = max(right, N - dp[person][2])
    return right

print(solve())