# %%
import os
import re

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

# %%


def solve_line(line):
    res = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", line)

    result = 0
    for r in res:
        r = r.replace("mul(", "").replace(")", "")
        r = r.split(",")
        num1 = int(r[0])
        num2 = int(r[1])
        result += num1 * num2
    return result


result = sum([solve_line(line) for line in lines])

print("part1", result)

# %%
