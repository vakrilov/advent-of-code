from itertools import product
import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

grid = [[int(x) for x in line.removesuffix("\n")] for line in f.readlines()]
L = len(grid)

# generates the height of trees starting from grid[y][x]:
def up(y, x): return (grid[i][x] for i in range(y-1, -1, -1))
def down(y, x): return (grid[i][x] for i in range(y+1, L))
def left(y, x): return (grid[y][i] for i in range(x-1, -1, -1))
def right(y, x): return (grid[y][i] for i in range(x+1, L))


def visible_from_direction(y: int, x: int, direction) -> bool:
    return all(val < grid[y][x] for val in direction(y, x))


def visible(y: int, x: int) -> bool:
    return visible_from_direction(y, x, up) \
        or visible_from_direction(y, x, down) \
        or visible_from_direction(y, x, left) \
        or visible_from_direction(y, x, right)


def count_trees(y: int, x: int, direction) -> int:
    cnt = 0
    for height in direction(y, x):
        cnt += 1
        if height >= grid[y][x]:
            break
    return cnt


def score(y: int, x: int):
    return count_trees(y, x, up) \
        * count_trees(y, x, down) \
        * count_trees(y, x, left) \
        * count_trees(y, x, right)


print("Part 1:", sum(visible(y, x) for y, x in product(range(L), range(L))))
print("Part 2:", max(score(y, x) for y, x in product(range(L), range(L))))
