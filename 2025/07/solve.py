# %%
import os

# f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]
ROWS = len(lines)
COLS = len(lines[0])

paths = [[0] * len(l) for l in lines]
paths[0][lines[0].index("S")] = 1
splits = 0

for row in range(ROWS - 1):
    next_paths = paths[row + 1]
    for col in range(COLS):
        current_paths = paths[row][col]
        if current_paths > 0:
            if lines[row + 1][col] == "^":
                splits += 1
                next_paths[col - 1] += current_paths
                next_paths[col + 1] += current_paths
            else:
                next_paths[col] += current_paths

print("part1:", splits)
print("part2:", sum(paths[-1]))
# %%
