N = int(input())
A = list(map(int, input().split()))

mi = 0
ma = -10**18
cnt = 0
for i in range(N):
    cnt += A[i]
    mi = min(mi, cnt)
    ma = max(ma, cnt)


print(abs(mi)+cnt)