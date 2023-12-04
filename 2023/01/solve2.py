import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

string_digits = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def get_digit(str):
    if str[0].isdigit():
        return int(str[0])

    for val, d in enumerate(string_digits):
        if str.startswith(d):
            return val

    return -1


def get_value(line):
    for i in range(len(line)):
        first = get_digit(line[i:])
        if first >= 0:
            break

    for i in range(len(line) - 1, -1, -1):
        second = get_digit(line[i:])
        if second >= 0:
            break
        
    return 10 * first + second


values = [get_value(line) for line in f.readlines()]

part2 = sum(values)

print(f"part2: {part2}")
