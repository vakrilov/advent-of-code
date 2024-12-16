# %%
import os
from queue import PriorityQueue

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

print(len(lines))
print(len(lines[0]))

L = len(lines)
board = [[c for c in l.replace("S", ".").replace("E", ".")] for l in lines]
print(board)
start = (L - 2, 1)
end = (1, L - 2)

dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

# %%

visited = set()


def step(pos):
    row, col, dir, score = pos

    next_pos = []

    forward = (row + dirs[dir][0], col + dirs[dir][1])

    if board[forward[0]][forward[1]] == ".":
        next_pos.append((forward[0], forward[1], dir, score + 1))

    right_dir = (dir + 1) % 4
    right_pos = (row + dirs[right_dir][0], col + dirs[right_dir][1])

    if board[right_pos[0]][right_pos[1]] == ".":
        next_pos.append((right_pos[0], right_pos[1], right_dir, score + 1001))

    left_dir = (dir - 1) % 4
    left_pos = (row + dirs[left_dir][0], col + dirs[left_dir][1])
    if board[left_pos[0]][left_pos[1]] == ".":
        next_pos.append((left_pos[0], left_pos[1], left_dir, score + 1001))

    return next_pos


queue = PriorityQueue()

queue.put((0, (start[0], start[1], 0, 0)))

while not queue.empty():
    _, pos = queue.get()

    mark = (pos[0], pos[1], pos[2])
    if mark in visited:
        continue

    visited.add(mark)

    if pos[0] == end[0] and pos[1] == end[1]:
        print(pos[3])
        break

    next_positions = step(pos)
    for next in next_positions:
        queue.put((next[3], next))

# %%
