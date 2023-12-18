import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

instructions = []

dir_map = ["R", "D", "L", "U"]
for line in lines:
    spl = line.split(" ")

    steps = int(spl[2][2:7], 16)
    dir = dir_map[int(spl[2][7])]

    instructions.append((dir, steps))


def next_step(current, dir, steps):
    if dir == "R":
        return (current[0] + steps, current[1])
    if dir == "D":
        return (current[0], current[1] + steps)
    if dir == "L":
        return (current[0] - steps, current[1])
    if dir == "U":
        return (current[0], current[1] - steps)


start = (0, 0)
current = start
points = [start]
for ins in instructions:
    current = next_step(current, *ins)
    points.append(current)

area = 0
for p1, p2 in zip(points, points[1:]):
    area += (p2[0] + p1[0]) * (p2[1] - p1[1]) / 2

edge = sum([i[1] for i in instructions]) / 2 + 1
print("part2:", round(area + edge))
