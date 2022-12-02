import os
f = open(os.path.dirname(__file__) + "/input.txt", "r")

results = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Y": 3,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "C Z": 3,
}

shape = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

result = 0
for line in f.readlines():
    line = line.removesuffix("\n")
    result += shape[line[2]] + results[line]

print(result)
