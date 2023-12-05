import os

f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

seeds = [int(s) for s in lines[0][len("seeds: ") :].split()]

def parse_entry(line: str):
    [destination, source, length] = [int(v) for v in line.split()]
    return (source, length, destination - source)

maps = []
current_map = []
for line in lines[2:]:
    if len(line) == 0:
        continue

    if line[0].islower():
        current_map = []
        maps.append(current_map)
    elif line[0].isdigit():
        current_map.append(parse_entry(line))


def use_map(value, map):
    for [source, length, diff] in map:
        if source <= value and value < source + length:
            return value + diff
    return value

for map in maps:
    map.sort(key=lambda x: x[0])



seed_results = []
for seed in seeds:
    value = seed
    for map in maps:
        value = use_map(value, map)

    seed_results.append(value)

print("part1:", min(seed_results))
