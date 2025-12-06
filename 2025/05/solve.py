# %%
import os

# f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

ranges = []
i = 0
while lines[i] != "":
    ranges.append([int(num) for num in lines[i].split("-")])
    i += 1

products = [int(line) for line in lines[i + 1 :]]


# %%
def is_fresh(num):
    return any(r[0] <= num <= r[1] for r in ranges)


print("Part 1:", sum(is_fresh(num) for num in products))


# %%


def are_overlapping(r1, r2):
    return not (r1[1] < r2[0] or r2[1] < r1[0])


def merge_ranges(r1, r2):
    return [min(r1[0], r2[0]), max(r1[1], r2[1])]


def perform_merge(ranges):
    for i in range(len(ranges)):
        for j in range(i + 1, len(ranges)):
            if are_overlapping(ranges[i], ranges[j]):
                new_range = merge_ranges(ranges[i], ranges[j])
                ranges.pop(j)
                ranges.pop(i)
                ranges.append(new_range)
                return True

    return False


while perform_merge(ranges):
    pass

print("part 2:", sum(r[1] - r[0] + 1 for r in ranges))

# %%
