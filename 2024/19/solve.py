# %%
import os
from functools import cache

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

towels = lines[0].split(", ")
patterns = lines[2:]

# %%


@cache
def check(pattern: str):
    if len(pattern) == 0:
        return 1

    matches = [t for t in towels if pattern.startswith(t)]
    return sum(check(pattern[len(t) :]) for t in matches)


print("part1:", sum(check(p) > 0 for p in patterns))
print("part2:", sum(check(p) for p in patterns))

# %%


class Node:
    def __init__(self, isStart=False):
        self.dict = {"w": [], "u": [], "b": [], "r": [], "g": []}

    def add(self, ch, node):
        self.dict[ch].append(node)

    def get(self, ch):
        return self.dict[ch]

    def __str__(self):
        return self.ch

    def __repr__(self):
        return self.ch


def create_trie(towels):
    start = Node(isStart=True)

    for t in towels:
        current = start

        for i, next_ch in enumerate(t):
            last = i == len(t) - 1
            next_current = start if last else Node()
            current.add(next_ch, next_current)
            current = next_current
    return start


trie = create_trie(towels)


def check_pattern(trie, pattern):
    current_nodes = [trie]
    for ch in pattern:
        next_nodes = set()
        for node in current_nodes:
            for nn in node.get(ch):
                next_nodes.add(nn)

        current_nodes = next_nodes

    return trie in current_nodes


part1 = sum([1 if check_pattern(trie, p) else 0 for p in patterns])
print("part1(with trie):", part1)


# %%
