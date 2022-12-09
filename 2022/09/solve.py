import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")


def add(x, y): return (x[0] + y[0], x[1] + y[1])
def sub(x, y): return (x[0] - y[0], x[1] - y[1])
def scale(x): return 1 if x > 0 else -1


def pullKnot(head, tail):
    diff = sub(head, tail)

    if (abs(diff[0]) + abs(diff[1])) > 2:
        return add(tail, (scale(diff[0]), scale(diff[1])))
    elif abs(diff[0]) > 1:
        return add(tail, (scale(diff[0]), 0))
    elif abs(diff[1]) > 1:
        return add(tail, (0, scale(diff[1])))
    else:
        return tail


directions = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
Rope = [(0, 0) for _ in range(10)]
visited_second = set()
visited_tail = set()

for line in f.readlines():
    split = line.split()
    direction, step = directions[split[0]], int(split[1])

    for i in range(int(split[1])):
        Rope[0] = add(Rope[0], direction)

        for i in range(9):
            Rope[i+1] = pullKnot(Rope[i], Rope[i+1])

        visited_second.add((Rope[1][0], Rope[1][1]))
        visited_tail.add((Rope[9][0], Rope[9][1]))

print("Part 1:", len(visited_second))
print("Part 2:", len(visited_tail))
