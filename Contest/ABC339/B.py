H, W, N = map(int, input().split())

grid = [["." for _ in range(W)] for _ in range(H)]
cur_row = 0
cur_col = 0
dir = (-1, 0)  # Initially moving up

for i in range(N):
    if grid[cur_row][cur_col] == ".":
        grid[cur_row][cur_col] = "#"  # Fill the current cell
        # Change direction to clockwise
        if dir == (-1, 0):
            dir = (0, 1)
        elif dir == (0, 1):
            dir = (1, 0)
        elif dir == (1, 0):
            dir = (0, -1)
        elif dir == (0, -1):
            dir = (-1, 0)
    else:
        grid[cur_row][cur_col] = "."  # Clear the current cell
        # Change direction anticlockwise
        if dir == (-1, 0):
            dir = (0, -1)
        elif dir == (0, -1):
            dir = (1, 0)
        elif dir == (1, 0):
            dir = (0, 1)
        elif dir == (0, 1):
            dir = (-1, 0)

    # Move to the next cell based on the direction
    cur_row = (cur_row + dir[0]) % H
    cur_col = (cur_col + dir[1]) % W

# Printing the grid
for row in grid:
    print(''.join(row))
