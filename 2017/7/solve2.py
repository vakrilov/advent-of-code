f = open("./7/input.txt", "r")


nodes = dict()
childNodes: list[str] = []

for line in f.readlines():
    str = line.split()
    name = str[0]
    weight = int(str[1][1:-1])
    children = list(map(lambda s: s.removesuffix(","), str[3:]))

    nodes[name] = {
        "weight": weight,
        "children": children,
        "towerWeight": 0
    }
    childNodes.extend(children)

# print(nodes)
# print(childNodes)

parent = [x for x in nodes.keys() if x not in childNodes][0]
print(parent)


def calc(name: str):
    node = nodes[name]

    childrenWeight = 0
    for child in node["children"]:
        childrenWeight += calc(child)

    weights = [nodes[n]["towerWeight"] for n in node["children"]]
    if len(set(weights)) == 2:
        print(name, weights)
        print(*[(n, nodes[n]) for n in node["children"]], sep="\n")
        exit()

    node["towerWeight"] = node["weight"] + childrenWeight
    return node["towerWeight"]


calc(parent)

# print(nodes)
