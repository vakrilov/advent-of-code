import os
f = open(os.path.dirname(__file__) + "/input.txt", "r")

layers = dict()
for line in f.readlines():
    [layer, depth] = line.split(":")
    layers[int(layer)] = int(depth)

penalty = 0
for (i, depth) in layers.items():
    cycle = (depth - 1) * 2
    if i % cycle == 0:
        penalty += i * depth

print(penalty)
