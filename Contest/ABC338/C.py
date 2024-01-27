N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_A = 10**18

for i in range(N):
    if A[i] == 0:
        continue
    max_A = min(max_A, Q[i]//A[i])

ans = 0

for j in range(max_A+1):
    max_B = 10**18
    for ing in range(N):
        if B[ing] == 0:
            continue
        left = Q[ing] - A[ing] * j
        b_cnt = left // B[ing]
        max_B = min(max_B, b_cnt)
    
    ans = max(ans, j+max_B)

print(ans)
