import os
f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")


def solve(line: str, length: int):
    return 0


lines = [l.removesuffix("\n") for l in f.readlines()]
res = 0
for line in lines:
    res += 1

print(res)
