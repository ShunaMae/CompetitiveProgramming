def create_spiral_matrix(n):
    # Initialize the matrix with zeros
    matrix = [[0] * n for _ in range(n)]

    # Define the starting point
    x, y = 0, 0
    dx, dy = 0, 1  # Initial direction: moving right

    # Fill the matrix
    for i in range(1, n * n + 1):
        matrix[x][y] = i
        # Check if the next step is within bounds and the cell is not yet filled
        if not (0 <= x + dx < n and 0 <= y + dy < n and matrix[x + dx][y + dy] == 0):
            # Change direction: right -> down -> left -> up
            dx, dy = dy, -dx
        x += dx
        y += dy

    # Replace the central element with 'T'
    center = n // 2
    matrix[center][center] = 'T'

    return matrix

# Example usage
spiral_matrix = create_spiral_matrix(int(input()))
for row in spiral_matrix:
    print(*row)
