# %%
import os

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
def solve(btnA, btnB, target):
    solution = float("inf")
    found = False

    for pressA in range(0, 101):
        for pressB in range(0, 101):
            totalX = pressA * btnA[0] + pressB * btnB[0]
            totalY = pressA * btnA[1] + pressB * btnB[1]

            if (totalX, totalY) == target:
                solution = min(solution, pressA * 3 + pressB)
                found = True
    return solution if found else 0


print("part1", sum(solve(*m) for m in machines))
# %%
