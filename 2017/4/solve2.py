f = open("./2017/4/input.txt", "r")
# f = open("./sample.txt", "r")


def hash(word: str) -> int:
    sum = 0
    for ch in word:
        ch = ord(ch) - ord('a') + 1
        sum += 10**ch
    return sum


sum = 0
for line in f.readlines():
    words = list(map(hash, line.split()))
    if len(words) == len(set(words)):
        sum += 1

print(sum)
