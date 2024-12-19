# %%
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]


# %%
def is_safe(nums, can_skip=False):
    direction = nums[0] > nums[1]
    prev = nums[0]
    for i in range(1, len(nums)):
        next = nums[i]
        diff = abs(prev - next)
        safe = diff >= 1 and diff <= 3 and (prev > next) == direction

        if safe:
            prev = next
            continue

        if can_skip:
            can_skip = False
        else:
            return False

    return True


count = 0
for line in lines:
    nums = [int(n) for n in line.split(" ")]
    count += is_safe(nums)
print("part1:", count)
# %%
count = 0

for line in lines:
    nums = [int(n) for n in line.split(" ")]
    safe = is_safe(nums, can_skip=True) or is_safe(nums[1:], can_skip=False)
    count += safe
print("part2:", count)

# %%
