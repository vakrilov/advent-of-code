import os
f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")

def find_non_repeat(line: str, length: int):
    for i in range(length, len(line)):
        if len(set(line[i-length:i])) == length:
            return i

first_line = f.read()
print("Part 1: ", find_non_repeat(first_line, 4))
print("Part 2: ", find_non_repeat(first_line, 14))
