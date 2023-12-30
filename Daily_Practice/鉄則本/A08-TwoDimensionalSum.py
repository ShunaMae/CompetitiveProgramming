def main():
    H, W = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(H)]
    Grid = [[(0) for _ in range(W+1)] for _ in range(H+1)]
    for c in range(1, W):
        for r in range()

    print(Grid)
    Q = int(input())
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        a -= 1
        b -= 1
        c -= 1
        d -= 1
        print(Grid[c][d] - Grid[a][b])

main()
    