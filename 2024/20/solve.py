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


def bfs(board, start, end):
    queue = [(start, [(start)])]
    visited = set()
    visited.add(start)
    while queue:
        (row, col), path = queue.pop(0)
        if (row, col) == end:
            return path

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
    return False


def print_path(path):
    for row in range(L):
        for col in range(L):
            if (row, col) in path:
                print("0", end="")
            else:
                print(board[row][col], end="")
        print()


base_path = bfs(board, start, end)
base_len = len(base_path)
# print_path(base_path)
print("Base path len", base_len)

cheat_moves = [(2, 0, 2), (-2, 0, 2), (0, 2, 2), (0, -2, 2)]
index_map = {}
for i, tile in enumerate(base_path):
    index_map[tile] = i


def solve_cheat(cheat_moves):
    saves = {}
    for start_cheat_index, start_cheat in enumerate(base_path):
        # print("cheats on move", start_cheat_index)
        row, col = start_cheat
        for dr, dc, cheat_len in cheat_moves:
            new_row, new_col = row + dr, col + dc
            end_cheat = (new_row, new_col)

            if end_cheat in index_map:
                end_cheat_index = index_map[end_cheat]
                save = end_cheat_index - start_cheat_index - cheat_len

                if save > 0:
                    saves[save] = saves.get(save, 0) + 1
    return saves


saves = solve_cheat(cheat_moves)


def count_saves(saves, above):
    res = 0
    for save in sorted(saves.keys()):
        if save >= above:
            res += saves[save]
            # print(saves[save], "saves for", save, "pico seconds")
    return res


count_saves(saves, 0)

print("part1:", count_saves(saves, 100))
# %%

cheat_moves2 = set()
RANGE = 20
for total_len in range(1, RANGE + 1):
    for x_len in range(0, total_len + 1):
        y_len = total_len - x_len
        cheat_moves2.add((x_len, y_len, total_len))
        cheat_moves2.add((-x_len, y_len, total_len))
        cheat_moves2.add((x_len, -y_len, total_len))
        cheat_moves2.add((-x_len, -y_len, total_len))

# %%
saves2 = solve_cheat(set(cheat_moves2))
print("part2:", count_saves(saves2, 100))
# for save in sorted(saves2.keys()):
#     print(save, saves2[save])

# %%
