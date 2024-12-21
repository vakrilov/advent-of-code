# %%
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]
L = len(lines)

numeric_pad = ["789", "456", "123", " 0A"]


def get_pos(symbol, pad):
    for row, l in enumerate(pad):
        if symbol in l:
            return (l.index(symbol), row)


def num_dx(dx):
    return (">" if dx > 0 else "<") * abs(dx)


def num_dy(dy):
    return ("v" if dy > 0 else "^") * abs(dy)


def navigate_numeric(fr, to):
    fr_pos = get_pos(fr, numeric_pad)
    to_pos = get_pos(to, numeric_pad)

    dx = to_pos[0] - fr_pos[0]
    dy = to_pos[1] - fr_pos[1]

    if fr in "0A" and to in "147":
        # print("Special case")
        return num_dy(dy) + num_dx(dx) + "A"
    else:
        return num_dx(dx) + num_dy(dy) + "A"


# print(navigate_numeric("7", "A"))
# print(navigate_numeric("A", "7"))
# print(navigate_numeric("0", "8"))


directional_pad = [" ^A", "<v>"]


def navigate_directional(fr, to):
    fr_pos = get_pos(fr, directional_pad)
    to_pos = get_pos(to, directional_pad)

    dx = to_pos[0] - fr_pos[0]
    dy = to_pos[1] - fr_pos[1]

    if fr == "<":
        return num_dx(dx) + num_dy(dy) + "A"
    else:
        return num_dy(dy) + num_dx(dx) + "A"


def path(code):
    prev = "A"
    dir1_nav = ""
    for ch in code:
        dir1_nav += navigate_numeric(prev, ch)
        prev = ch
    # print(dir1_nav)

    prev = "A"
    dir2_nav = ""
    for ch in dir1_nav:
        dir2_nav += navigate_directional(prev, ch)
        prev = ch
    # print(dir2_nav)

    prev = "A"
    dir3_nav = ""
    for ch in dir2_nav:
        dir3_nav += navigate_directional(prev, ch)
        prev = ch

    # print(dir3_nav)
    # print(len(dir3_nav))

    return len(dir3_nav)


total = 0
for line in lines:
    res = path(line)
    val = int(line[:-1])
    total += val * res

print("part1", total)
# %%
