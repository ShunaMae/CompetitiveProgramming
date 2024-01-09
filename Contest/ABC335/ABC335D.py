def create_spiral_matrix(N):
    matrix = [[0] * N for _ in range(N)]

    # 左上から始める
    x, y = 0, 0

    # 最初は右方向への移動
    dx, dy = 1, 0

    # Fill the matrix
    for i in range(1, n * n + 1):

        matrix[y][x] = i

        # not(次のマスが存在する、かつまだ埋められていないとき)
        # つまり「次のマスが存在しなかったりもう埋められていたとき」
        if not (0 <= x + dx < N and 0 <= y + dy < N and matrix[y+dy][dx+x] == 0):
            # 方向を変えます
            dx, dy = -dy, dx
        
        x += dx
        y += dy

    center = N // 2
    matrix[center][center] = 'T'

    return matrix

matrix = create_spiral_matrix(int(input()))
for row in matrix:
    print(*row)
