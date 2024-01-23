# https://atcoder.jp/contests/arc006/tasks/arc006_2

N, L = map(int, input().split())
G = [list(input()) for _ in range(L)]
y = input()

print(G)

for pos in range(N):
    cur = pos*2
    for i in range(L):
        # print(cur)
        if cur > 0:
            if G[i][cur-1] == "-":
                cur -= 2
        # print(G[i])
        # print(G[i][cur+1])
        if cur < (N)*2-1:
            # print(G[i][cur+1], "sign")
            if G[i][cur+1] == "-":
                cur += 2
    print("end")

    
    print(cur)

