# %%
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")
L = 71
TAKE = 1024

# f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")
# L = 7
# TAKE = 12

lines = [l.removesuffix("\n") for l in f.readlines()]

print(len(lines))
obstacles = []
for l in lines:
    p = l.split(",")
    obstacles.append((int(p[0]), int(p[1])))

part1_obstacles = obstacles[0:TAKE]
board = [["." for _ in range(L)] for _ in range(L)]
for x, y in part1_obstacles:
    board[y][x] = "#"

# board = [[int(c) for c in l] for l in lines]

# %%
start = (0, 0)
end = (L - 1, L - 1)


def bfs(board, start, end):
    queue = [(start, 0)]
    visited = set()
    visited.add(start)
    while queue:
        pos, length = queue.pop(0)
        x, y = pos
        if (x, y) == end:
            return True, length
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= L or ny < 0 or ny >= L:
                continue
            if board[ny][nx] == "#" or (nx, ny) in visited:
                continue
            visited.add((nx, ny))
            queue.append(((nx, ny), length + 1))
    return False, 0


_, result = bfs(board, start, end)

print("part1:", result)

# %%
for x, y in obstacles[TAKE:]:
    board[y][x] = "#"
    is_path, _ = bfs(board, start, end)

    if not is_path:
        print(f"part2: {x},{y}")
        break

# %%
