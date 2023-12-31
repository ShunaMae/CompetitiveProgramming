def main():
    H, W = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(H)]
    Grid = []
    for _ in range(H):
        li = list(map(int, input().split()))
        x = [li[0]]
        print(li)
        for i in range(1, W):
            x.append(x[-1]+li[i])
        Grid.append(x)
    
    for c in range(W):
        for r in range(1, H):
            Grid[r][c] += Grid[r-1][c]
    
    print(Grid)

    Q = int(input())
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
    





main()
    