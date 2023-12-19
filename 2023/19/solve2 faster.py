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


def solve(workflow_name, ranges):
    if workflow_name == "A":
        res = 1
        for r in ranges.values():
            res *= max(0, r[1] - r[0])
        return res

    if workflow_name == "R":
        return 0

    rules = workflows[workflow_name]
    res = 0
    for r in rules[:-1]:
        key, op, arg, out = r
        newRange = ranges.copy()
        if op == "<":
            newRange[key] = (ranges[key][0], min(ranges[key][1], arg))
            res += solve(out, newRange)

            ranges[key] = (max(ranges[key][0], arg), ranges[key][1])

        if op == ">":
            newRange[key] = (max(ranges[key][0], arg + 1), ranges[key][1])
            res += solve(out, newRange)

            ranges[key] = (ranges[key][0], min(ranges[key][1], arg + 1))

    res += solve(rules[-1], ranges.copy())
    return res


ranges = {
    "x": (1, 4001),
    "m": (1, 4001),
    "a": (1, 4001),
    "s": (1, 4001),
}

print("part2:", solve("in", ranges))
