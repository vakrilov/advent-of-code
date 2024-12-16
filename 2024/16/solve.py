# %%
import os
from queue import PriorityQueue

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

# print(len(lines))
# print(len(lines[0]))

L = len(lines)
board = [[c for c in l.replace("S", ".").replace("E", ".")] for l in lines]
# print(board)
start = (L - 2, 1)
end = (1, L - 2)

dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

# %%


def step(pos):
    row, col, dir, score, track = pos

    next_pos = []

    forward_pos = (row + dirs[dir][0], col + dirs[dir][1])

    if board[forward_pos[0]][forward_pos[1]] == ".":
        next_pos.append(
            (forward_pos[0], forward_pos[1], dir, score + 1, track + (forward_pos,))
        )

    right_dir = (dir + 1) % 4
    right_pos = (row + dirs[right_dir][0], col + dirs[right_dir][1])

    if board[right_pos[0]][right_pos[1]] == ".":
        next_pos.append(
            (right_pos[0], right_pos[1], right_dir, score + 1001, track + (right_pos,))
        )

    left_dir = (dir - 1) % 4
    left_pos = (row + dirs[left_dir][0], col + dirs[left_dir][1])
    if board[left_pos[0]][left_pos[1]] == ".":
        next_pos.append(
            (left_pos[0], left_pos[1], left_dir, score + 1001, track + (left_pos,))
        )

    return next_pos


queue = PriorityQueue()

queue.put(
    (
        0,
        (
            start[0],
            start[1],
            0,
            0,
            (start,),
        ),
    )
)


visited = {}
found_score = 0
found_tracks = []
while not queue.empty():
    score, pos = queue.get()

    mark = (pos[0], pos[1], pos[2])
    if mark in visited and visited[mark] < score:
        continue
    visited[mark] = score

    if pos[0] == end[0] and pos[1] == end[1]:
        found_score = pos[3]
        found_tracks.append(pos[4])
        break

    next_positions = step(pos)
    for next in next_positions:
        queue.put((next[3], next))

print("part1:", found_score)

while not queue.empty():
    score, pos = queue.get()
    if score == found_score:
        if pos[0] == end[0] and pos[1] == end[1]:
            found_tracks.append(pos[4])
    else:
        break

track_tiles = set()
for track in found_tracks:
    for t in track:
        track_tiles.add(t)

print("part2:", len(track_tiles))

# %%
