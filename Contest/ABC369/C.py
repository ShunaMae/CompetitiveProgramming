N = int(input())
A = list(map(int, input().split()))

ans = 0

if N == 1:
    ans = 1
else:
    length = 2 
    for i in range(2, N):
        if A[i] - A[i-1] == A[i-1] - A[i-2]:
            length += 1 
        else:
            ans += (length - 1) * (length - 2) // 2
            length = 2 
    
    ans += (length - 1) * (length - 2) // 2
    ans += N + N - 1

print(ans)