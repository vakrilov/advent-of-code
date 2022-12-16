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
def turn_on_valve(open_valves, i):
    return open_valves[:i] + (True,) + open_valves[i+1:]


@cache
def solve(position: int, open_valves, turns_left: int):
    if turns_left == 0:
        return 0

    current_flow = sum(rates[i] if open_valves[i] else 0 for i in range(LEN))

    # stop moving if all valves are open
    if all(open_valves):
        return current_flow * turns_left

    possible = []
    if not open_valves[position]:
        possible.append(solve(position, turn_on_valve(
            open_valves, position), turns_left - 1))

    for new_pos in tunnels[position]:
        possible.append(solve(new_pos, open_valves, turns_left - 1))

    return current_flow + max(possible)


open = tuple(True if rates[i] == 0 else False for i in range(LEN))
start = keys_dict["AA"]
print("Part 1:", solve(start, open, 30))
