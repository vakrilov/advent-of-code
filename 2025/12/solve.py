# %%
import os

# f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

parts = []
part_areas = []
part_variants = []
scenarios = []


def parse_part(lines):
    return tuple(tuple(0 if ch == "." else 1 for ch in line) for line in lines)


def rotate_part(part):
    return tuple(
        tuple(part[len(part) - 1 - c][r] for c in range(len(part)))
        for r in range(len(part[0]))
    )


def flip_part(part):
    return tuple(tuple(reversed(row)) for row in part)


def print_part(part):
    for line in part:
        print("".join("#" if x == 1 else "." for x in line))
    print()


line_idx = 0
while line_idx < len(lines):
    line = lines[line_idx]
    if line and line[0].isdigit() and line[1] == ":":
        part = parse_part(lines[line_idx + 1 : line_idx + 4])
        parts.append(part)
        line_idx += 5
    elif not line == "":
        size_part, counts_part = line.split(": ")
        size = tuple(int(x) for x in size_part.split("x"))
        counts = [int(x) for x in counts_part.split(" ")]
        scenarios.append((size, counts))
        line_idx += 1


for part in parts:
    part_area = sum(sum(row) for row in part)
    part_areas.append(part_area)

    unique_variations = set([part])
    for _ in range(3):
        part = rotate_part(part)
        unique_variations.add(part)

    part = flip_part(part)
    unique_variations.add(part)
    for _ in range(3):
        part = rotate_part(part)
        unique_variations.add(part)

    part_variants.append(list(unique_variations))

    print(f"Part variants count: {len(unique_variations)}")
    for pv in unique_variations:
        print_part(pv)


print(part_variants)
# %%

possible = 0
for scenario_idx, (size, counts) in enumerate(scenarios):
    area = size[0] * size[1]
    parts_area = sum(part_areas[i] * counts[i] for i in range(len(counts)))
    possible += 1 if area > parts_area else 0

print(f"Part1: {possible}")

# %%
