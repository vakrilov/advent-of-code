import os

MAX = 10**12

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")
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



for map in maps:
    map.sort(key=lambda x: x[0])

    first = map[0]
    if first[0] != 0:
        map.insert(0, (0, first[0], 0))

    last = map[-1]
    map.append((last[0] + last[1], MAX, 0))

    additional = []
    for r1, r2 in zip(map[0:-1], map[1:]):
        if r1[0] + r1[1] < r2[0]:
            additional.append((r1[0] + r1[1], r2[0] - r1[0] - r1[1], 0))
    map.extend(additional)
    map.sort(key=lambda x: x[0])


def process_range(range, map):
    start, length = range
    map_idx = 0
    res = []
    while length > 0:
        m_start, m_length, m_value_diff = map[map_idx]
        m_end = m_start + m_length
        map_idx += 1
        if start > m_start + m_length:
            continue

        if start + length >= m_end:
            res.append((start + m_value_diff, m_end - start))
            length = start + length - m_end
            start = m_end
        else:
            res.append((start + m_value_diff, length))
            length = 0
    return res


final_ranges = []
for start, length in zip(seeds[0::2], seeds[1::2]):
    current_ranges = [(start, length)]
    for map in maps:
        new_ranges = []
        for r in current_ranges:
            new_ranges.extend(process_range(r, map))
        current_ranges = new_ranges
    final_ranges.extend(current_ranges)

print("part2:", min(s for s, _ in final_ranges))
