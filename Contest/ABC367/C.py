N, K = map(int, input().split())
R = list(map(int, input().split()))

from itertools import product

ans = []
for i in product(*(range(1, r+1) for r in R)):
    if sum(i) % K == 0:
        ans.append(i)

ans = sorted(ans)
for a in ans:
    print(*a)


