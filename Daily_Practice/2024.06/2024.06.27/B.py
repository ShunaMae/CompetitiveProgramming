def find_final_position(H, W, grid):
    i, j = 0, 0
    
    visited = set()

    while True:

        if (i, j) in visited:
            return -1 
        visited.add((i, j))
        
        direction = grid[i][j]
        
        # 移動先を決定
        if direction == 'U' and i != 0:
            i -= 1
        elif direction == 'D' and i != H - 1:
            i += 1
        elif direction == 'L' and j != 0:
            j -= 1
        elif direction == 'R' and j != W - 1:
            j += 1
        else:
            return [i + 1, j + 1]  

H, W = map(int, input().split())
grid = []
for _ in range(H):
    grid.append(input())

ans =  find_final_position(H, W, grid)

if ans == -1:
    print(-1)
else:
    print(*ans)