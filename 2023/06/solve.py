from numpy import prod
import math

EPS = 0.00001

def solve(time: int, limit: int):
    term = math.sqrt(time * time - 4 * limit)
    x1 = (time - term) / 2
    x2 = (time + term) / 2
    return math.floor(x2 - EPS) - math.ceil(x1 + EPS) + 1


times = [61, 70, 90, 66]
limit = [643, 1184, 1362, 1041]

print("part1:",prod([solve(time, limit) for time, limit in zip(times, limit)]))

times = [61709066]
limit = [643118413621041]

print("part2:", solve(61709066, 643118413621041))
