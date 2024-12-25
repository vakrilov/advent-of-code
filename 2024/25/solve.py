# %%
import os
from itertools import product

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

L = 8
keys = []
locks = []


def parse(lines):
    res = [0, 0, 0, 0, 0]
    for i in range(5):
        res[i] = sum([1 if l[i] == "#" else 0 for l in lines])
    return res


for i in range(0, len(lines), L):
    vals = parse(lines[i : i + 7])
    if lines[i] == "#####":
        locks.append(vals)
    else:
        keys.append(vals)


def is_fit(key, lock):
    return all([key[i] + lock[i] <= 7 for i in range(5)])


print("part1:", sum(is_fit(key, lock) for key, lock in product(keys, locks)))
# %%
