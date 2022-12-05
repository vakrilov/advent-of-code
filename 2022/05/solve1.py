import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

stacks = [[] for _ in range(10)]

lines = [l.removesuffix("\n") for l in f.readlines()]
split = lines.index("")

for line in lines[:split]:
    for i in range(0, len(line), 4): # each stack is 4 symbols thick
        if line[i+1].isupper(): # skip empty stacks
            stacks[1 + i//4].insert(0, line[i+1])

for line in lines[split + 1:]:
    [move, fr, to] = [int(x) for x in line.split(" ")[1::2]]
    for _ in range(move):
        stacks[to].append(stacks[fr].pop())

print("Part 1: ", "".join([s[-1] for s in stacks if len(s[-1:]) > 0]))
