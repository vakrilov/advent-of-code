from itertools import product
f = open("./input.txt", "r")
# f = open("./sample.txt", "r")

sum = 0
for line in f.readlines():
    parsed = list(map(int, line.split()))
    for i, j in product(range(len(parsed)), range(len(parsed))):
        if i != j and parsed[i] % parsed[j] == 0:
            sum += parsed[i] // parsed[j]

print(sum)
