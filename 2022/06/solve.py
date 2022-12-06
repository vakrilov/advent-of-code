import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")


def find_non_repeat(line: str, length: int):
    """ O(len(line) * length) """
    for i in range(len(line)):
        if len(set(line[i-length:i])) == length:
            return i


def find_non_repeat_faster(line: str, length: int):
    """ O(len(line)) """
    repeats = dict()

    def add(key: str):
        repeats[key] = repeats.get(key, 0) + 1

    def remove(key: str):
        if repeats[key] == 1:
            del repeats[key]
        else:
            repeats[key] -= 1

    for i, char in enumerate(line):
        add(char)
        if i >= length:
            remove(line[i - length])

        if len(repeats) == length:
            return i + 1


first_line = f.read()
print("Part 1 slower: ", find_non_repeat(first_line, 4))
print("Part 1 faster: ", find_non_repeat_faster(first_line, 4))
print()
print("Part 2 slower: ", find_non_repeat(first_line, 14))
print("Part 2 faster: ", find_non_repeat_faster(first_line, 14))
