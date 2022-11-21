f = open("./2017/4/input.txt", "r")
# f = open("./sample.txt", "r")


sum = 0
for line in f.readlines():
    words = line.split()
    if len(words) == len(set(words)):
        sum += 1

print(sum)
