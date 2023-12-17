import os
import heapq

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

LEN = len(lines)
costs = [[int(ch) for ch in line] for line in lines]


def is_valid(row, col):
    return row >= 0 and row < LEN and col >= 0 and col < LEN


def get_neighbours(row, col, dir, steps):
    res = []
    if dir == "d":
        res.append((row, col - 1, "l", 1))
        res.append((row, col + 1, "r", 1))
        if steps < 3:
            res.append((row + 1, col, "d", steps + 1))
    elif dir == "u":
        res.append((row, col - 1, "l", 1))
        res.append((row, col + 1, "r", 1))
        if steps < 3:
            res.append((row - 1, col, "u", steps + 1))
    elif dir == "l":
        res.append((row - 1, col, "u", 1))
        res.append((row + 1, col, "d", 1))
        if steps < 3:
            res.append((row, col - 1, "l", steps + 1))
    elif dir == "r":
        res.append((row - 1, col, "u", 1))
        res.append((row + 1, col, "d", 1))
        if steps < 3:
            res.append((row, col + 1, "r", steps + 1))

    return [n for n in res if is_valid(n[0], n[1])]


front = []
start = (0, 0, "d", 0)
visited = set({start})
heapq.heappush(front, (0, start))
while front:
    current_cost, info = heapq.heappop(front)

    if info[0] == LEN - 1 and info[1] == LEN - 1:
        print("part1:", current_cost)
        break

    for n in get_neighbours(*info):
        if n not in visited:
            visited.add(n)
            new_cost = current_cost + costs[n[0]][n[1]]
            heapq.heappush(front, (new_cost, n))

