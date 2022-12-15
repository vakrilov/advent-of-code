import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

LINE = 2000000
PART2_RANGE = 4000000


def dist(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)


def does_overlap(x1, y1, x2, y2):
    # not (one range start after the other ends)
    return not (y1+1 < x2 or y2+1 < x1)


def merge(x1, y1, x2, y2):
    return (min(x1, x2), max(y1, y2))


def find_overlap(ranges):
    for i in range(len(ranges)-1):
        for j in range(i+1, len(ranges)):
            if does_overlap(*ranges[i], *ranges[j]):
                return (i, j)


lines = [l.removesuffix("\n") for l in f.readlines()]
sensors = []
for line in lines:
    line = line.removeprefix("Sensor at x=").replace(
        ", y=", ",").replace(": closest beacon is at x=", ",")
    x, y, bx, by = (int(x) for x in line.split(","))
    sensors.append((x, y, dist(x, y, bx, by)))


def ranges_for_row(row):
    ranges = []
    for x, y, r in sensors:
        intersect = r - abs(y - row)
        if intersect >= 0:
            ranges.append((x-intersect, x+intersect))

    while True:
        r = find_overlap(ranges)
        if r is None:
            break

        range1 = ranges.pop(r[1])
        range2 = ranges.pop(r[0])
        ranges.append(merge(*range1, *range2))
    return ranges


print("Part 1:", sum(r[1]-r[0]+1 for r in ranges_for_row(LINE)) - 1)

for y in range(PART2_RANGE):
    r = ranges_for_row(y)
    if len(r) == 2:
        x = min(r[0][1], r[1][1]) + 1
        print("Part 2:", x * 4000000 + y)
        break
