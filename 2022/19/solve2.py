from functools import cache
import re
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")


def read_blueprint(line):
    ore = re.search(r"Each ore robot costs (\d+) ore", line).group(1)
    clay = re.search(r"Each clay robot costs (\d+) ore", line).group(1)
    obsidian = re.search(
        r"Each obsidian robot costs (\d+) ore and (\d+) clay", line).group(1, 2)
    geode = re.search(
        r"Each geode robot costs (\d+) ore and (\d+) obsidian", line).group(1, 2)

    blueprint = (
        ((int(geode[0]), 0, int(geode[1]), 0), (0, 0, 0, 1)),
        ((int(obsidian[0]), int(obsidian[1]), 0, 0), (0, 0, 1, 0)),
        ((int(clay), 0, 0, 0), (0, 1, 0, 0)),
        ((int(ore), 0, 0, 0), (1, 0, 0, 0)),
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

    geode_robots = robots[3]
    max_possible_geodes = geode_robots * time + \
        int((time-1) * time/2) + resources[3]
    if max_possible_geodes < MAX_GEODES:
        return 0

    p = []

    for b, r in blue:
        if can_build(b, resources):
            new_robots = add(robots, r)
            after_build = build(b, resources)
            new_resources = add(after_build, robots)
            p.append(simulate(new_robots, new_resources, blueprint, time-1))

    p.append(simulate(robots, add(resources, robots), blueprint, time-1))

    return max(p)


res = 1
for i, line in enumerate(f.readlines()):
    if i < 3:
        blue = read_blueprint(line)
        MAX_GEODES = 0
        score = simulate((1, 0, 0, 0), (0, 0, 0, 0), blue, 32)
        print(score)
        res *= score

print("Part 2:", res)
