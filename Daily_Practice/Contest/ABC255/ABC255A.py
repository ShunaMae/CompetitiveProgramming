R, C = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
if R == 1:
    ans = A[C-1]
else:
    ans = B[C-1]

print(ans)