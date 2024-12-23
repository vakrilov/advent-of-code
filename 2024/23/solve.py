# %%
import os
from itertools import combinations

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]


node_map = {}
nodes = set()
for l in lines:
    n1, n2 = l.split("-")
    nodes.add(n1)
    nodes.add(n2)

    node_map[n1] = node_map.get(n1, []) + [n2]
    node_map[n2] = node_map.get(n2, []) + [n1]

print(len(nodes))
print(min([len(node_map[n]) for n in node_map]))
print(max([len(node_map[n]) for n in node_map]))


def is_link(n1, n2):
    return n2 in node_map[n1]


# %%

ans = set()
for n1 in node_map:
    if not n1.startswith("t"):
        continue

    for n2, n3 in combinations(node_map[n1], 2):
        if is_link(n2, n3):
            clique = [n1, n2, n3]
            clique.sort()
            ans.add(tuple(clique))

print("part1:", len(ans))


# %%

CLIQUE_SIZE = 13
solutions = []
for n1 in node_map:
    neighs = node_map[n1]

    for reduced in combinations(neighs, CLIQUE_SIZE - 1):
        is_full = all([is_link(n2, n3) for n2, n3 in combinations(reduced, 2)])
        if is_full:
            solution = [n1] + list(reduced)
            solution.sort()
            solutions.append(",".join(solution))

print("part2:", solutions[0])

# %%
