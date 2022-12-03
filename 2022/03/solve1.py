import os
f = open(os.path.dirname(__file__) + "/input.txt", "r")

def priority(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 1 + 26

def findCommon(p1: str, p2: str):
    for c1 in p1:
        for c2 in p2:
            if c1 == c2:
                return c1

lines = [l.removesuffix("\n") for l in f.readlines()]
sum = 0
for line in lines:
    mid = int(len(line)/2)
    p1 = line[0:mid]
    p2 = line[mid:]
    sum += priority(findCommon(p1, p2))

print(sum)
