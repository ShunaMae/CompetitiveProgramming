# 3, 14, 15 

# 210, 200, 100

# (3, 14) 
# (3, 15)
# (14, 15)

# 3 * 200 = 600 
# 14 * 100 = 1400 

# 3 * 0 = 0
# 14 * 1 = 14 
# 15 * 2 = 30 

N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

digits = [0] * N 
digits[-1] = 10 ** len(str(A[-1]))

for i in range(N-2, -1, -1):
    digits[i] = 10 ** len(str(A[i])) + digits[i+1]

ans = 0 

for j in range(N):
    ans += A[j] * j % MOD
    if j != N-1:
        ans += A[j] * digits[j+1] % MOD
    
    ans %= MOD

print(ans)
