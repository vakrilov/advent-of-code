import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]
LEN = len(lines)


def advance(row, col, dir):
    tile = lines[row][col]

    down = (row + 1, col, "d")
    up = (row - 1, col, "u")
    left = (row, col - 1, "l")
    right = (row, col + 1, "r")

    if dir == "u":
        if tile == "." or tile == "|":
            return [up]
        if tile == "-":
            return [left, right]
        if tile == "/":
            return [right]
        if tile == "\\":
            return [left]

    if dir == "d":
        if tile == "." or tile == "|":
            return [down]
        if tile == "-":
            return [left, right]
        if tile == "/":
            return [left]
        if tile == "\\":
            return [right]

    if dir == "l":
        if tile == "." or tile == "-":
            return [left]
        if tile == "|":
            return [up, down]
        if tile == "/":
            return [down]
        if tile == "\\":
            return [up]

    if dir == "r":
        if tile == "." or tile == "-":
            return [right]
        if tile == "|":
            return [up, down]
        if tile == "/":
            return [up]
        if tile == "\\":
            return [down]


def isValid(row, col):
    return row >= 0 and row < len(lines) and col >= 0 and col < len(lines[row])


def eval_initial(queue):
    visited = set()
    while len(queue) > 0:
        action = queue.pop(0)

        if action in visited:
            continue

        visited.add(action)

        for next in advance(*action):
            if isValid(next[0], next[1]):
                queue.append(next)

    visited_coord = set([(r, c) for r, c, _ in visited])
    return len(visited_coord)


print("Part 1:", eval_initial([(0, 0, "r")]))

possible_starts = []
for x in range(LEN - 1):
    possible_starts.append((x, 0, "r"))
    possible_starts.append((x, LEN - 1, "l"))
    possible_starts.append((0, x, "d"))
    possible_starts.append((LEN - 1, x, "u"))

print("Part 2:", max([eval_initial([start]) for start in possible_starts]))
