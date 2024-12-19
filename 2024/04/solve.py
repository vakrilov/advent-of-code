# %%
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

L = len(lines)


# %%
def XMAS(r, c):
    result = 0
    if c + 3 < L:
        test = lines[r][c] + lines[r][c + 1] + lines[r][c + 2] + lines[r][c + 3]
        result += test == "XMAS" or test == "SAMX"

    if r + 3 < L:
        test = lines[r][c] + lines[r + 1][c] + lines[r + 2][c] + lines[r + 3][c]
        result += test == "XMAS" or test == "SAMX"

    if r + 3 < L and c + 3 < L:
        test = (
            lines[r][c]
            + lines[r + 1][c + 1]
            + lines[r + 2][c + 2]
            + lines[r + 3][c + 3]
        )
        result += test == "XMAS" or test == "SAMX"

    if r + 3 < L and c - 3 >= 0:
        test = (
            lines[r][c]
            + lines[r + 1][c - 1]
            + lines[r + 2][c - 2]
            + lines[r + 3][c - 3]
        )
        result += test == "XMAS" or test == "SAMX"

    return result


print("part 1:", sum([XMAS(r, c) for r in range(L) for c in range(L)]))


# %%


def MAS(r, c):
    test1 = lines[r - 1][c - 1] + lines[r][c] + lines[r + 1][c + 1]
    test2 = lines[r - 1][c + 1] + lines[r][c] + lines[r + 1][c - 1]
    return (test1 == "MAS" or test1 == "SAM") and (test2 == "MAS" or test2 == "SAM")


print("part 2:", sum([MAS(r, c) for r in range(1, L - 1) for c in range(1, L - 1)]))

# %%
