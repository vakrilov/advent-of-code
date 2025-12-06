# %%
import os

# f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]
ranges = [tuple(map(int, r.split("-"))) for r in lines[0].split(",")]
# a, b = [int(x) for x in ranges[0].split("-")]


def is_repeated(s: str, times: int) -> bool:
    l = len(s)
    if l % times != 0:
        return False

    part_len = l // times
    pattern = s[:part_len]

    for i in range(1, times):
        if s[i * part_len : (i + 1) * part_len] != pattern:
            return False

    return True


def is_invalid(s: str) -> bool:
    l = len(s)
    for t in range(2, l + 1):
        if is_repeated(s, t):
            return True

    return False


is_invalid("1212")
is_invalid("1212121212")
is_invalid("111111")


# %%
part1 = sum(n for r in ranges for n in range(r[0], r[1] + 1) if is_repeated(str(n), 2))
print("part1:", part1)

# %%
part2 = sum(n for r in ranges for n in range(r[0], r[1] + 1) if is_invalid(str(n)))
print("part2:", part2)

# %%
