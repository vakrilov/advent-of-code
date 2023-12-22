import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

FACTOR = 31
board = [l.removesuffix("\n") for l in f.readlines()]

for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c] == "S":
            board[r] = board[r].replace("S", ".")
            start = (r, c)
print(start)

ORG_LEN = len(board)
board = [line * FACTOR for line in board] * FACTOR
distances = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
LEN = len(board[0])
org_start = start
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
        if r % ORG_LEN == 0:
            print(("+" + "-" * ORG_LEN) * FACTOR)
        for c in range(LEN):
            if c % ORG_LEN == 0:
                print("|", end="")
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
        if (r, c) not in log:
            log.add((r, c))
            distances[r][c] = dist

        if dist <= steps:
            for r, c in valid_neighbors(r, c):
                if (r, c) not in visited:
                    visited.add((r, c))
                    queue.append((r, c, dist + 1))
    return log

def get_visited_after(steps):
    log = simulate(steps)
    val = sum(1 for r, c in log if (r + c) % 2 == steps % 2)
    return val

STEPS = 26501365
PATTERN_AFTER = 2

def check2(steps):
    rem = steps % ORG_LEN
    jumps = steps // ORG_LEN

    p_range = range(rem, rem + (PATTERN_AFTER + 1) * ORG_LEN + 1, ORG_LEN)
    vals = [get_visited_after(s) for s in p_range]
    diff1 = [vals[i] - vals[i - 1] for i in range(PATTERN_AFTER, PATTERN_AFTER + 2)]
    diff2 = [diff1[i] - diff1[i - 1] for i in range(1, len(diff1))]

    b = vals[PATTERN_AFTER - 1]
    d1 = diff1[0]
    d2 = diff2[0]


    jump_to = jumps - PATTERN_AFTER + 1
    res = b + jump_to * d1 + jump_to * (jump_to - 1) // 2 * d2
    return res

print("Actual:", check2(STEPS))
