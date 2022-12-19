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


input_rates = [0] * LEN
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
    input_rates[keys_dict[name]] = int(split[1])

    paths_input = split[2:]
    for p in paths_input:
        add_if_needed(p, keys_dict)
        tunnels[keys_dict[name]].append(keys_dict[p])

valves = list(i for i in range(
    LEN) if input_rates[i] != 0) + [keys_dict["AA"], ]
rates = list(input_rates[i] for i in range(LEN) if input_rates[i] != 0) + [0]
start = len(valves) - 1


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


distances = [[0] * len(valves) for _ in range(len(valves))]

for i, name_i in enumerate(valves):
    for j, name_j in enumerate(valves):
        distances[i][j] = dist(name_i, name_j)


def generate_paths(current, open_valves: set[int], time, current_path, generated_paths):
    generated_paths.append(current_path)

    for next_node in open_valves:
        d = distances[current][next_node]
        if time > d + 1:
            generate_paths(next_node, open_valves - {next_node},
                           time-d-1, current_path + (next_node,), generated_paths)


def eval_path(current, path, time):
    result = 0
    for next_node in path:
        d = distances[current][next_node]
        time -= d + 1
        result += time * rates[next_node]
        current = next_node

    return result


# part 1
paths = []
generate_paths(start, set(range(len(valves) - 1)), 30, (), paths)
print("[Part 1]: paths to eval", len(paths))
print("Part 1:", max(eval_path(start, p, 30) for p in paths))

# part 2
player1_paths = []
generate_paths(start, set(range(len(valves) - 1)), 26, (), player1_paths)
print("[Part 2]: paths to eval", len(player1_paths))
best = 0
for i, p in enumerate(player1_paths):
    p1_score = eval_path(start, p, 26)

    if p1_score < best / 2:
        continue

    p2_paths = []
    subset = set(range(len(valves)-1)) - set(p)
    generate_paths(start, subset, 26, (), p2_paths)

    p2_score = max(eval_path(start, p, 26) for p in p2_paths)
    best = max(best, p1_score + p2_score)
print("Part 2:", best)
