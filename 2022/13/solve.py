import os
import json
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")


def compare(l1: int | list[int], l2: int | list[int]):
    if isinstance(l1, int) and isinstance(l2, int):
        return l1 - l2

    if isinstance(l1, list) and isinstance(l2, list):
        for left, right in zip(l1, l2):
            res = compare(left, right)
            if res != 0:
                return res
        return len(l1) - len(l2)

    if isinstance(l1, list) and isinstance(l2, int):
        return compare(l1, [l2])

    if isinstance(l1, int) and isinstance(l2, list):
        return compare([l1], l2)

    raise ValueError("Unexpected input")


lines = [json.loads(l) for l in f.readlines() if l != "\n"]

right_pairs = [
    i//2+1 for i in range(0, len(lines), 2) if compare(lines[i], lines[i+1]) < 0]
print("Part 1:", sum(right_pairs))

div1_index = sum(1 for l in lines if compare(l, [[2]]) < 0) + 1
div2_index = sum(1 for l in lines if compare(l, [[6]]) < 0) + 2
print("Part 2:", div1_index * div2_index)
