
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 


# 入力
N = is_int()
G = [[] for _ in range(N)]
for i in range(N-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    print("AB", A, B)
    G[A].append(B)
    G[B].append(A)
    print(G)


dist = [-1] * N


nodes = [[] for i in range(N)]


dist[0] = 0
nodes[0] = [0]
ans = []

for k in range(1, N):
    for v in nodes[k - 1]:
        for next_v in G[v]:
            if dist[next_v] != -1:
                ans.append(v)
                continue
            dist[next_v] = dist[v] + 1
            nodes[k].append(next_v)
            ans.append(next_v)

print(ans)
for k in range(N):
    # 頂点番号を小さい順に
    nodes[k].sort()

    # 出力
    print(*nodes[k])
