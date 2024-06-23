t = int(input())

for _ in range(t):
    N, M = map(int, input().split())

    grid = []
    for _ in range(N):
        cur_row = list(map(int, input().split()))
        grid.append(cur_row)

    def get_max(grid, row, col):
        
        to_check = [
            (row-1, col),  # 上
            (row+1, col),  # 下
            (row, col-1),  # 左
            (row, col+1)   # 右
        ]

        max_val = 0
        for r, c in to_check:
            if 0 <= r < N and 0 <= c < M:
                max_val = max(max_val, grid[r][c])
        
        return max_val 
    
    ans = 0

    for r in range(N):
        for c in range(M):
            cur = grid[r][c]
            max_adj = get_max(grid, r, c)
            if cur > max_adj:
                grid[r][c] -= (cur-max_adj)
    
    
    for i in range(N):
        print(*grid[i])