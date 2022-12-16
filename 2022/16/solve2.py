from functools import cache
import os
f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")

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
def turn_on_valve(open_valves, pos):
    return open_valves | 1 << pos


def is_closed(open_valves, pos):
    return not (open_valves & 1 << pos) > 0

count = 0
all_open = 0
for i in range(LEN):
    all_open = turn_on_valve(all_open, i)


@cache
def solve(pos1: int, pos2: int, open_valves: int, turns_left: int):
    global count
    count += 1
    if count % 1_000_000 == 0:
        print(count)

    if turns_left == 0:
        return 0

    if pos1 > pos2:
        return solve(pos2, pos1, open_valves, turns_left)

    score_this_turn = sum(0 if is_closed(open_valves, i)
                          else rates[i] for i in range(LEN))

    # stop moving if all valves are open
    if open_valves == all_open:
        # print("All open, turns left:", turns_left, score_this_turn)
        return score_this_turn * turns_left

    r = []

    if is_closed(open_valves, pos1) and is_closed(open_valves, pos2) and pos1 != pos2:
        open_both = turn_on_valve(turn_on_valve(open_valves, pos1), pos2)
        r.append(solve(pos1, pos2, open_both, turns_left - 1))

    # open first and move second
    if is_closed(open_valves, pos1):
        open_first = turn_on_valve(open_valves, pos1)

        for move_p2 in tunnels[pos2]:
            r.append(solve(pos1, move_p2, open_first, turns_left - 1))

    # open second and move first
    if is_closed(open_valves, pos2):
        open_second = turn_on_valve(open_valves, pos2)

        for move_p1 in tunnels[pos1]:
            r.append(solve(move_p1, pos2, open_second, turns_left - 1))

    # move both
    for move_p1 in tunnels[pos1]:
        for move_p2 in tunnels[pos2]:
            r.append(solve(move_p1, move_p2, open_valves, turns_left - 1))

    return score_this_turn + max(r)


open = 0
for i in range(LEN):
    if rates[i] == 0:
        open = turn_on_valve(open, i)

start = keys_dict["AA"]
print("Part 2:", solve(start, start, open, 26))
