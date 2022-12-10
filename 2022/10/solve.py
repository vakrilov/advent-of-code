import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

cycle = 0
value = 1
result = 0

def tick(): 
    global cycle
    global result

    cycle += 1
    position = cycle % 40

    # Part 1
    if cycle  % 40 == 20:
        result += cycle*value

    # Part 2
    if value <= position and position <= value + 2:
        print("#", end="")
    else:
        print(".", end="")

    if cycle % 40 == 0:
        print("")

for line in lines:
    if line == "noop":
        tick()
    else:
        tick()
        tick()
        value += int(line[5:])

print("Part 1:", result)
