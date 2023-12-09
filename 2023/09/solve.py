import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

def extend(seq: list[int]):
    stack = [seq]
    current = seq

    while not all([num == 0 for num in current]):
        current = [b - a for a, b in zip(current, current[1:])]
        stack.append(current)

    current += [0, 0]

    while len(stack) > 1:
        stack.pop()
        stack[-1].insert(0, stack[-1][0] - current[0])
        stack[-1].append(stack[-1][-1] + current[-1])
        current = stack[-1]

lines = [l.removesuffix("\n") for l in f.readlines()]
sequences = [[int(num) for num in line.split()] for line in lines]

for seq in sequences:
    extend(seq)

print("part1:", sum([seq[-1] for seq in sequences]))
print("part2:", sum([seq[0] for seq in sequences]))
