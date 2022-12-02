import os
f = open(os.path.dirname(__file__) + "/input.txt", "r")

res = 0
sum = 0

shape = {
    "A X": 3,
    "A Y": 1,
    "A Z": 2,
    "B X": 1,
    "B Y": 2,
    "B Z": 3,
    "C X": 2,
    "C Y": 3,
    "C Z": 1,
}

result = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

for line in f.readlines():
    line = line.removesuffix("\n")
    sum += shape[line] + result[line[2]]

print(sum)
