# %%
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

# %%
list1 = []
list2 = []
for line in lines:
    nums = line.split("  ")
    list1.append(int(nums[0]))
    list2.append(int(nums[1]))

# %%
list1.sort()
list2.sort()

# %%
dist = [abs(a - b) for a, b in zip(list1, list2)]
part1 = sum(dist)
print("part1: ", part1)

# %%
map = {}
for num in list2:
    map[num] = map.get(num, 0) + 1

# %%
scores = [num * map.get(num, 0) for num in list1]
part2 = sum(scores)
print("part2: ", part2)
