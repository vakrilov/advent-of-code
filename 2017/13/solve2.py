import os
f = open(os.path.dirname(__file__) + "/input.txt", "r")

layers = dict()
for line in f.readlines():
    [layer, depth] = line.split(":")
    layers[int(layer)] = int(depth)


def tryWithDelay(delay: int):
    penalty = 0
    for (i, depth) in layers.items():
        cycle = (depth - 1) * 2
        if (i + delay) % cycle == 0:
            penalty += i * depth
            return False
    return True


delay = 0
while not tryWithDelay(delay):
    delay += 1
print(delay)
