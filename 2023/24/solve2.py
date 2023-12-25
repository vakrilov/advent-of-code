import os


f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

positions = []
velocities = []
for line in lines:
    p, v = line.split("@")

    pos = [int(x.strip()) for x in p.split(",")]
    vel = [int(x.strip()) for x in v.split(",")]

    positions.append(pos)
    velocities.append(vel)

# print(sum((107839125973411.0, 318670276491834.0, 144586871078647.0)))
# 144373393337221
#
# 242720827369528

FROM = -2000
TO = 2000
x = 0

p1x, p1y, p1z = positions[2]
v1x, v1y, v1z = velocities[2]

p2x, p2y, p2z = positions[1]
v2x, v2y, v2z = velocities[1]

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

    # t1 = Ax * t2 + Bx
    # t1 = Ay * t2 + By
    # t1 = Az * t2 + Bz

    Ax = (v2x - vx) / (v1x - vx)
    Bx = (p2x - p1x) / (v1x - vx)

    Ay = (v2y - vy) / (v1y - vy)
    By = (p2y - p1y) / (v1y - vy)

    Az = (v2z - vz) / (v1z - vz)
    Bz = (p2z - p1z) / (v1z - vz)

    # Ax * t2 + Bx = Ay * t2 + By
    if Ay - Ax == 0 or Az - Ax == 0:
        print(f"Skipping: vx: {vx}, vy: {vy}, vz: {vz}")
        return

    t2 = round((Bx - By) / (Ay - Ax), 5)
    t22 = round((Bx - Bz) / (Az - Ax), 5)
    if t2 == t22 and t2.is_integer() and t2 > 0:
        t1 = Ax * t2 + Bx

        x = p1x + t1 * (v1x - vx)
        y = p1y + t1 * (v1y - vy)
        z = p1z + t1 * (v1z - vz)
        if (
            t1.is_integer()
            and t1 > 0
            and x.is_integer()
            and y.is_integer
            and z.is_integer()
            and x >= 0
            and y >= 0
            and z >= 0
        ):
            print(f"vx: {vx}, vy: {vy}, vz: {vz}")
            print(f"t1: {t1}, t2: {t2}")
            print(f"x: {x}, y: {y}, z: {z}")
            print("")
            solutions.append(((x, y, z), (vx, vy, vz)))


# vx 99
# vy 269
# vz 81
check(99, 269, 81)
check(99, 269, -81)
check(99, -269, 81)
check(99, -269, -81)
check(-99, 269, 81)
check(-99, 269, -81)
check(-99, -269, 81)
check(-99, -269, -81)
# solutions = []
# for vx in range(99,100):
#     print(f"vx: {vx}")
#     for vy in range(FROM, TO):
#         for vz in range(FROM, TO):
#             # vx, vy, vz = -3, 1, 2
#             # x = p1x + t1(v1x - vx)
#             # x = p2x + t2(v2x - vx)
#             # p1x + t1(v1x - vx) = p2x + t2(v2x - vx)

#             # t1 = (p2x - p1x + t2(v2x - vx)) / (v1x - vx)
#             # t1 = (p2x - p1x) / (v1x - vx) + t2 * (v2x - vx) / (v1x - vx)


# print(solutions)


# x, y, z = (107839125973411.0, 318670276491834.0, 144586871078647.0)
# vx, vy, vz = (280, 54, 284)

# for i in range(len(positions)):
#     p1x, p1y, p1z = positions[i]
#     v1x, v1y, v1z = velocities[i]

#     t1 = (x - p1x) / (v1x - vx)
#     t2 = (y - p1y) / (v1y - vy)
#     t3 = (z - p1z) / (v1z - vz)
#     print(t1, t2, t3)

