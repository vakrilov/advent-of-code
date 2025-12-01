# %%
import os

f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

print(len(lines))
print(len(lines[0]))

L = len(lines)
board = [[int(c) for c in l] for l in lines]

# %%
