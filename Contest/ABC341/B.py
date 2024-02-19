N = int(input())
A = list(map(int, input().split()))
st = [list(map(int, input().split())) for _ in range(N-1)]

for i in range(N-1):
    num = A[i] // st[i][0]
    A[i+1] += num * st[i][1]

print(A[-1])