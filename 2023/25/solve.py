# %%
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

nodes = set()
links = dict()
links_count = 0


def add_link(a, b):
    if a not in links:
        links[a] = set()
    links[a].add(b)

    if b not in links:
        links[b] = set()
    links[b].add(a)


for line in lines:
    first = line[0:3]
    nodes.add(first.strip())

    rest = line[5:].split(" ")

    links_count += len(rest)
    for r in rest:
        nodes.add(r)
        add_link(first, r)

# %%
def bfs(fr, to):
    visited = set()
    queue = [(fr, (fr,))]

    while len(queue) > 0:
        node, path = queue.pop(0)
        if path[-1] == to:
            return path

        if node in visited:
            continue

        visited.add(node)

        for n in links[node]:
            queue.append((n, path + (node,)))

    print("path not found")
    return len(visited)


# %%
nodes_list = list(nodes)
bridges_count = dict()

split = 40
for i in range(split-1):
    print(f"{i}/{split}")
    for n1 in nodes_list[i : len(nodes_list) : 40]:
        for n2 in nodes_list[i + 1 : len(nodes_list) : 40]:
            if n1 == n2:
                continue
            path = bfs(n1, n2)
            for i in range(len(path) - 1):
                a = path[i]
                b = path[i + 1]
                (a, b) = sorted([a, b])
                key = (a, b) 
                if key not in bridges_count:
                    bridges_count[key] = 0
                bridges_count[key] += 1


br_count_list = [(k, v) for k, v in bridges_count.items()]
br_count_list.sort(key=lambda x: x[1], reverse=True)

# %%
# remove top 3
def remove_link(a, b):
    links[a].remove(b)
    links[b].remove(a)

# remove_link('rtt', 'zcj')
# remove_link('gxv', 'tpn')
# remove_link('hxq', 'txl')
for bridge, num in br_count_list[0:3]:
    remove_link(*bridge)

# %%

group1 = bfs(br_count_list[0][0][0], br_count_list[0][0][1])
group2 = bfs(br_count_list[0][0][1], br_count_list[0][0][0])
print("answer:", group1 * group2)
