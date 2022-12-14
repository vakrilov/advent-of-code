import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

ROWS = 1000
COLS = 1000
grid = [[0] * COLS for _ in range(ROWS)]

floor_y = 0
for line in f.readlines():
    ints = [int(x) for x in line.replace("->", ",").split(",")]

    for i in range(0, len(ints)-2, 2):
        x1, y1, x2, y2 = ints[i:i+4]
        y1, y2 = min(y1, y2), max(y1, y2)
        x1, x2 = min(x1, x2), max(x1, x2)

        if x1 == x2:
            for y in range(y1, y2+1):
                grid[y][x1] = 1
        else:
            for x in range(x1, x2+1):
                grid[y1][x] = 1

        floor_y = max(floor_y, y2 + 2)


def drop_one(x: int, y: int):
    if grid[y][x] > 0:
        return None

    while y < ROWS-1:
        if grid[y+1][x] == 0:
            y += 1
        elif grid[y+1][x-1] == 0:
            y += 1
            x -= 1
        elif grid[y+1][x+1] == 0:
            y += 1
            x += 1
        else:
            return (x, y)

    return None


def drop_sand():
    dropped_count = 0
    while True:
        r = drop_one(500, 0)
        if r is None:
            break
        grid[r[1]][r[0]] = 2
        dropped_count += 1
    return dropped_count


res = drop_sand()
print("Part 1:", res)

grid[floor_y] = [1] * COLS
res += drop_sand()
print("Part 2:", res)
