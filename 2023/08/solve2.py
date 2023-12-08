import os
import math

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")
lines = [l.removesuffix("\n") for l in f.readlines()]

lr = lines[0].strip()
mymap = {}

for line in lines[2:]:
    fr = line[0:3]
    left = line[7:10]
    right = line[12:15]
    mymap[fr] = (left, right)


starting_nodes = [node for node in mymap if node[2] == "A"]

def go(dir, node):
    return mymap[node][0] if dir == "L" else mymap[node][1]

def simulate(node):
    step = 0    
    while node[2] != "Z":
        node = go(lr[step % len(lr)], node)
        step += 1
    return step

# looks like all starting nodes cycle - nice!
cycles = [simulate(node) for node in starting_nodes]

print (math.lcm(*cycles))
