H, W, N = map(int, input().split())
T = list(input())
G = [input() for _ in range(H)]

def find_possible_landing_spots(grid, movements):
    H, W = len(grid), len(grid[0])
    possible_spots = 0

    # 移動方向をマッピング
    direction_map = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

    # グリッド上の各陸地マスについて検討
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':  # 陸のマスの場合
                x, y = i, j
                valid = True
                # 移動手順を逆順に適用
                for move in reversed(movements):
                    dx, dy = direction_map[move]
                    x, y = x - dx, y - dy  # 逆移動
                    # 移動後のマスがグリッド外または海の場合
                    if not (0 <= x < H and 0 <= y < W) or grid[x][y] == '#':
                        valid = False
                        break
                if valid:
                    possible_spots += 1

    return possible_spots

print(find_possible_landing_spots(G, T))