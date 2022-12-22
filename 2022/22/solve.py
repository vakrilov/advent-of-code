import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

directions = (
    (1, 0),  # right
    (0, 1),  # down
    (-1, 0),  # left
    (0, -1)  # up
)

direction_sym = [">", "V", "<", "^"]

lines = [l.removesuffix("\n") for l in f.readlines()]
ROW = len(lines) - 2
COL = max(len(l) for l in lines[:-1])


def read_input():
    g = []
    for line in lines[: -2]:
        g.append(list(line) + [' '] * (COL - len(line)))
    return g


grid = read_input()


def find_index(lst, func):
    for i, val in enumerate(lst):
        if func(val):
            return i


def generate_coords(x, y, d, g):
    while True:
        x, y = (x+d[0]) % COL, (y+d[1]) % ROW
        while g[y][x] == " ":
            x, y = (x+d[0]) % COL, (y+d[1]) % ROW
        yield (x, y)


curr_x = find_index(grid[0], lambda x: x == ".")
curr_y = 0
curr_dir = 0
steps = 0


def go():
    global curr_x, curr_y, curr_dir, steps

    gen = generate_coords(curr_x, curr_y, directions[curr_dir], grid)

    for _ in range(steps):
        new_x, new_y = next(gen)
        if grid[new_y][new_x] != "#":
            grid[curr_y][curr_x] = direction_sym[curr_dir]
            curr_x, curr_y = new_x, new_y
        else:
            break

    # p()
    steps = 0


def p():
    for row in range(ROW):
        print("".join(grid[row]))
    print()
    print()


for ch in lines[-1]:
    if ch == "R":
        go()
        curr_dir = (curr_dir + 1) % 4
    elif ch == "L":
        go()
        curr_dir = (curr_dir - 1) % 4
    else:
        steps *= 10
        steps += int(ch)
go()

answer = 1000*(curr_y+1) + 4*(curr_x+1) + curr_dir
print(answer)
