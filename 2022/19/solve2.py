from functools import cache
import re
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]


def read_blueprint(line):
    ore = re.search(r"Each ore robot costs (\d+) ore", line).group(1)
    clay = re.search(r"Each clay robot costs (\d+) ore", line).group(1)
    obsidian = re.search(
        r"Each obsidian robot costs (\d+) ore and (\d+) clay", line).group(1, 2)
    geode = re.search(
        r"Each geode robot costs (\d+) ore and (\d+) obsidian", line).group(1, 2)

    max_ore = max(int(clay[0]), int(obsidian[0]), int(geode[0]))
    max_clay = int(obsidian[1])
    max_obs = int(geode[1])
    max_geode = 1000

    blueprint = (
        ((int(geode[0]), 0, int(geode[1]), 0), (0, 0, 0, 1), max_geode, 3),
        ((int(obsidian[0]), int(obsidian[1]), 0, 0), (0, 0, 1, 0), max_obs, 2),
        ((int(clay), 0, 0, 0), (0, 1, 0, 0), max_clay, 1),
        ((int(ore), 0, 0, 0), (1, 0, 0, 0), max_ore, 0),
    )

    return blueprint


def can_build(blueprint, resources):
    return resources[0] >= blueprint[0] \
        and resources[1] >= blueprint[1] \
        and resources[2] >= blueprint[2]


def build(blueprint, resources):
    return (resources[0] - blueprint[0],
            resources[1] - blueprint[1],
            resources[2] - blueprint[2],
            resources[3])


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


MAX_GEODES = 0


@cache
def simulate(robots, resources, blueprint, time):
    global MAX_GEODES

    if time == 0:
        if resources[3] > MAX_GEODES:
            MAX_GEODES = resources[3]
            print("FOUND MORE GEODES: ", resources[3], robots, resources)
        return resources[3]

    max_possible_geodes = robots[3] * time + \
        int((time-1) * time/2) + resources[3]
    if max_possible_geodes < MAX_GEODES:
        return 0

    p = []

    for b, r, max_robots, position in blueprint:
        if robots[position] < max_robots and can_build(b, resources):
            new_robots = add(robots, r)
            after_build = build(b, resources)
            new_resources = add(after_build, robots)
            p.append(simulate(new_robots, new_resources, blueprint, time-1))

    p.append(simulate(robots, add(resources, robots), blueprint, time-1))

    return max(p)


part1_res = 0
for blueprint_number, line in enumerate(lines):
    blue = read_blueprint(line)
    MAX_GEODES = 0
    print("------------------------------------------------")
    print("Blueprint ", blueprint_number + 1) 
    print("Max robots: ", list(b[2] for b in blue))
    score = simulate((1, 0, 0, 0), (0, 0, 0, 0), blue, 24)
    print("Blueprint ", blueprint_number + 1, ": score[24]", score)
    part1_res += (blueprint_number + 1) * score

print("Part 1:", part1_res)


part2_res = 1
for blueprint_number, line in enumerate(lines):
    if blueprint_number < 3:
        blue = read_blueprint(line)
        MAX_GEODES = 0
        score = simulate((1, 0, 0, 0), (0, 0, 0, 0), blue, 32)
        print("Blueprint ", blueprint_number + 1, ": score[32]:", score)
        part2_res *= score

print("Part 2:", part2_res)
