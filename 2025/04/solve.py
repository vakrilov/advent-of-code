# %%
import os

# f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [[l[i] for i in range(len(l.removesuffix("\n")))] for l in f.readlines()]

print(lines)
# %%
R = len(lines)
C = len(lines[0])


def is_roll(r, c):
    if r < 0 or r >= R or c < 0 or c >= C:
        return False
    return lines[r][c] == "@"


def is_accessible_roll(r, c):
    if not is_roll(r, c):
        return False
    rolls = sum(is_roll(nr, nc) for nr in (r - 1, r, r + 1) for nc in (c - 1, c, c + 1))
    return rolls <= 4


part1 = 0
for r in range(R):
    for c in range(C):
        if is_accessible_roll(r, c):
            part1 += 1
print("part1:", part1)

# %%

part2 = 0


def iterate():
    to_remove = []
    for r in range(R):
        for c in range(C):
            if is_accessible_roll(r, c):
                to_remove.append((r, c))
    for r, c in to_remove:
        lines[r][c] = "."
    return len(to_remove)


while (res := iterate()) > 0:
    part2 += res

print("part2:", part2)

# %%
