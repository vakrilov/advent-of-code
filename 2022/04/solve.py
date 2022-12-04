import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

contained = 0
overlap = 0
for line in f.readlines():
    [start1, end1, start2, end2] = [
        int(x) for x in line.replace("-", ",").split(",")]

    if (start1 <= start2 and end2 <= end1) or (start2 <= start1 and end1 <= end2):
        contained += 1

    # not (one range start after the other ends)
    if not (end1 < start2 or end2 < start1):
        overlap += 1

print("Part 1: ", contained)
print("Part 2: ", overlap)
