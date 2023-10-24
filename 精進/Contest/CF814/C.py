import sys;input=sys.stdin.readline
T, = map(int, input().split())
for _ in range(T):
    N, Q = map(int, input().split())
    X = list(map(int, input().split()))
    X = [(i+1, X[i]) for i in range(N)]
    X = X[::-1]
    tmp = [0]*N
    Y = [10**18]*(N+1)
    for l in range(1, N):
        (i, x) = X.pop()
        (j, y) = X.pop()
        if x > y:
            Y[j] = l
            X.append((i, x))
        else:
            Y[i] = l
            X.append((j, y))

#    print(Y)
    for _ in range(Q):
        i, k = map(int, input().split())
        x = Y[i]-max((i-1), 1)
        x = min(k+1-max(i-1,1), x)
        x = max(0, x)
        print(x)

