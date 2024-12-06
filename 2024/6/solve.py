# %%
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

linesRaw = [l.removesuffix("\n") for l in f.readlines()]

L = len(linesRaw)

lines = [list(l) for l in linesRaw]
print(lines)

# %%
directions = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0),
}

pos = (0, 0)
dir = 0

for y, line in enumerate(lines):
    if "^" in line:
        pos = (line.index("^"), y)
        lines[pos[1]][pos[0]] = "X"
        break

print(pos)
# %%


def p():
    for l in lines:
        print(l)
    print()


def move():
    global dir
    global pos
    dx, dy = directions[dir]
    nx, ny = pos[0] + dx, pos[1] + dy
    if nx < 0 or nx >= L or ny < 0 or ny >= L:
        return False

    if lines[ny][nx] == "#":
        dir = (dir + 1) % 4
    else:
        lines[ny][nx] = "X"
        pos = nx, ny

    return True


while move():
    pass

result = sum([l.count("X") for l in lines])
print("part1:", result)

# %%
