# %%
from itertools import product
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

L = len(lines)

# %%

visited = set()


def adjacent(r, c):
    return [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]


def perimeter(tiles: set):
    perim = 0
    for r, c in tiles:
        perim += len([a for a in adjacent(r, c) if a not in tiles])

    return perim


def is_edge(adj1, adj2, diag):
    outer_edge = not adj1 and not adj2
    inner_edge = adj1 and adj2 and not diag
    return outer_edge or inner_edge


def edges(tiles: set):
    edges = 0
    for r, c in tiles:
        tr = is_edge((r - 1, c) in tiles, (r, c + 1) in tiles, (r - 1, c + 1) in tiles)
        rl = is_edge((r - 1, c) in tiles, (r, c - 1) in tiles, (r - 1, c - 1) in tiles)
        br = is_edge((r + 1, c) in tiles, (r, c + 1) in tiles, (r + 1, c + 1) in tiles)
        bl = is_edge((r + 1, c) in tiles, (r, c - 1) in tiles, (r + 1, c - 1) in tiles)

        edges += tr + rl + br + bl

    return edges


def solve(r, c):
    tiles = set()
    letter = lines[r][c]

    bfs(r, c, tiles, letter)

    area = len(tiles)
    perim = perimeter(tiles)
    edges_count = edges(tiles)

    return (area * perim, area * edges_count)


def bfs(r, c, tiles: set, letter):
    if not (0 <= r < L and 0 <= c < L):
        return

    if (r, c) in visited:
        return

    if lines[r][c] != letter:
        return

    visited.add((r, c))
    tiles.add((r, c))

    for ar, ac in adjacent(r, c):
        bfs(ar, ac, tiles, letter)


part1 = 0
part2 = 0
for r, c in product(range(L), range(L)):
    p1, p2 = solve(r, c)
    part1 += p1
    part2 += p2

print("part1:", part1)
print("part2:", part2)

# %%
