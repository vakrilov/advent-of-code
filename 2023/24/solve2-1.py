import os
from itertools import chain
from math import sqrt

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]


def divisors(n):
    return set(
        chain.from_iterable(
            (i, n // i) for i in range(1, int(sqrt(n)) + 1) if n % i == 0
        )
    )

positions = []
velocities = []
for line in lines:
    p, v = line.split("@")

    pos = [int(x.strip()) for x in p.split(",")]
    vel = [int(x.strip()) for x in v.split(",")]

    positions.append(pos)
    velocities.append(vel)

FROM = -1000
TO = 1000
x = 0


vxes = dict()
for i in range(len(positions)):
    vx = velocities[i][0]
    if vx not in vxes.keys():
        vxes[vx] = []
    vxes[vx].append(i)

x = [vals for vals in vxes.values() if len(vals) > 2]


candidates = []
for li in x:
    xpos = [positions[i][0] for i in li]
    vx = velocities[li[0]][0]
    # print(vx)

    xpos.sort()
    # print(xpos)

    diffs = [xpos[i + 1] - xpos[i] for i in range(len(xpos) - 1)]
    # print(diffs)
    divisor_sets = [set(divisors(d)) for d in diffs]

    intersection = divisor_sets[0].intersection(*divisor_sets[1:])
    # print(intersection)


    possibleVXs = [vx + i for i in intersection] + [i - vx for i in intersection]
    possibleVXs.sort()
    print(possibleVXs)
    candidates.append(set(possibleVXs))

candidates_intersection = candidates[0].intersection(*candidates[1:])
print(candidates_intersection)

# x, y, z = (107839125973411.0, 318670276491834.0, 144586871078647.0)
# vx, vy, vz = (280, 54, 284)

# for i in range(len(positions)):
#     p1x, p1y, p1z = positions[i]
#     v1x, v1y, v1z = velocities[i]

#     t1 = (x - p1x) / (v1x - vx)
#     t2 = (y - p1y) / (v1y - vy)
#     t3 = (z - p1z) / (v1z - vz)
#     print(t1, t2, t3)

#vx 99
#vy 269
#vz 81
