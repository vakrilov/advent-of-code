import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]
trail = [["."] * len(lines[0]) for _ in range(len(lines))]

ROWS = len(lines)
COLS = len(lines[0])


def print_trail():
    for l in trail:
        print("".join(l))
    print()


start = (0, 0)
for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] == "S":
            start = (r, c)


def go(pos):
    # print(pos)
    # print_trail()
    pipe = lines[pos[0]][pos[1]]
    fr = pos[2]

    go_up = (pos[0] - 1, pos[1], "d")
    go_down = (pos[0] + 1, pos[1], "u")
    go_left = (pos[0], pos[1] - 1, "r")
    go_right = (pos[0], pos[1] + 1, "l")

    if pipe == "|":
        return go_up if fr == "d" else go_down

    if pipe == "-":
        return go_left if fr == "r" else go_right

    if pipe == "L":
        return go_right if fr == "u" else go_up

    if pipe == "J":
        return go_left if fr == "u" else go_up

    if pipe == "7":
        return go_left if fr == "d" else go_down

    if pipe == "F":
        return go_right if fr == "d" else go_down


steps = 1
current = (start[0] + 1, start[1], "u")
trail[current[0]][current[1]] = current[2]

while True:
    current = go(current)
    trail[current[0]][current[1]] = current[2]
    steps += 1
    if lines[current[0]][current[1]] == "S":
        break

print("part1:", steps / 2)

stack = []
visited = set()

def addIfGood(r, c):
    if (r, c) in visited:
        return

    if r >= 0 and r < ROWS and c >= 0 and c < COLS and trail[r][c] == ".":
        visited.add((r, c))
        stack.append((r, c))


polarity = 1
for r in range(len(trail)):
    for c in range(len(trail[r])):
        dir = trail[r][c]
        if trail[r][c] == "u":
            addIfGood(r, c - polarity)
            addIfGood(r - 1, c - polarity)
        elif trail[r][c] == "d":
            addIfGood(r, c + polarity)
            addIfGood(r + 1, c + polarity)
        elif trail[r][c] == "l":
            addIfGood(r + polarity, c)
            addIfGood(r + polarity, c - 1)
        elif trail[r][c] == "r":
            addIfGood(r - polarity, c)
            addIfGood(r - polarity, c + 1)

while len(stack) > 0:
    current = stack.pop()
    trail[current[0]][current[1]] = "X"
    addIfGood(current[0] - 1, current[1])
    addIfGood(current[0] + 1, current[1])
    addIfGood(current[0], current[1] - 1)
    addIfGood(current[0], current[1] + 1)

# print_trail()

print(
    "part2:",
    sum(
        [
            1
            for r in range(len(trail))
            for c in range(len(trail[r]))
            if trail[r][c] == "X"
        ]
    ),
)
