# %%
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

# %%

equations = []

for l in lines:
    parts = l.split(":")
    res = int(parts[0])
    args = [int(x) for x in parts[1].strip().split(" ")]
    equations.append((res, args))


# %%
def test_part1(r, args):
    if len(args) == 1:
        return args[0] == r

    add = [args[0] + args[1]]
    mul = [args[0] * args[1]]
    rest = args[2:]

    return test_part1(r, add + rest) or test_part1(r, mul + rest)


def test_part2(r, args):
    if len(args) == 1:
        return args[0] == r

    add = [args[0] + args[1]]
    mul = [args[0] * args[1]]
    con = [int(str(args[0]) + str(args[1]))]
    rest = args[2:]

    return (
        test_part2(r, add + rest)
        or test_part2(r, mul + rest)
        or test_part2(r, con + rest)
    )


print(
    "part1",
    sum([r for r, args in equations if test_part1(r, args)]),
)

print(
    "part2",
    sum([r for r, args in equations if test_part2(r, args)]),
)
# %%
