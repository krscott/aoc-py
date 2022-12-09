#!python
from __future__ import annotations

with open("input/08.txt") as f:
    grid: list[list[int]] = [[int(x) for x in row.strip()] for row in f.readlines()]

    visible: list[list[int]] = [[0 for _ in row] for row in grid]

    num_rows = len(grid)
    num_cols = len(grid[0])

    # From left
    for r in range(num_rows):
        visible[r][0] = 1
        max_height = grid[r][0]
        for c in range(1, num_cols):
            h = grid[r][c]
            if h > max_height:
                visible[r][c] = 1
                max_height = h

    # From right
    for r in range(num_rows):
        visible[r][-1] = 1
        max_height = grid[r][-1]
        for c in reversed(range(1, num_cols)):
            h = grid[r][c]
            if h > max_height:
                visible[r][c] = 1
                max_height = h

    # From top
    for c in range(1, num_cols):
        visible[0][c] = 1
        max_height = grid[0][c]
        for r in range(num_rows):
            h = grid[r][c]
            if h > max_height:
                visible[r][c] = 1
                max_height = h

    # From bottom
    for c in range(1, num_cols):
        visible[-1][c] = 1
        max_height = grid[-1][c]
        for r in reversed(range(num_rows)):
            h = grid[r][c]
            if h > max_height:
                visible[r][c] = 1
                max_height = h

    # print('\n'.join(''.join(str(c) for c in row) for row in visible))
    print(sum(sum(row) for row in visible))
