import os
from itertools import product
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

MAX = 21
cubes = []
for line in f.readlines():
    cubes.append(tuple(int(x)+1 for x in line.split(",")))


def dist(a, b):
    return sum(abs(d1 - d2) for d1, d2 in zip(a, b))


print("Part 1:", len(cubes)*6 - sum(1 for i,
      j in product(cubes, cubes) if i != j and dist(i, j) == 1))


def in_bounds(x, y, z):
    return \
        0 <= x and x <= MAX and \
        0 <= y and y <= MAX and \
        0 <= z and z <= MAX


def get_neighbors(x, y, z):
    return (
        (x+1, y, z),
        (x-1, y, z),
        (x, y+1, z),
        (x, y-1, z),
        (x, y, z+1),
        (x, y, z-1)
    )


reached = {(0, 0, 0)}
stack = [(0, 0, 0)]
part2_res = 0
while len(stack) > 0:
    neighbors = get_neighbors(*stack.pop())

    part2_res += sum((1 for x in neighbors if x in cubes))

    for n in neighbors:
        if in_bounds(*n) and n not in reached and n not in cubes:
            reached.add(n)
            stack.append(n)


print("Part 2:", part2_res)
