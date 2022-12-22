import os
# N, f = 50, open(os.path.dirname(__file__) +
#                 "/input.txt", "r", encoding="utf-8")
# b1 = [(4, 0), (0, 1), (2, 1), (3, 2), (1, 3)]
# b2 = [(3, 0), (4, 2), (0, 4), (2, 4)]

N, f = 4, open(os.path.dirname(__file__) +
               "/sample2.txt", "r", encoding="utf-8")
b1 = []
b2 = []

MAX = 5 * N
directions = (
    (1, 0),  # right
    (0, 1),  # down
    (-1, 0),  # left
    (0, -1)  # up
)

direction_sym = [">", "v", "<", "^"]

lines = [l.removesuffix("\n") for l in f.readlines()]


def read_input():
    g = [[" "] * MAX for _ in range(MAX)]
    for row, line in enumerate(lines[: -2]):
        g[row][0: len(line)] = list(line)

    for col, row in b1:
        for i in range(N):
            g[row * N + i][col * N + i] = "\\"

    for col, row in b2:
        for i in range(N):
            g[row * N + N - 1 - i][col * N + i] = "/"

    return g


grid = read_input()


def find_index(lst, func):
    for i, val in enumerate(lst):
        if func(val):
            return i


# /
bounce1 = {
    0: 1,
    1: 0,
    2: 3,
    3: 2
}

# \
bounce2 = {
    0: 3,
    1: 2,
    2: 1,
    3: 0
}


def generate_coords(x, y, d, g):
    while True:
        x, y = (x+directions[d][0]) % MAX, (y+directions[d][1]) % MAX

        if g[y][x] == " " or g[y][x] == "/" or g[y][x] == "\\":
            while g[y][x] == " " or g[y][x] == "/" or g[y][x] == "\\":
                if g[y][x] == "/":
                    d = bounce1[d]
                elif g[y][x] == "\\":
                    d = bounce2[d]

                x, y = (x+directions[d][0]) % MAX, (y+directions[d][1]) % MAX

        yield (x, y, d)


curr_x = find_index(grid[0], lambda x: x == ".")
curr_y = 0
curr_dir = 0
steps = 0


def go():
    global curr_x, curr_y, curr_dir, steps

    gen = generate_coords(curr_x, curr_y, curr_dir, grid)

    for _ in range(steps):
        new_x, new_y, new_dir = next(gen)
        if grid[new_y][new_x] != "#":
            grid[curr_y][curr_x] = direction_sym[curr_dir]
            curr_x, curr_y, curr_dir = new_x, new_y, new_dir
        else:
            break

    # p()
    steps = 0


def p():
    for row in range(len(grid)):
        print("".join(grid[row]))
    print()
    print()


p()
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
