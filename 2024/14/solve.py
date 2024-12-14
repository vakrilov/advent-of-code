# %%
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")
# W, H = 11, 7
W, H = 101, 103
lines = [l.removesuffix("\n") for l in f.readlines()]

robots = []
for line in lines:
    parts = line.split(" ")
    ps = parts[0][2:].split(",")
    pos = (int(ps[0]), int(ps[1]))

    vs = parts[1][2:].split(",")
    vel = (int(vs[0]), int(vs[1]))

    robots.append((pos, vel))


def p(pos):
    for y in range(H):
        for x in range(W):
            count = sum([1 for p in pos if p == (x, y)])
            print(count if count > 0 else ".", end="")
        print()


def simulate(turns):
    new_pos = []
    for r in robots:
        pos, vel = r
        x = (pos[0] + vel[0] * turns) % W
        y = (pos[1] + vel[1] * turns) % H
        new_pos.append((x, y))

    q = [0, 0, 0, 0]
    for pos in new_pos:
        x, y = pos
        if x < W // 2 and y < H // 2:
            q[0] += 1
        elif x < W // 2 and y > H // 2:
            q[1] += 1
        elif x > W // 2 and y < H // 2:
            q[2] += 1
        elif x > W // 2 and y > H // 2:
            q[3] += 1

    if q[0] == q[1] and q[2] == q[3]:
        print("turns:", turns)
        p(new_pos)

    return q[0] * q[1] * q[2] * q[3]


print("part 1:", simulate(100))

# for i in range(1, 100000):
#     simulate(i)

# %%
