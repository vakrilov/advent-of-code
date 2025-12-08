# %%
import os

# f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")
# CONNECTS = 10


f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")
CONNECTS = 1000

lines = [l.removesuffix("\n") for l in f.readlines()]
boxes = []  # [x,y,z, [circuit]]
circuits = []

i = 0
for l in lines:
    x, y, z = map(int, l.split(","))
    cir = [i]
    boxes.append([x, y, z, cir])
    circuits.append(cir)
    i += 1

distances = []
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        dx = boxes[i][0] - boxes[j][0]
        dy = boxes[i][1] - boxes[j][1]
        dz = boxes[i][2] - boxes[j][2]
        dist = dx * dx + dy * dy + dz * dz
        distances.append((dist, i, j))

sorted_distances = sorted(distances, key=lambda x: x[0])

print(sorted_distances)


# %%


def merge(circuit1, circuit2):
    if circuit1 == circuit2:
        return False

    circuit1 += circuit2
    circuits.remove(circuit2)
    for box in circuit2:
        boxes[box][3] = circuit1

    return circuit1


for _ in range(CONNECTS):
    dist, i, j = sorted_distances.pop(0)
    new_circuit = merge(boxes[i][3], boxes[j][3])

sorted_circuits = sorted(circuits, key=lambda x: len(x), reverse=True)

print(
    "part1:",
    len(sorted_circuits[0]) * len(sorted_circuits[1]) * len(sorted_circuits[2]),
)

# %%

while True:
    dist, i, j = sorted_distances.pop(0)
    new_circuit = merge(boxes[i][3], boxes[j][3])

    if len(circuits) == 1:
        print("part2:", boxes[i][0] * boxes[j][0])
        break


# %%
