import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]


def is_valid(template, prefix):
    for i in range(len(prefix)):
        if template[i] != "?" and template[i] != prefix[i]:
            return False
    return True


rows = []

for line in lines:
    [template, nums_part] = line.split()
    numbers = [int(x) for x in nums_part.split(",")]
    rows.append((template, numbers))


def gen(template, nums):
    if template == "":
        yield ""
        return

    if len(nums) == 0:
        rest = "." * len(template)
        if is_valid(template, rest):
            yield rest
        return

    free = len(template) - sum(nums) - len(nums) + 1
    for i in range(free + 1):
        prefix = "." * i + nums[0] * "#" + "."
        if len(prefix) > len(template):
            prefix = prefix[: len(template)]
        if is_valid(template, prefix):
            for suffix in gen(template[len(prefix) :], nums[1:]):
                yield prefix + suffix

res = 0
for t, n in rows:
    print(t, n)
    for candidate in gen(t, n):
        res += 1
        print(candidate)
    print()

print("part1", res)
