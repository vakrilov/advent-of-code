import os
f = open(os.path.dirname(__file__) + "/input.txt", "r")

directions = {"n": 0, "s": 0, "nw": 0, "sw": 0, "ne": 0, "se": 0}


def distance():
    n = directions["n"] - directions["s"]
    ne = directions["ne"] - directions["sw"]
    se = directions["se"] - directions["nw"]
    ne += n
    se -= n

    if ne * se > 0:
        return abs(ne+se)
    else:
        return max(abs(ne), abs(se))


maxDistance = 0
for x in f.read().split(","):
    directions[x] += 1
    maxDistance = max(maxDistance, distance())

print("end distance: ", distance())
print("max distance: ", maxDistance)
