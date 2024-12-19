# %%
import os
import re

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")
lines = [l.removesuffix("\n") for l in f.readlines()]
# %%
mul = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
do = r"do\(\)"
dont = r"don\'t\(\)"
regex = "|".join([mul, do, dont])


# %%
def get_mul(group):
    group = group.replace("mul(", "").replace(")", "")
    nums = [int(x) for x in group.split(",")]
    return nums[0] * nums[1]


# %%
result = 0
for line in lines:
    for match in re.findall(mul, line):
        result += get_mul(match)
print("part1", result)


# %%
enabled = True
result = 0
for line in lines:
    for match in re.findall(regex, line):
        if match == "don't()":
            enabled = False
        elif match == "do()":
            enabled = True
        elif enabled:
            result += get_mul(match)

print("part2", result)

# %%
