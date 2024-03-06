#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (List[List[int]]): A 2D array representing the grid.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # If current cell is land
                perimeter += 4  # Each land cell contributes 4 edges initially
                
                # Check left adjacent cell
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Deduct 2 for shared edge
                
                # Check top adjacent cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Deduct 2 for shared edge

    return perimeter

# Test the function with the provided example
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))
