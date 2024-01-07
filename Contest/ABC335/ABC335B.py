N = int(input())
ans = []
for x in range(N+1):
    for y in range(N+1):
        for z in range(N+1):
            if x+y+z <= N:
                ans.append([x,y,z])
ans = sorted(ans)
for i in ans:
    print(*i)
