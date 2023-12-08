import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")
lines = [l.removesuffix("\n") for l in f.readlines()]

lr = lines[0].strip()
mymap = {}

for line in lines[2:]:
    fr = line[0:3]
    left = line[7:10]
    right = line[12:15]
    mymap[fr] = (left, right)


step = 0
current = "AAA"
while current != "ZZZ":
    if lr[step%len(lr)] == "L":
        current = mymap[current][0]
    else:
        current = mymap[current][1]
    step += 1





print(step)
