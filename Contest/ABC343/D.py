
d = {}

N, T = map(int, input().split())
d[0] = N
li = [(0) for _ in range(N)]

for _ in range(T):
    a, b = map(int, input().split())
    a -= 1
    cur = li[a]
    d[cur] -= 1
    if d[cur] == 0:
        del d[cur]
    
    li[a] += b

    nex = li[a]
    
    if nex in d:
        d[nex] += 1
    else:
        d[nex] = 1
    
    print(len(d))
    