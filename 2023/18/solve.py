import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")
LEN = 402
start = (200, 200)

# LEN = 100
# start = (5, 5)


current = start
board = [["."] * LEN for _ in range(LEN)]


def p():
    for i in range(LEN):
        for j in range(LEN):
            print(board[i][j], end="")
        print()
    print()


lines = [l.removesuffix("\n") for l in f.readlines()]


def next_step(current, dir):
    if dir == "U":
        return (current[0] - 1, current[1])
    if dir == "D":
        return (current[0] + 1, current[1])
    if dir == "L":
        return (current[0], current[1] - 1)
    if dir == "R":
        return (current[0], current[1] + 1)


board[current[0]][current[1]] = "X"
path = [current]
for line in lines:
    spl = line.split(" ")
    dir = spl[0]
    steps = int(spl[1])

    for i in range(steps):
        current = next_step(current, dir)
        path.append(current)
        board[current[0]][current[1]] = "#"

p()

stack = [(start[0] + 1, start[1] + 1)]
visited = set()

while len(stack) > 0:
    current = stack.pop()
    r, c = current
    if current in visited:
        continue
    visited.add(current)
    board[r][c] = "#"

    if board[r - 1][c] == ".":
        stack.append((r - 1, c))

    if board[r + 1][c] == ".":
        stack.append((r + 1, c))

    if board[r][c - 1] == ".":
        stack.append((r, c - 1))

    if board[r][c + 1] == ".":
        stack.append((r, c + 1))

p()
print("part1:", sum([sum([1 if c == "#" else 0 for c in r]) for r in board]))
