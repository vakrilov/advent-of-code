f = open("./8/input.txt", "r")

checks = {
    ">": lambda a, b: a > b,
    ">=": lambda a, b: a >= b,
    "<": lambda a, b: a < b,
    "<=": lambda a, b: a <= b,
    "==": lambda a, b: a == b,
    "!=": lambda a, b: a != b,
}

registers = dict()
highest = 0
for line in f.readlines():
    str = line.split()
    checkReg, check, checkVal = str[4], str[5], int(str[6])
    regVal = registers.get(checkReg, 0)

    shouldExecute = checks[check](regVal, checkVal)

    if checks[check](regVal, checkVal):
        register, operation, val = str[0], str[1], int(str[2])
        currentVal = registers.get(register, 0)
        currentVal += val if operation == "inc" else -val
        registers[register] = currentVal
        highest = max(highest, currentVal)


# print(registers)
print("1: ", max(registers.values()))
print("2: ", highest)
