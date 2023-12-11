import os
from itertools import combinations

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

rows = [l.removesuffix("\n") for l in f.readlines()]

exRows = []
exCols = []
for i in range(len(rows)):
    if all(c == "." for c in rows[i]):
        exRows.append(i)

for i in range(len(rows[0])):
    if all(rows[j][i] == "." for j in range(len(rows))):
        exCols.append(i)

galaxies = []
for r in range(len(rows)):
    for c in range(len(rows[r])):
        if rows[r][c] == "#":
            galaxies.append((r, c))

expand_factor = 1000_000
res_part1 = 0
res_part2 = 0
for g1, g2 in combinations(galaxies, 2):
    row_from, row_to = sorted([g1[0], g2[0]])
    col_from, col_to = sorted([g1[1], g2[1]])

    expandX = sum([1 for i in range(row_from, row_to) if i in exRows])
    expandY = sum([1 for i in range(col_from, col_to) if i in exCols])

    res_part1 += row_to - row_from + col_to - col_from + expandX + expandY
    res_part2 += row_to - row_from + col_to - col_from + (expandX + expandY) * (expand_factor - 1)


print("part1:", res_part1)
print("part2:", res_part2)
