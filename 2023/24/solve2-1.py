# %%
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

parts = []
for line in lines:
    p, v = line.split("@")

    pos = [int(x.strip()) for x in p.split(",")]
    vel = [int(x.strip()) for x in v.split(",")]

    parts.append((*pos, *vel))

def check(coord_idx):
    velocity_groups = dict()

    for i in range(len(parts)):
        v = parts[i][coord_idx + 3]
        if v not in velocity_groups.keys():
            velocity_groups[v] = []
        velocity_groups[v].append(i)

    vel_candidates = []
    for part_vel, idx_list in velocity_groups.items():
        if len(idx_list) < 3:
            continue

        positions = [parts[idx][coord_idx] for idx in idx_list]
        positions.sort()
        # print("part_vel", part_vel)
        # print("positions", positions)

        diffs = [positions[i + 1] - positions[i] for i in range(len(positions) - 1)]
        divisor_sets = [set(divisors(d)) for d in diffs]
        vel_diffs = divisor_sets[0].intersection(*divisor_sets[1:])

        # print("vel_diffs", vel_diffs)


        possible_rock_vels = [part_vel - vel_diff for vel_diff in vel_diffs] + [
            part_vel + vel_diff for vel_diff in vel_diffs
        ]
        possible_rock_vels.sort()
        # print("possibleRockVels", possible_rock_vels)
        vel_candidates.append(set(possible_rock_vels))

        # print("--------")
        # print("--------")

    # print(vel_candidates)
    candidates_intersection = vel_candidates[0].intersection(*vel_candidates[1:])
    print(candidates_intersection)
    return candidates_intersection

vx_options = check(0)
vy_options = check(1)
vz_options = check(2)


p1x, p1y, p1z, v1x, v1y, v1z = parts[3]
p2x, p2y, p2z, v2x, v2y, v2z  = parts[1]

# %%
solutions = []
def check(vx, vy, vz):
    if (
        v1x - vx == 0
        or v2x - vx == 0
        or v1y - vy == 0
        or v2y - vy == 0
        or v1z - vz == 0
        or v2z - vz == 0
    ):
        print("SKIP")
        return
    
    v1x_r = v1x - vx
    v2x_r = v2x - vx
    v1y_r = v1y - vy
    v2y_r = v2y - vy

    Ax = v2x_r / v1x_r
    Bx = (p2x - p1x) / v1x_r

    Ay = v2y_r / v1y_r
    By = (p2y - p1y) / v1y_r

    Az = (v2z - vz) / (v1z - vz)
    Bz = (p2z - p1z) / (v1z - vz)

    # Ax * t2 + Bx = Ay * t2 + By

    if Ay - Ax == 0 or Az - Ax == 0:
        print(f"Skipping: vx: {vx}, vy: {vy}, vz: {vz}")
        return

    t2 = round((Bx - By) / (Ay - Ax), 2)
    t22 = round((Bx - Bz) / (Az - Ax), 2)

    if t2 == t22 and t2.is_integer() and t2 > 0:
        t1 = Ax * t2 + Bx

        x = p1x + t1 * (v1x - vx)
        y = p1y + t1 * (v1y - vy)
        z = p1z + t1 * (v1z - vz)
        if (
            t1.is_integer()
            and t1 > 0
            and x.is_integer()
            and y.is_integer()
            and z.is_integer()
            and x >= 0
            and y >= 0
            and z >= 0
        ):
            print(f"vx: {vx}, vy: {vy}, vz: {vz}")
            print(f"t1: {t1}, t2: {t2}")
            print(f"x: {x}, y: {y}, z: {z}")
            print("SOLUTION:", round(x+y+z))
            solutions.append(((x, y, z), (vx, vy, vz)))

for vx in vx_options:
    for vy in vy_options:
        for vz in vz_options:
            check(vx, vy, vz)

# %%
