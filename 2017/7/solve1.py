f = open("./7/input.txt", "r")


nodes: list[str] = []
childNodes: list[str] = []

for line in f.readlines():
    str = line.split()
    name = str[0]
    weight = int(str[1][1:-1])
    children = map(lambda s: s.removesuffix(","), str[3:])

    nodes.append(name)
    childNodes.extend(children)

# print(nodes)
# print(childNodes)

matches = [x for x in nodes if x not in childNodes]
print(matches)
