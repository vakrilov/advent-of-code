import os
import itertools

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]


def parse_coords(s):
    return list(map(int, s.split(",")))


parts = []
for i, l in enumerate(lines):
    start, end = l.split("~")
    part = (parse_coords(start), parse_coords(end), i + 1)
    parts.append(part)


def compare(part):
    return part[0][2] * 1000 + part[0][1] * 10 + part[0][0]


parts.sort(key=compare)


x, y, z = 10, 10, 1000
board = array_3d = [[[0 for _ in range(z)] for _ in range(y)] for _ in range(x)]


def drop(part):
    x1, y1, z1 = part[0]
    x2, y2, z2 = part[1]
    part_id = part[2]
    z_diff = z2 - z1

    hit_area = list(itertools.product(range(x1, x2 + 1), range(y1, y2 + 1)))

    current_z = z1
    while current_z > 0:
        if any([board[x][y][current_z - 1] != 0 for x, y in hit_area]):
            break
        current_z -= 1

    dropped_part = ((x1, y1, current_z), (x2, y2, current_z + z_diff), part_id)
    print(f"part: {part} -> {dropped_part}")

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(current_z, current_z + z_diff + 1):
                board[x][y][z] = part_id

    return dropped_part


dropped_parts = []
for part in parts:
    dropped_parts.append(drop(part))


def depends_on(part):
    x1, y1, z1 = part[0]
    x2, y2, z2 = part[1]

    if z1 == 0:
        return []

    hit_area = list(itertools.product(range(x1, x2 + 1), range(y1, y2 + 1)))

    deps = set()
    for x, y in hit_area:
        if board[x][y][z1 - 1] != 0:
            deps.add(board[x][y][z1 - 1])
    
    return list(deps)

can_remove = set()
for part in dropped_parts:
    deps = depends_on(part)
    if len(deps) == 1:
        can_remove.add(deps[0])

print(len(dropped_parts) - len(can_remove))
