N, K = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
ans = 10**18

# print(A)
length = N-K
for i in range(K+1):
    # print(A[i+length-1], A[i], i+N-K-1)
    diff = A[i+length-1] - A[i]
    ans = min(ans, diff)

print(ans)
