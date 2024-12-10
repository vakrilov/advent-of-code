# %%
import os
from itertools import product

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")
lines = [l.removesuffix("\n") for l in f.readlines()]
L = len(lines)

board = [[int(c) for c in l] for l in lines]
print(L)
print(board)
# %%


def search(r, c, prev, heads):
    if (not 0 <= r < L) or (not 0 <= c < L):
        return 0

    val = board[r][c]
    if val != (prev + 1):
        return 0

    if val == 9:
        heads.add((r, c))
        return 1

    neighbours = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    return sum(search(nr, nc, val, heads) for nr, nc in neighbours)


# %%


part1 = 0
part2 = 0
for r, c in product(range(L), range(L)):
    if board[r][c] == 0:
        heads = set()
        part2 += search(r, c, -1, heads)
        part1 += len(heads)

print("part1:", part1)
print("part2:", part2)
# %%
