# %%
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")
# f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")
lines = [l.removesuffix("\n") for l in f.readlines()]

# %%
current = 50
zeros = 0
for ln in lines:
    diff = (-1 if ln[0] == "L" else 1) * int(ln[1:])
    current += diff
    current %= 100
    if current == 0:
        zeros += 1
print("part1:", zeros)


# %%
current = 50
passedThroughZeros = 0
for ln in lines:
    diff = (-1 if ln[0] == "L" else 1) * int(ln[1:])
    if current + diff >= 100:
        passes = (current + diff) // 100
        passedThroughZeros += passes

    if current + diff <= 0:
        passes = (-(current + diff)) // 100 + (1 if current > 0 else 0)
        passedThroughZeros += passes

    current += diff
    current %= 100


print("part2:", passedThroughZeros)

# %%
