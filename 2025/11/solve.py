# %%
import os
from functools import cache


# f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")
# f = open(os.path.dirname(__file__) + "/sample2.txt", "r", encoding="utf-8")
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

nodes = dict()

for line in lines:
    parts = line.split(": ")
    name = parts[0]
    nodes[name] = parts[1].split(" ")

nodes["out"] = []

# %%


@cache
def paths(start, to):
    if start == to:
        return 1
    return sum(paths(n, to) for n in nodes[start])


print("part1: ", paths("you", "out"))

dac_fft = paths("svr", "dac") * paths("dac", "fft") * paths("fft", "out")
fft_dac = paths("svr", "fft") * paths("fft", "dac") * paths("dac", "out")
print("part2: ", dac_fft + fft_dac)


# %%


# %%
