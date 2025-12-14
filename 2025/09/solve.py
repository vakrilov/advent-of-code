# %%
import os
from itertools import combinations

# f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")
# f = open(os.path.dirname(__file__) + "/sample2.txt", "r", encoding="utf-8")
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]
points = [(int(c[0]), int(c[1])) for c in (l.split(",") for l in lines)]

rects = list(combinations(points, 2))


def area(r1, r2):
    return (abs(r1[0] - r2[0]) + 1) * (abs(r1[1] - r2[1]) + 1)


print("part1:", max(area(r1, r2) for (r1, r2) in rects))


# %%

# ordered set of x coordinates for each row
x_set = set()
y_set = set()
for x, y in points:
    x_set.add(x)
    # x_set.add(x - 1)
    # x_set.add(x + 1)

    y_set.add(y)
    # y_set.add(y - 1)
    # y_set.add(y + 1)

x_map = list(x_set)
x_map.sort()

y_map = list(y_set)
y_map.sort()

points_remapped = [(x_map.index(x), y_map.index(y)) for x, y in points]

L = max(len(x_map), len(y_map)) + 2
board = [["." for _ in range(L)] for _ in range(L)]

points2 = points_remapped


# %%
for i in range(len(points2)):
    x1, y1 = points2[i]
    x2, y2 = points2[(i + 1) % len(points2)]

    symbol = "|" if x1 == x2 else "-"

    for x in range(min(x1, x2), max(x1, x2) + 1):
        board[y1][x] = symbol
    for y in range(min(y1, y2), max(y1, y2) + 1):
        board[y][x2] = symbol

for x, y in points2:
    board[y][x] = "#"

# print("\n".join("".join(row) for row in board))


for row in range(L):
    fill = False
    for col in range(L):
        if board[row][col] == "|":
            board[row][col] = "X"
            fill = not fill
        elif board[row][col] == "#":
            board[row][col] = "X"
            point_idx = points2.index((col, row))
            prev_point_y = points2[(point_idx - 1) % len(points2)][1]
            next_point_y = points2[(point_idx + 1) % len(points2)][1]

            max_y = max(prev_point_y, next_point_y)
            if row < max_y:
                fill = not fill
        elif board[row][col] == "-":
            board[row][col] = "X"

        if fill:
            board[row][col] = "X"


# print("\n".join("".join(row) for row in board))

# %%


def remap_coordinates(rect):
    (x1, y1), (x2, y2) = rect
    x1_remapped = x_map.index(x1)
    x2_remapped = x_map.index(x2)
    y1_remapped = y_map.index(y1)
    y2_remapped = y_map.index(y2)

    if x1_remapped > x2_remapped:
        x1_remapped, x2_remapped = x2_remapped, x1_remapped
    if y1_remapped > y2_remapped:
        y1_remapped, y2_remapped = y2_remapped, y1_remapped

    return (x1_remapped, y1_remapped), (x2_remapped, y2_remapped)


def print_board(board, rect):
    board_copy = [row.copy() for row in board]
    (x1_remapped, y1_remapped), (x2_remapped, y2_remapped) = remap_coordinates(rect)

    for row in range(y1_remapped, y2_remapped + 1):
        for col in range(x1_remapped, x2_remapped + 1):
            if board_copy[row][col] == "X":
                board_copy[row][col] = "*"
            else:
                board_copy[row][col] = "!"

    print("\n".join("".join(row) for row in board_copy))


rects.sort(key=lambda r: area(r[0], r[1]), reverse=True)

for rect in rects:
    (x1_remapped, y1_remapped), (x2_remapped, y2_remapped) = remap_coordinates(rect)

    all_filled = True
    for row in range(y1_remapped, y2_remapped + 1):
        for col in range(x1_remapped, x2_remapped + 1):
            if board[row][col] != "X":
                all_filled = False
                break
        if not all_filled:
            break
    # print("Checking rect:", (x1, y1), (x2, y2), "all filled:", all_filled)

    # print_board(board, rect)

    if all_filled:
        print("part2:", area(*rect))
        break

# %%
