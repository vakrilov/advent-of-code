# %%
import os
from functools import cache

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")
lines = [l.removesuffix("\n") for l in f.readlines()]
stones = [int(l) for l in lines[0].split()]


# %%
@cache
def solve(stone, blinks_left):
    if blinks_left == 0:
        return 1

    if stone == 0:
        return solve(1, blinks_left - 1)

    stoneStr = str(stone)
    if len(stoneStr) % 2 == 0:
        l = len(stoneStr) // 2
        left = int(stoneStr[0:l])
        right = int(stoneStr[l:])
        return solve(left, blinks_left - 1) + solve(right, blinks_left - 1)

    return solve(int(stone) * 2024, blinks_left - 1)


print("part1:", sum(solve(s, 25) for s in stones))
print("part2:", sum(solve(s, 75) for s in stones))
# %%
