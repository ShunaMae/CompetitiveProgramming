N = int(input())
for i in range(N):
    s = list(map(int, input().split()))
    ans = []
    for j in range(N):
        if s[j] == 1:
            ans.append(j+1)
    print(*ans)