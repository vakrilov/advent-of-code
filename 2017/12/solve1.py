import os
f = open(os.path.dirname(__file__) + "/input.txt", "r")

links = []
for line in f.readlines():
    links.append([int(x) for x in line[line.index("<->") + 4:].split(",")])

visited = set()
queue = list()
def visit(node): 
    if node in visited:
        return
    visited.add(node)
    queue.extend(links[node])

visit(0)
while len(queue) > 0:
    visit(queue.pop())

print(len(visited))
