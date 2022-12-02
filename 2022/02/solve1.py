import os
f = open(os.path.dirname(__file__) + "/input.txt", "r")

points = {
    # "elf me": score + sign
    "A X": 3 + 1,
    "A Y": 6 + 2,
    "A Z": 0 + 3,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 6 + 1,
    "C Y": 0 + 2,
    "C Z": 3 + 3,
}

print(sum([points[l.removesuffix("\n")] for l in f.readlines()]))
