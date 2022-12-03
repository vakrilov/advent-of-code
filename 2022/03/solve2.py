import os
f = open(os.path.dirname(__file__) + "/input.txt", "r")


def priority(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 1 + 26


def findCommon3(s1: str, s2: str, s3):
    overlap = set(s1) & set(s2) & set(s3)
    return overlap.pop()


lines = [l.removesuffix("\n") for l in f.readlines()]
sum = 0
for i in range(0, len(lines), 3):
    common = findCommon3(lines[i], lines[i+1], lines[i+2])
    sum += priority(common)

print(sum)
