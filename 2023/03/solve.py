import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") + "." for l in f.readlines()]
ROWS = len(lines)
COLS = len(lines[0])


def check(row, col, len):
    for r in range(max(row - 1, 0), min(row + 2, ROWS)):
        for c in range(max(col - 1, 0), min(col + len + 1, COLS)):
            if not lines[r][c].isdigit() and lines[r][c] != ".":
                return True
    return False


res = 0
for row, line in enumerate(lines):
    current = 0
    start = -1
    for col in range(len(line)):
        ch = line[col]
        if ch.isdigit():
            current = current * 10 + int(ch)
            if start == -1:
                start = col
        else:
            if start != -1 and check(row, start, col - start):
                res += current
            current = 0
            start = -1


print("part1", res)
