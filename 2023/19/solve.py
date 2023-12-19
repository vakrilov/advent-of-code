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


def parse_part(line):
    line = line[1:-1]
    setters = line.split(",")
    part = {}
    for setter in setters:
        key, value = setter.split("=")
        part[key] = int(value)

    return part


def apply_rules(part, rules):
    for rule in rules[:-1]:
        key, op, arg, out = rule

        value = part[key]
        if op == ">" and value > arg:
            return out
        if op == "<" and value < arg:
            return out

    return rules[-1]



parsing_parts = False
for line in lines:
    if line == "":
        parsing_parts = True
        continue
    if parsing_parts:
        parts.append(parse_part(line))
    else:
        name, steps = parse_workflow(line)
        workflows[name] = steps

result = 0
for part in parts:
    rule_name = "in"
    while rule_name != "A" and rule_name != "R":
        rule_name = apply_rules(part, workflows[rule_name])

    if rule_name == "A":
        result += sum(part.values())

print("part1:", result)
