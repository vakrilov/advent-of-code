import os
from functools import cache
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")


monkeys = {}
marked = set()
operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


# res = arg1 [op] x
reverse_operations_arg1 = {
    "+": lambda x, res: res - x,
    "-": lambda x, res: res + x,
    "*": lambda x, res: res / x,
    "/": lambda x, res: res * x,
}

# res = x [op] arg2
reverse_operations_arg2 = {
    "+": lambda x, res: res - x,
    "-": lambda x, res: x - res,
    "*": lambda x, res: res / x,
    "/": lambda x, res: x / res,
}

lines = [l.removesuffix("\n") for l in f.readlines()]
for line in lines:
    name, value = line.split(": ")
    monkeys[name] = value


def get_value(monkey):
    val = monkeys[monkey]

    if val[0].isalpha():
        arg1, op, arg2 = val[0:4], val[5], val[7:]
        return operations[op](get_value(arg1), get_value(arg2))
    else:
        return int(val)


def mark_path(monkey):
    if (monkey == "humn"):
        marked.add(monkey)
        return True

    val = monkeys[monkey]
    if not val[0].isalpha():
        return False

    arg1, arg2 = val[0:4], val[7:]
    if mark_path(arg1) or mark_path(arg2):
        marked.add(monkey)
        return True


def expect_value(monkey, expect):
    if monkey == "humn":
        return expect

    val = monkeys[monkey]
    arg1, op, arg2 = val[0:4], val[5], val[7:]

    if arg1 in marked:
        arg2_value = get_value(arg2)
        new_expect = reverse_operations_arg1[op](arg2_value, expect)
        return expect_value(arg1, new_expect)
    else:
        arg1_value = get_value(arg1)
        new_expect = reverse_operations_arg2[op](arg1_value, expect)
        return expect_value(arg2, new_expect)


mark_path("root")
left, right = monkeys["root"][0:4], monkeys["root"][7:]
if left in marked:
    expected = get_value(right)
    answer = expect_value(left, expected)
else:
    expected = get_value(left)
    answer = expect_value(right, expected)

print("Part 2:", int(answer))
