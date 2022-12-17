from functools import cache
import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

rates_dict = {}
tunnels_dict = {}

lines = [l.removesuffix("\n") for l in f.readlines()]
LEN = len(lines)
keys_dict = {}


def add_if_needed(key, dictionary):
    if not key in dictionary:
        dictionary[key] = len(dictionary)


rates = [0] * LEN
tunnels = [[] for _ in range(LEN)]

for line in lines:
    line = line.replace("Valve ", "")\
        .replace("has flow rate=", "")\
        .replace("; tunnels lead", "")\
        .replace("; tunnel leads", "")\
        .replace("to valves ", "")\
        .replace("to valve ", "")\
        .replace(", ", " ")
    split = line.split(" ")

    name = split[0]
    add_if_needed(name, keys_dict)
    rates[keys_dict[name]] = int(split[1])

    paths = split[2:]
    for p in paths:
        add_if_needed(p, keys_dict)
        tunnels[keys_dict[name]].append(keys_dict[p])


@cache
def open_valve(open_valves, i):
    return open_valves[:i] + (True,) + open_valves[i+1:]


@cache
def dist(fr: int, to: int):
    stack = [(fr, 0)]
    visited = set()

    while True:
        current, cost = stack.pop(0)
        if current == to:
            return cost
        visited.add(current)

        for next in tunnels[current]:
            if not next in visited:
                stack.append((next, cost+1))


count = 0


@cache
def solve(p1: int, p2: int, open_valves: list[bool], turns_left: int, p1_turns, p2_turns):
    if turns_left == 0:
        return 0

    # global count
    # count += 1
    # if count % 1000 == 0:
    #     print(count)

    current_flow = sum(rates[i] if open_valves[i] else 0 for i in range(LEN))

    if all(open_valves):
        return current_flow * turns_left

    possible = [0]
    where_to_go = [i for i, val in enumerate(open_valves) if not val]
    
    if p1_turns == 0:
        for next_valve in where_to_go:
            turns_to_open = dist(p1, next_valve) + 1
            if turns_to_open < turns_left:
                new_valves = open_valve(open_valves, next_valve)
                possible.append(turns_to_open * current_flow +
                                solve(next_valve, p2, new_valves, turns_left - turns_to_open, 0, turns_to_open))

    return max(possible)


open = tuple(True if rates[i] == 0 else False for i in range(LEN))
start = keys_dict["AA"]
print("Part 2:", solve(start, start, open, 26, 0, 0))
