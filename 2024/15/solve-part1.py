# %%
import os

# f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]
L = lines.index("")

board = [[c for c in l] for l in lines[0:L]]
commands = [c for c in "".join(lines[L + 1 :])]

# %%

directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def p():
    for row in board:
        print("".join(row))
    print()


# %%

robot = [0, 0]
for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c] in "@":
            robot = [r, c]
            break


# %%


def move(pos, dir):
    to = [pos[0] + dir[0], pos[1] + dir[1]]
    what = board[pos[0]][pos[1]]
    to_what = board[to[0]][to[1]]

    if to_what == "#":
        return False, pos
    elif to_what == ".":
        board[to[0]][to[1]] = what
        board[pos[0]][pos[1]] = "."
        return True, to
    elif to_what == "O":
        can, _ = move(to, dir)
        if can:
            board[to[0]][to[1]] = what
            board[pos[0]][pos[1]] = "."
            return True, to
        else:
            return False, pos


# %%
for c in commands:
    moved, robot = move(robot, directions[c])
# p()

# %%
sum = 0
for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c] == "O":
            sum += 100 * r + c
print("part1:", sum)
# %%
