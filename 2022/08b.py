#!python
from __future__ import annotations

with open("input/08.txt") as f:
    grid: list[list[int]] = [[int(x) for x in row.strip()] for row in f.readlines()]

    num_rows = len(grid)
    num_cols = len(grid[0])
    max_score = 0

    for r in range(num_rows):
        for c in range(num_cols):
            height = grid[r][c]

            # look left
            left_score = 0
            for c2 in range(c - 1, -1, -1):
                left_score += 1
                if grid[r][c2] >= height:
                    break

            # look right
            right_score = 0
            for c2 in range(c + 1, num_cols):
                right_score += 1
                if grid[r][c2] >= height:
                    break

            # look up
            up_score = 0
            for r2 in range(r - 1, -1, -1):
                up_score += 1
                if grid[r2][c] >= height:
                    break

            # look down
            down_score = 0
            for r2 in range(r + 1, num_rows):
                down_score += 1
                if grid[r2][c] >= height:
                    break

            max_score = max(left_score * right_score * up_score * down_score, max_score)

    print(max_score)
