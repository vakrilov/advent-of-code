# %%
import os
from itertools import combinations

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

# %%
L = len(lines)


def is_valid(r, c):
    return 0 <= r < L and 0 <= c < L


loc = {}
for r in range(L):
    for c in range(L):
        if lines[r][c] != ".":
            key = lines[r][c]
            loc[lines[r][c]] = loc.get(lines[r][c], []) + [(r, c)]

antinodes = set()
for key in loc:
    for n1, n2 in combinations(loc[key], 2):
        p1 = (2 * n2[0] - n1[0], 2 * n2[1] - n1[1])
        if is_valid(*p1):
            antinodes.add(p1)

        p2 = (2 * n1[0] - n2[0], 2 * n1[1] - n2[1])
        if is_valid(*p2):
            antinodes.add(p2)
print("part1:", len(antinodes))

# %%

antinodes = set()
for key in loc:
    for n1, n2 in combinations(loc[key], 2):
        dr = n2[0] - n1[0]
        dc = n2[1] - n1[1]

        r, c = n1
        while is_valid(r, c):
            antinodes.add((r, c))
            r += dr
            c += dc

        r, c = n1
        while is_valid(r, c):
            antinodes.add((r, c))
            r -= dr
            c -= dc

print("part2", len(antinodes))


# %%
