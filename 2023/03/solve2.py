import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") + "." for l in f.readlines()]
ROWS = len(lines)
COLS = len(lines[0])

gears = dict()


def process(row, col, len, value):
    for r in range(max(row - 1, 0), min(row + 2, ROWS)):
        for c in range(max(col - 1, 0), min(col + len + 1, COLS)):
            if lines[r][c] == "*":
                if (r, c) not in gears:
                    gears[(r, c)] = []
                gears[(r, c)].append(value)


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
            if start != -1:
                process(row, start, col - start, current)
            current = 0
            start = -1


print("part2", sum(vals[0] * vals[1] for vals in gears.values() if len(vals) == 2))
