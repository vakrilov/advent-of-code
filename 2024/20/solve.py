# %%
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

print(len(lines))
print(len(lines[0]))

L = len(lines)
board = [[c for c in l] for l in lines]

start = None
end = None
for row in range(L):
    for col in range(L):
        if board[row][col] == "S":
            start = (row, col)
            board[row][col] = "."
        if board[row][col] == "E":
            end = (row, col)
            board[row][col] = "."
print(start, end)

# %%


def bfs(board, start, end, cheat_start, cheat_end):
    queue = [(start, [(start)])]
    visited = set()
    visited.add(start)
    while queue:
        (row, col), path = queue.pop(0)
        if (row, col) == end:
            return path + [end]

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if (
                0 <= new_row < L
                and 0 <= new_col < L
                and (new_row, new_col) not in visited
                and board[new_row][new_col] == "."
            ):
                queue.append(((new_row, new_col), path + [(new_row, new_col)]))
                visited.add((new_row, new_col))

        if (row, col) == cheat_start:
            cheat_node = (cheat_end[0] + 1000, cheat_end[1] + 1000)
            queue.append((cheat_end, path + [cheat_node]))
            visited.add(cheat_end)
    return False


def print_path(path):
    for row in range(L):
        for col in range(L):
            if (row, col) in path:
                print("0", end="")
            elif (row + 1000, col + 1000) in path:
                print("!", end="")
            else:
                print(board[row][col], end="")

        print()


base_path = bfs(board, start, end, (-1, -1), (-1, -1))
base_len = len(base_path)
print(base_len)
# print_path(base_path)

# %%
saves = {}
for i, tile in enumerate(base_path):
    row, col = tile
    cheat_moves = [(2, 0), (-2, 0), (0, 2), (0, -2)]
    for dr, dc in cheat_moves:
        new_row, new_col = row + dr, col + dc
        new = (new_row, new_col)
        if new in base_path:
            start_cheat_index = base_path.index(tile)
            end_cheat_index = base_path.index(new)
            save = end_cheat_index - start_cheat_index - 2

            if save > 0:
                saves[save] = saves.get(save, 0) + 1

for save in sorted(saves.keys()):
    print(save, saves[save])

# %%
result = 0
for save in sorted(saves.keys()):
    if save >= 100:
        result += saves[save]
print("part1:", result)
# %%
