from itertools import product
import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")


lines = [l.removesuffix("\n") for l in f.readlines()]
ROWS = len(lines)
COLS = len(lines[0])

grid =[[0] * COLS for _ in range(ROWS)]
for (row, line) in enumerate(lines):
    for (col, ch) in enumerate(line):
        if ch == "S":
            grid[row][col] = 0
            start = (row, col)
        elif ch == "E":
            grid[row][col] = 25
            end = (row, col)
        else:
            grid[row][col] = ord(ch)-ord('a')

path_lengths =[[-1] * COLS for _ in range(ROWS)]
queue = [end + (0,)]
visited = set()
visited.add(end)

def process(r, c, height, depth):
    # in bounds
    if not(0 <= r and r < ROWS and 0 <= c and c < COLS): 
        return

    # at most one step down
    if grid[r][c] < height - 1:
        return

    # not visited already
    if (r, c) in visited:
        return

    visited.add((r, c))
    queue.append((r, c, depth + 1))


part1_answer = -1
part2_answer = -1
while len(queue) > 0:
    row, col, depth = queue.pop(0)
    path_lengths[row][col] = depth

    height = grid[row][col]

    if part2_answer < 0 and height == 0:
        part2_answer = depth # first point with elevation 0 reached

    if (row, col) == start:
        part1_answer = depth
        break

    process(row-1, col, height, depth)
    process(row+1, col, height, depth)
    process(row, col-1, height, depth)
    process(row, col+1, height, depth)

print("Part 1:", part1_answer)
print("Part 2:", part2_answer)
