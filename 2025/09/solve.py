# %%
import os
from itertools import combinations

# f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]
rects = [(int(c[0]), int(c[1])) for c in (l.split(",") for l in lines)]


print(
    "part1:",
    max(
        abs(r1[0] - r2[0] + 1) * abs(r1[1] - r2[1] + 1)
        for (r1, r2) in list(combinations(rects, 2))
    ),
)

# %%
