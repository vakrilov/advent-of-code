# %%
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

# %%

count = 0

for line in lines:
    nums = [int(n) for n in line.split(" ")]

    direction = nums[0] > nums[1]

    safe = 1
    for i in range(0, len(nums) - 1):
        num1 = nums[i]
        num2 = nums[i + 1]
        diff = abs(num1 - num2)
        if diff < 1 or diff > 3 or (num1 > num2) != direction:
            safe = 0
            break
    count += safe


print(count)
# %%


def is_valid(nums):
    direction = nums[0] > nums[1]
    for i in range(0, len(nums) - 1):
        num1 = nums[i]
        num2 = nums[i + 1]
        diff = abs(num1 - num2)
        if diff < 1 or diff > 3 or (num1 > num2) != direction:
            return False
    return True


count = 0

for line in lines:
    nums = [int(n) for n in line.split(" ")]

    print("original", nums)
    safe = is_valid(nums)

    if not safe:
        for i in range(0, len(nums)):
            nums_fixed = nums[:i] + nums[i + 1 :]
            print("fixed", nums_fixed)
            safe = is_valid(nums_fixed)
            if safe:
                print("FOUND!", nums_fixed)
                safe = 1
                break

    count += safe


print(count)

# %%
