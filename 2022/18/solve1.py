import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

L = 21
lines = [l.removesuffix("\n") for l in f.readlines()]
cubes = []
for line in lines:
    cubes.append(tuple(int(x)+1 for x in line.split(",")))


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


part1_res = 0
for i in cubes:
    sides = 6
    for j in cubes:
        if i != j and dist(i, j) == 1:
            sides -= 1
    part1_res += sides

print("Part 1:", part1_res)


def in_bounds(x, y, z):
    return \
        0 <= x and x <= L and \
        0 <= y and y <= L and \
        0 <= z and z <= L


reached = {(0, 0, 0)}
stack = [(0, 0, 0)]
part2_res = 0
while len(stack) > 0:
    current = stack.pop()

    other = [
        (current[0]+1, current[1], current[2]),
        (current[0]-1, current[1], current[2]),
        (current[0], current[1]+1, current[2]),
        (current[0], current[1]-1, current[2]),
        (current[0], current[1], current[2]+1),
        (current[0], current[1], current[2]-1),
    ]

    part2_res += sum((1 for x in other if x in cubes))

    for n in other:
        if in_bounds(*n) and n not in reached and n not in cubes:
            reached.add(n)
            stack.append(n)


print("Part 2:", part2_res)
