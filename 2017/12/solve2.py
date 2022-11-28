import os
f = open(os.path.dirname(__file__) + "/input.txt", "r")

links = []
for line in f.readlines():
    links.append([int(x) for x in line[line.index("<->") + 4:].split(",")])

visited = set()
def visit(node, queue):
    if node in visited:
        return
    visited.add(node)
    queue.extend(links[node])


groups = 0
for i in range(len(links)):
    if i not in visited:
        groups += 1
        queue = [i]
        while len(queue) > 0:
            visit(queue.pop(), queue)

print(groups)
