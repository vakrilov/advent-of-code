# %%
import os
from functools import cache
from itertools import product

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]
L = len(lines)

numeric_pad = ("789", "456", "123", " 0A")
directional_pad = (" ^A", "<v>")


def get_pos(symbol, pad):
    for row, l in enumerate(pad):
        if symbol in l:
            return (l.index(symbol), row)


def num_dx(dx):
    return (">" if dx > 0 else "<") * abs(dx)


def num_dy(dy):
    return ("v" if dy > 0 else "^") * abs(dy)


@cache
def navigate(fr, to, pad):
    fr_x, fr_y = get_pos(fr, pad)
    to_x, to_y = get_pos(to, pad)

    dx = to_x - fr_x
    dy = to_y - fr_y

    results = set()
    if pad[fr_y][to_x] != " ":
        results.add(num_dx(dx) + num_dy(dy) + "A")

    if pad[to_y][fr_x] != " ":
        results.add(num_dy(dy) + num_dx(dx) + "A")

    return results


@cache
def navigate_numeric(fr, to):
    return navigate(fr, to, numeric_pad)


@cache
def navigate_directional(fr, to):
    return navigate(fr, to, directional_pad)


# print(navigate_numeric("3", "7"))
# print(navigate_directional("v", "A"))

# %%


def get_pairs(path):
    prefixed_path = "A" + path
    for i in range(len(path)):
        yield prefixed_path[i], prefixed_path[i + 1]


# %%


def numeric_paths(code):
    all_steps = [list(navigate_numeric(fr, to)) for fr, to in get_pairs(code)]
    # print(all_steps)

    products = ["".join(steps) for steps in product(*all_steps)]
    # print(products)
    return products


# numeric_paths(lines[0])
# numeric_paths(lines[1])
# numeric_paths(lines[2])
# numeric_paths(lines[3])
# numeric_paths(lines[4])


# %%
@cache
def navigate_directional_with_lvl(fr, to, lvl):
    paths = navigate_directional(fr, to)
    if lvl == 1:
        return min(len(p) for p in navigate_directional(fr, to))

    path_costs = []
    for path in paths:
        cost = sum(
            navigate_directional_with_lvl(fr, to, lvl - 1) for fr, to in get_pairs(path)
        )
        path_costs.append(cost)

    return min(path_costs)


# %%


def min_numeric_path(code, lvl):
    paths = numeric_paths(code)

    path_costs = []
    for path in paths:
        cost = sum(
            navigate_directional_with_lvl(fr, to, lvl) for fr, to in get_pairs(path)
        )
        path_costs.append(cost)
    return min(path_costs)


# %%

total = 0
LVL = 2
for line in lines:
    res = min_numeric_path(line, LVL)
    # print(line, res)
    val = int(line[:-1])
    total += val * res

print("part1", total)
# %%

total = 0
LVL = 25
for line in lines:
    res = min_numeric_path(line, LVL)
    # print(line, res)
    val = int(line[:-1])
    total += val * res

print("part2", total)

# %%
