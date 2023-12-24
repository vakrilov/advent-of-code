import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

# BOUND_LOW = 7
# BOUND_HIGH = 27

BOUND_LOW = 200000000000000
BOUND_HIGH = 400000000000000

positions = []
velocities = []
for line in lines:
    p, v = line.split("@")

    pos = [int(x.strip()) for x in p.split(",")]
    vel = [int(x.strip()) for x in v.split(",")]

    positions.append(pos)
    velocities.append(vel)


def line_from_pos_and_vel(pos, vel):
    if vel[0] == 0:
        return (0, 1, -pos[1])
    m = vel[1] / vel[0]
    return (-m, 1, m * pos[0] - pos[1])


def intersect(line1, line2):
    a1, b1, c1 = line1
    a2, b2, c2 = line2

    det = a1 * b2 - a2 * b1

    if det == 0:
        return None

    x = -(b2 * c1 - b1 * c2) / det
    y = -(a1 * c2 - a2 * c1) / det

    return (x, y)


line_eq = [line_from_pos_and_vel(pos, vel) for pos, vel in zip(positions, velocities)]


def is_in_bounds(pos):
    return (
        pos is not None
        and BOUND_LOW <= pos[0] <= BOUND_HIGH
        and BOUND_LOW <= pos[1] <= BOUND_HIGH
    )


def is_in_future(pos, vel, intersection):
    if vel[0] != 0:
        t = (intersection[0] - pos[0]) / vel[0]
        return t > 0
    else:
        t = (intersection[1] - pos[1]) / vel[1]
        return t > 0


res = 0
for i in range(len(positions) - 1):
    for j in range(i + 1, len(positions)):
        line1 = line_eq[i]
        line2 = line_eq[j]

        pos1 = positions[i]
        pos2 = positions[j]

        intersection = intersect(line1, line2)
        if (
            is_in_bounds(intersection)
            and is_in_future(pos1, velocities[i], intersection)
            and is_in_future(pos2, velocities[j], intersection)
        ):
            res += 1

print("part1:", res)
