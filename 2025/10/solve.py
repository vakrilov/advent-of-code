# %%
import os
from itertools import combinations


f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")
# f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

machines = []
for l in lines:
    parts = l.split(" ")

    target_bin = parts[0][1:-1].replace(".", "0").replace("#", "1")
    target = int(target_bin, 2)
    lights_count = len(target_bin)

    btn_parts = parts[1:-1]
    btn_vals = []
    for btn in btn_parts:
        nums = [int(x) for x in btn[1:-1].split(",")]
        btn_value = sum([2 ** (lights_count - x - 1) for x in nums])
        btn_vals.append(btn_value)

    jolt_requirement = [int(x) for x in parts[-1][1:-1].split(",")]
    print("jolt requirement:", jolt_requirement)

    machines.append((target, btn_vals, jolt_requirement))
    # print([f"{val:b}" for val in btn_vals])

print(machines)


# %%
def calc_state(btn_vals):
    state = 0
    for val in btn_vals:
        state ^= val
    return state


def activate_machine(target, btn_vals) -> int:
    n = len(btn_vals)
    for n in range(1, n + 1):
        for combo in combinations(btn_vals, n):
            if calc_state(combo) == target:
                return n

    raise Exception("No solution found")


print("part 1:", sum(activate_machine(m[0], m[1]) for m in machines))

# %%
