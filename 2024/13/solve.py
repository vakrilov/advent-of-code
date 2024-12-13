# %%
import os
import math

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

machines = []


def parseBtn(line):
    parts = line.split(", ")
    x = int(parts[0][len("Button A: X+") :])
    y = int(parts[1][len("Y+") :])
    return (x, y)


def parseTarget(line):
    parts = line.split(", ")
    x = int(parts[0][len("Prize: X=") :])
    y = int(parts[1][len("Y=") :])
    return (x, y)


def parseMachine(lines):
    btn1 = parseBtn(lines[0])
    btn2 = parseBtn(lines[1])
    target = parseTarget(lines[2])
    return (btn1, btn2, target)


for i in range(0, len(lines), 4):
    machines.append(parseMachine(lines[i : i + 3]))


# %%
def solve(btnA, btnB, target, maxCoins=100):
    solution = float("inf")
    found = False

    for pressA in range(0, maxCoins + 1):
        for pressB in range(0, maxCoins + 1):
            totalX = pressA * btnA[0] + pressB * btnB[0]
            totalY = pressA * btnA[1] + pressB * btnB[1]

            if (totalX, totalY) == target:
                solution = min(solution, pressA * 3 + pressB)
                found = True
    return solution if found else 0


print("part1", sum(solve(*m) for m in machines))
# %%

def solve2(btnA, btnB, target):
    x1, y1 = btnA
    x2, y2 = btnB
    a, b = target

    # Calucate reverse matrix to convert to coordinate system wiht btnA and btnB as base
    determinant = x1 * y2 - x2 * y1

    u = (a * y2 - b * x2) / determinant
    v = (-a * y1 + b * x1) / determinant

    if u.is_integer() and v.is_integer() and u >= 0 and v >= 0:
        return int(3 * u + v)
    else:
        return 0


print("part1 with solve2", sum(solve2(*m) for m in machines))

new_machines = [
    (btn1, btn2, (target[0] + 10000000000000, target[1] + 10000000000000))
    for btn1, btn2, target in machines
]

print("part2: ", sum(solve2(*m) for m in new_machines))


