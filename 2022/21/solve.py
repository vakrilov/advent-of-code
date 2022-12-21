import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")


monkeys = {}
operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
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


print("Part 1:", int(get_value("root")))
