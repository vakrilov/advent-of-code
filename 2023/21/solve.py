import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

board = [l.removesuffix("\n") for l in f.readlines()]

STEPS = 64
LEN = len(board[0])

for r in range(LEN):
    for c in range(LEN):
        if board[r][c] == "S":
            start = (r, c)

def is_valid(row, col):
    return 0 <= row < LEN and 0 <= col < LEN and board[row][col] == "."

def valid_neighbors(row, col):
    return [(r, c) for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)] if is_valid(r, c)]

begin = (start[0], start[1], 0)
queue = [begin]
visited = set(start)
log = set()

while len(queue) > 0:
    r, c, dist = queue.pop(0)
    if dist % 2 == 0 and dist <= STEPS:
      log.add((r, c))

    if dist <= STEPS:
      for r, c in valid_neighbors(r, c):
          if (r, c) not in visited:
              visited.add((r, c))

              queue.append((r, c, dist + 1))

def p():
    for r in range(LEN):
        for c in range(LEN):
            if (r, c) in log:
                print("O", end="")
            else:
                print(board[r][c], end="")
        print()

p()
print("part1:", len(log))


