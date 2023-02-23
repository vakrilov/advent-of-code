import os
from functools import cache
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")


@cache
def fuel_requirement(mass: int) -> int:
    if mass < 9:
        return 0
    current_step_value = mass // 3 - 2
    return current_step_value + fuel_requirement(current_step_value)


lines = [int(l.removesuffix("\n")) for l in f.readlines()]

print("Part 1", sum([mass // 3 - 2 for mass in lines]))
print("Part 2",  sum([fuel_requirement(mass) for mass in lines]))
