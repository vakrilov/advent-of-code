import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]


def hash(s):
    res = 0
    for c in s:
        res += ord(c)
        res *= 17
        res %= 256
    return res


parts = lines[0].split(",")

result = print("part1:", sum([hash(p) for p in parts]))

boxes = [[] for _ in range(256)]
for p in parts:
    if "=" in p:
        [lbl, num] = p.split("=")
        num = int(num)
        h = hash(lbl)

    if "-" in p:
        lbl = p[0:-1]
        num = None

    h = hash(lbl)
    box = boxes[h]
    labels = [lbl for lbl, _ in box]
    idx = labels.index(lbl) if lbl in labels else None

    if num is not None:
        if idx is None:
            box.append((lbl, num))
        else:
            box[idx] = (lbl, num)
    else:
        if idx is not None:
            box.pop(idx)


result = 0
for box_idx, box in enumerate(boxes):
    for slot, (_, num) in enumerate(box):
        result += (box_idx + 1) * (slot + 1) * num
print("part2:", result)
