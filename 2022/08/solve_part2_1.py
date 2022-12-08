from itertools import product
import os
from datetime import datetime

f = open(os.path.dirname(__file__) +
         "/inputs/input5000.txt", "r", encoding="utf-8")

grid = [[int(x) for x in line.removesuffix("\n")] for line in f.readlines()]
L = len(grid)

start_time = datetime.now()


def up(y, x): return (grid[i][x] for i in range(y-1, -1, -1))
def down(y, x): return (grid[i][x] for i in range(y+1, L))
def left(y, x): return (grid[y][i] for i in range(x-1, -1, -1))
def right(y, x): return (grid[y][i] for i in range(x+1, L))


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


result = max(score(y, x) for y, x in product(range(L), range(L)))
print("result:", result, f' Duration: {(datetime.now() - start_time)}')
