import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

digits = [[int(ch) for ch in line if ch.isdigit()] for line in f.readlines()]

part1 = sum(d[0] * 10 + d[-1] for d in digits)

print(f"part1: {part1}")
