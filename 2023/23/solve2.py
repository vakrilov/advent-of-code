import os
import sys

sys.setrecursionlimit(1_000_000)

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

board = [l.removesuffix("\n") for l in f.readlines()]


def p(board, visited):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if (r, c) in visited:
                print("o", end="")
            else:
                print(board[r][c], end="")
        print("")
    print("")
    print("")


def is_valid(row, col):
    return 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] != "#"


def next(r, c):
    current = board[r][c]

    if (
        current == "."
        or current == ">"
        or current == "<"
        or current == "^"
        or current == "v"
    ):
        possible = [(r, c + 1), (r, c - 1), (r - 1, c), (r + 1, c)]

        return [p for p in possible if is_valid(*p)]


start = (0, 1)
end = (len(board) - 1, len(board[0]) - 2)


nodes = []
dists = dict()

for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c] != "#":
            neighbours = next(r, c)
            if len(neighbours) > 2:
                nodes.append((r, c))
nodes.append(start)
nodes.append(end)

def track(fr, to, dist):
    if to in nodes:
        return (to, dist)
    else:
        neighbours = [n for n in next(*to) if n != fr]
        assert len(neighbours) == 1
        return track(to, neighbours[0], dist + 1)


for node in nodes:
    dists[node] = []
    for neighbor in next(*node):
        next_node, dist = track(node, neighbor, 1)
        dists[node].append((next_node, dist))
        # print("from", node, "to", next_node, "is", dist)


def get_max_route(node, dist, visited):
    if node == end:
        return dist

    results = [0]
    for next_node, next_dist in dists[node]:
        if next_node not in visited:
            results.append(
                get_max_route(next_node, dist + next_dist, visited + [next_node])
            )

    return max(results)

print("part2:", get_max_route(start, 0, []))
