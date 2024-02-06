N = int(input())
G = [list(input()) for _ in range(N)]


from collections import deque

def is_valid_move(N, pos, grid):
    """Check if the move is valid: within the grid and not into an obstacle."""
    return 0 <= pos[0] < N and 0 <= pos[1] < N and grid[pos[0]][pos[1]] != '#'

def bfs_min_moves(N, grid):
    # Find the initial positions of the players
    player_positions = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 'P']

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(player_positions[0], player_positions[1], 0)])
    visited = set(((player_positions[0], player_positions[1]),))

    while queue:
        p1, p2, moves = queue.popleft()
        if p1 == p2:
            return moves

        for d in directions:
            new_p1 = (p1[0] + d[0], p1[1] + d[1]) if is_valid_move(N, (p1[0] + d[0], p1[1] + d[1]), grid) else p1
            new_p2 = (p2[0] + d[0], p2[1] + d[1]) if is_valid_move(N, (p2[0] + d[0], p2[1] + d[1]), grid) else p2
            newState = (new_p1, new_p2)

            if newState not in visited:
                visited.add(newState)
                queue.append((new_p1, new_p2, moves + 1))

    return -1



# Calculate minimum moves
min_moves = bfs_min_moves(N, G)
print(min_moves)
