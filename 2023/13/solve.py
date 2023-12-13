import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]


patterns = []
current_pattern = []

for line in lines:
    if line == "":
        patterns.append(current_pattern)
        current_pattern = []
    else:
        current_pattern.append(list(line))
patterns.append(current_pattern)


def transpose(pattern):
    return [list(x) for x in zip(*pattern)]


def print_pattern(pattern):
    for line in pattern:
        print("".join(line))
    print()


def eq(line1, line2):
    return all([line1[i] == line2[i] for i in range(len(line1))])

def find_H_reflection(pattern):
    for i in range(1, len(pattern)):
        checks = [(x, 2 * i - x - 1) for x in range(i) if 2 * i - x - 1 < len(pattern)]
        if all([eq(pattern[x], pattern[y]) for x, y in checks]):
            return i
    return 0


def eval_pattern(pattern):
    h_reflection = find_H_reflection(pattern)
    v_reflection = find_H_reflection(transpose(pattern))
    return h_reflection * 100 + v_reflection


print("part1", sum([eval_pattern(p) for p in patterns]))


def find_all_H_reflection(pattern):
    r = []
    for i in range(1, len(pattern)):
        checks = [(x, 2 * i - x - 1) for x in range(i) if 2 * i - x - 1 < len(pattern)]
        if all([eq(pattern[x], pattern[y]) for x, y in checks]):
            r.append(i)
    return r

def eval_smudged_pattern(pattern):
    org_h_ref = find_H_reflection(pattern)
    org_v_ref = find_H_reflection(transpose(pattern))

    for r in range(len(pattern)):
        for c in range(len(pattern[0])):
            old_char = pattern[r][c]
            new_char = "#" if old_char == "." else "."

            pattern[r][c] = new_char

            all_h = find_all_H_reflection(pattern)
            if org_h_ref in all_h:
                all_h.remove(org_h_ref)

            all_v = find_all_H_reflection(transpose(pattern))
            if org_v_ref in all_v:
                all_v.remove(org_v_ref)

            if len(all_h) == 1:
                return all_h[0] * 100 
            
            if len(all_v) == 1:
                return all_v[0] 
 
            pattern[r][c] = old_char
    return 0


print("part2", sum([eval_smudged_pattern(p) for p in patterns]))
