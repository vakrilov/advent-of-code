import os
import re

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

workflows = {}
parts = []

part_pattern = re.compile(r"([xmas]+)([<>])(\d+):(\w+)")


def parse_workflow(line):
    name, steps_strings = line.split("{")
    steps_strings = steps_strings.removesuffix("}").split(",")
    steps = []

    for str in steps_strings:
        if ":" in str:
            match = part_pattern.search(str)
            key, op, arg_str, out = match.groups()
            arg = int(arg_str)
            steps.append((key, op, arg, out))

        else:
            steps.append(str)

    return name, steps


for line in lines:
    if line == "":
        break
    else:
        name, steps = parse_workflow(line)
        workflows[name] = steps


def apply_rules(part, rules):
    for rule in rules[:-1]:
        key, op, arg, out = rule

        value = part[key]
        if op == ">" and value > arg:
            return out
        if op == "<" and value < arg:
            return out

    return rules[-1]


ranges = {
    "x": [1, 4001],
    "m": [1, 4001],
    "a": [1, 4001],
    "s": [1, 4001],
}

for rules in workflows.values():
    for r in rules[:-1]:
        key, op, arg, out = r
        if op == "<":
            ranges[key].append(arg)
        if op == ">":
            ranges[key].append(arg + 1)

for range in ranges.values():
    range.sort()


def is_accepted(part):
    rule_name = "in"
    while rule_name != "A" and rule_name != "R":
        rule_name = apply_rules(part, workflows[rule_name])
    return rule_name == "A"


# print([len(r) for r in ranges.values()])
# exit()
result = 0
total = len(ranges["x"]) * len(ranges["m"]) * len(ranges["a"]) * len(ranges["s"])
c = 0
for x, end_x in zip(ranges["x"], ranges["x"][1:]):
    l_x = end_x - x
    for m, end_m in zip(ranges["m"], ranges["m"][1:]):
        l_m = end_m - m
        for a, end_a in zip(ranges["a"], ranges["a"][1:]):
            l_a = end_a - a
            for s, end_s in zip(ranges["s"], ranges["s"][1:]):
                l_s = end_s - s
                c += 1
                if c % 1000_000 == 0:
                    print(c//1000_000, "/", total//1000_000)

                part = {"x": x, "m": m, "a": a, "s": s}
                if is_accepted(part):
                    result += l_s * l_a * l_m * l_x
print("part2:", result)
