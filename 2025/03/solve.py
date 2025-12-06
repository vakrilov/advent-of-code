# %%
import os

# f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")
lines = [[int(c) for c in l.removesuffix("\n")] for l in f.readlines()]


def max_jolt(nums: list[int]) -> int:

    max_first_index = 0
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[max_first_index]:
            max_first_index = i

    max_second_index = max_first_index + 1
    for i in range(max_first_index + 2, len(nums)):
        if nums[i] > nums[max_second_index]:
            max_second_index = i

    first = nums[max_first_index]
    second = nums[max_second_index]
    return first * 10 + second


part1 = sum(max_jolt(line) for line in lines)
print("part1:", part1)


# %%
def max_idx(nums: list[int], skip_end: int) -> int:
    max_index = 0
    for i in range(1, len(nums) - skip_end):
        if nums[i] > nums[max_index]:
            max_index = i
    return max_index


def max_jolt_2(nums: list[int], length: int) -> int:
    result = 0
    for skip_end in range(length - 1, -1, -1):
        max_index = max_idx(nums, skip_end)
        result = result * 10 + nums[max_index]
        nums = nums[max_index + 1 :]
    return result


print(max_jolt_2([9, 8, 1, 7, 6, 5, 4, 3, 2, 1, 1, 9, 9], 2))

# %%

part1 = sum(max_jolt_2(line, 2) for line in lines)
print("part1:", part1)

part2 = sum(max_jolt_2(line, 12) for line in lines)
print("part2:", part2)
# %%
