# %%
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

result = 0
for line in lines[30:]:
    size_part, counts_part = line.split(": ")

    size = tuple(int(x) for x in size_part.split("x"))
    total_slots = (size[0] // 3) * (size[1] // 3)

    total_parts = sum(int(x) for x in counts_part.split(" "))

    result += 1 if total_slots >= total_parts else 0

print(f"Part1: {result}")

# %%
