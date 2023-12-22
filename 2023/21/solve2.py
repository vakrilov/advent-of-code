import os

f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")

FACTOR = 5
STEPS = 10
board = [l.removesuffix("\n") for l in f.readlines()]

EVEN_STEP = STEPS % 2

for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c] == "S":
            board[r] = board[r].replace("S", ".")
            start = (r, c)
print(start)

ORG_LEN = len(board)
board = [line * FACTOR for line in board] * FACTOR
LEN = len(board[0])
start = (start[0] + ORG_LEN * (FACTOR // 2), start[1] + ORG_LEN * (FACTOR // 2))


def is_valid(row, col):
    return 0 <= row < LEN and 0 <= col < LEN and board[row][col] == "."


def valid_neighbors(row, col):
    return [
        (r, c)
        for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        if is_valid(r, c)
    ]


def p(log):
    for r in range(LEN):
        for c in range(LEN):
            if (r, c) in log:
                print("o", end="")
            else:
                print(board[r][c], end="")
        print()

begin = (start[0], start[1], 0)

def simulate(steps):
    queue = [begin]
    visited = set(start)
    log = set()

    while len(queue) > 0:
        r, c, dist = queue.pop(0)
        # if dist % 2 == 0 and dist <= STEPS:
        log.add((r, c))

        if dist <= steps:
            for r, c in valid_neighbors(r, c):
                if (r, c) not in visited:
                    visited.add((r, c))
                    queue.append((r, c, dist + 1))
    p(log)

for i in range(1, 10):
    print(i)
    simulate(i)
    print("")
    print("")
    print("")




# print(log)
# print(sum(1 for l in log if (l[0] + l[1]) % 2 == EVEN_STEP))
