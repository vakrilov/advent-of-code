from itertools import product
import os
from datetime import datetime

f = open(os.path.dirname(__file__) +
         "/inputs/input5000.txt", "r", encoding="utf-8")

grid = [[int(x) for x in line.removesuffix("\n")] for line in f.readlines()]
L = len(grid)
start_time = datetime.now()


def left_to_right(row): return ((row, i, grid[row][i]) for i in range(L))
def right_to_left(row): return ((row, i, grid[row][i]) for i in range(L-1, -1, -1))
def up_to_down(col): return ((i, col, grid[i][col]) for i in range(L))
def down_to_up(col): return ((i, col, grid[i][col]) for i in range(L-1, -1, -1))


def calc_scores(direction):
    scores = [[0] * L for _ in range(L)]
    for position in range(L):
        tmp_scores = [0] * 10
        for (row, col, value) in direction(position):
            scores[row][col] = tmp_scores[value]
            for i in range(10):
                tmp_scores[i] = tmp_scores[i] + 1 if i > value else 1
    return scores


scores_left_to_right = calc_scores(left_to_right)
scores_right_to_left = calc_scores(right_to_left)
scores_up_to_down = calc_scores(up_to_down)
scores_down_to_up = calc_scores(down_to_up)


def score(y: int, x: int):
    return scores_left_to_right[y][x] \
        * scores_right_to_left[y][x] \
        * scores_up_to_down[y][x] \
        * scores_down_to_up[y][x]


result = max(score(y, x) for y, x in product(range(L), range(L)))
print("result:", result, f' Duration: {(datetime.now() - start_time)}')
