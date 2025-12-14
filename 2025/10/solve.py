# %%
import os
from itertools import combinations


# f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

machines = []
machines_part2 = []
for l in lines:
    parts = l.split(" ")

    target_bin = parts[0][1:-1].replace(".", "0").replace("#", "1")
    target = int(target_bin, 2)
    lights_count = len(target_bin)

    btn_parts = parts[1:-1]
    btn_vals = []
    btn_vals_as_bin = []
    for btn in btn_parts:
        nums = [int(x) for x in btn[1:-1].split(",")]
        btn_value = sum([2 ** (lights_count - x - 1) for x in nums])
        btn_vals.append(btn_value)

        btn_vals_tuple = tuple(1 if i in nums else 0 for i in range(lights_count))

        btn_vals_as_bin.append(btn_vals_tuple)

    btn_vals_as_bin.sort(key=lambda x: sum(x), reverse=True)
    jolt_requirement = tuple(int(x) for x in parts[-1][1:-1].split(","))

    machines.append((target, btn_vals))
    machines_part2.append((jolt_requirement, tuple(btn_vals_as_bin)))

# print(machines)
print(machines_part2)


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
from operator import sub
from functools import cache


def vector_sub(t1, t2):
    return tuple(x - y for x, y in zip(t1, t2))


def vector_add(t1, t2):
    return tuple(x + y for x, y in zip(t1, t2))


def vector_mul(t1, scalar):
    return tuple(x * scalar for x in t1)


def vector_len(v):
    return sum(x * x for x in v) ** 0.5


current_buttons = None
target = None
target_norm = None


@cache
def solve(position) -> int:
    if target == position:
        return 0

    results = []
    for i, btn in enumerate(current_buttons):
        next_position = vector_add(position, btn)

        if valid(next_position):
            res = solve(next_position)
            if res is not None:
                results.append(res)

    return min(results) + 1 if len(results) > 0 else None


def valid(pos: tuple) -> bool:
    for i in range(len(target)):
        if pos[i] < 0 or pos[i] > target[i]:
            return False

    l = vector_len(pos)
    perfect_pos = vector_mul(target_norm, l)
    diff = vector_sub(pos, perfect_pos)
    diff_len = vector_len(diff)

    # tweak this constant. Less means faster but possibly not accurate
    return diff_len < 1.6


def p(m):
    print(m[0])
    print("\n".join("".join(str(x) for x in row) for row in m[1]))


def solve_machine(num: int):
    global target, current_buttons, target_norm
    m = machines_part2[num]
    target = m[0]
    current_buttons = m[1]
    target_len = vector_len(target)
    target_norm = vector_mul(target, 1 / target_len)
    # print("Target norm:", target_norm)

    solve.cache_clear()
    return solve((0,) * len(target))


# print(solve_machine(1))  # warmup

total_part2 = 0
for m in range(len(machines_part2)):
    res = solve_machine(m)
    print(f"Machine {m} solved with {res} presses")
    total_part2 += res

print("part 2:", total_part2)
# %%
