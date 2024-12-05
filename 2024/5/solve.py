# %%
import os

f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

# %%

rules = []
updates = []

reading_rules = True
for l in lines:
    if l == "":
        reading_rules = False
        continue

    if reading_rules:
        rules.append([int(x) for x in l.split("|")])
    else:
        updates.append([int(x) for x in l.split(",")])


# %%
def is_good(u):
    for r in rules:
        try:
            if u.index(r[0]) > u.index(r[1]):
                return False
        except ValueError:
            continue
    return True


result = sum([u[len(u) // 2] for u in updates if is_good(u)])
print("part1:", result)

# %%
to_fix = [u for u in updates if not is_good(u)]
print(to_fix)

# %%
