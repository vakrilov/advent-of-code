# %%
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

# %%

rules = []
updates = []
reading_rules = True
for l in lines:
    if l == "":
        reading_rules = False
    elif reading_rules:
        rules.append([int(x) for x in l.split("|")])
    else:
        updates.append([int(x) for x in l.split(",")])
# %%


def is_good(u):
    is_bad = lambda r: r[0] in u and r[1] in u and u.index(r[0]) > u.index(r[1])
    return not any([is_bad(r) for r in rules])

result = sum([u[len(u) // 2] for u in updates if is_good(u)])
print("part1:", result)

# %%

def fix(u):
    # get only relevant rules
    current_rules = set([tuple(r) for r in rules if r[0] in u and r[1] in u])

    left_to_add = set(u)
    result = []
    
    has_no_rules_for_page = lambda page: not any(r for r in current_rules if r[1] == page)
    
    while len(left_to_add) > 0:
        to_add = next(page for page in left_to_add if has_no_rules_for_page(page))
        
        result.append(to_add)
        left_to_add.remove(to_add)
        
        current_rules = set([r for r in current_rules if r[0] != to_add])
    return result


fixed = [fix(u)for u in updates if not is_good(u)]
result = sum([u[len(u) // 2] for u in fixed])
print("part2:", result)
