import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")
lines = [l.removesuffix("\n") for l in f.readlines()]
ROW = len(lines) - 2
COL = len(lines[0]) - 2

start = (0, -1)
target = (COL - 1, ROW)

right, left, up, down = [], [], [], []

for row, line in enumerate(lines[1:-1]):
    for col, ch in enumerate(line[1:-1]):
        match ch:
            case ">":
                right.append([col, row])
            case "<":
                left.append([col, row])
            case "^":
                up.append([col, row])
            case "v":
                down.append([col, row])


def fill(current, direction):
    return direction if current == "." else str(int(current) if current.isdecimal() else 1 + 1)


def get_grid():
    grid = [["."] * COL for _ in range(ROW)]
    for x, y in right:
        grid[y][x] = fill(grid[y][x], ">")

    for x, y in left:
        grid[y][x] = fill(grid[y][x], "<")

    for x, y in up:
        grid[y][x] = fill(grid[y][x], "^")

    for x, y in down:
        grid[y][x] = fill(grid[y][x], "v")
    return grid


def p(grid):
    for l in grid:
        print("".join(l))
    print()


def move_blizzards():
    for d in right:
        d[0] += 1
        d[0] %= COL

    for d in left:
        d[0] -= 1
        d[0] %= COL

    for d in up:
        d[1] -= 1
        d[1] %= ROW

    for d in down:
        d[1] += 1
        d[1] %= ROW


def is_valid(p):
    if p == start or p == target:
        return True

    return 0 <= p[0] and p[0] < COL \
        and 0 <= p[1] and p[1] < ROW


def solve():
    positions = set()
    positions.add(start)
    turn = 1
    while True:
        move_blizzards()
        grid = get_grid()

        next_positions = set()
        for pos in positions:
            variants = ((pos[0], pos[1]), (pos[0]-1, pos[1]), (pos[0]+1, pos[1]),
                        (pos[0], pos[1]-1), (pos[0], pos[1]+1))
            for variant in variants:
                if is_valid(variant) and (variant == start or variant == target or grid[variant[1]][variant[0]] == "."):
                    next_positions.add(variant)

        if target in next_positions:
            return turn

        positions = next_positions
        turn += 1


answer = solve()
print("Part 1:", answer)

start, target = target, start
answer += solve()
start, target = target, start
answer += solve()
print("Part 1:", answer)
