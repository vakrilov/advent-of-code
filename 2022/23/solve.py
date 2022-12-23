import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")
lines = [l.removesuffix("\n") for l in f.readlines()]

N = len(lines)
BUFFER = 60
grid = [["."] * (N + 2*BUFFER) for _ in range(N + 2*BUFFER)]

dirs = (
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0)
)

dirs_check = (
    ((-1, -1), (0, -1), (1, -1)),
    ((-1, 1), (0, 1), (1, 1)),
    ((-1, -1), (-1, 0), (-1, 1)),
    ((1, -1), (1, 0), (1, 1))
)


def p():
    for l in grid:
        print("".join(l))
    print()
    print()


def should_move(x, y):
    c = 0
    for x1 in range(x-1, x+2):
        for y1 in range(y-1, y+2):
            c += 1 if grid[y1][x1] == "#" else 0
    return c > 1


def can_move(x, y, d):
    for p in dirs_check[d]:
        if grid[y + p[1]][x + p[0]] == "#":
            return False
    return True


def turn(d):
    elves = []
    new_elves_positions = dict()
    new_positions_count = dict()

    # get elves positions
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "#":
                elves.append((x, y))

    # decide move for each elf
    for e in elves:
        if not should_move(*e):
            continue

        for try_direction in [d % 4, (d+1) % 4, (d+2) % 4, (d+3) % 4]:
            if can_move(*e, try_direction):
                new_pos = (e[0] + dirs[try_direction][0],
                           e[1] + dirs[try_direction][1])
                new_elves_positions[e] = new_pos
                if new_pos in new_positions_count:
                    new_positions_count[new_pos] += 1
                else:
                    new_positions_count[new_pos] = 1
                break

    # execute move if no collision
    for e in elves:
        if e in new_elves_positions:
            new_e = new_elves_positions[e]
            if new_positions_count[new_e] == 1:
                grid[e[1]][e[0]] = "."
                grid[new_e[1]][new_e[0]] = "#"

    return len(new_positions_count) > 0


for row, line in enumerate(lines):
    grid[BUFFER + row][BUFFER:BUFFER+len(line)] = line


def answer_part1():
    min_r, min_c = 1000, 1000
    max_r, max_c = -1, -1
    elves_count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "#":
                elves_count += 1
                min_r, max_r = min(r, min_r), max(r, max_r)
                min_c, max_c = min(c, min_c), max(c, max_c)
    return (max_r - min_r + 1) * (max_c - min_c + 1) - elves_count


for turn_num in range(10000):
    if not turn(turn_num % 4):
        break

    if turn_num == 9:
        print("Part 1:", answer_part1())
        p()


print("Part 2:", turn_num + 1)
p()
