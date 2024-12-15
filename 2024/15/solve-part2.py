# %%
import os

# f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")
# f = open(os.path.dirname(__file__) + "/sample2.txt", "r", encoding="utf-8")
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]
L = lines.index("")

replace = {
    "#": "##",
    "O": "[]",
    ".": "..",
    "@": "@.",
}

extended_lines = ["".join([replace[c] for c in l]) for l in lines[0:L]]
board = [[c for c in l] for l in extended_lines]
print(board)

commands = [c for c in "".join(lines[L + 1 :])]
len(commands)


directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def p():
    for row in board:
        print("".join(row))
    print()


p()

robot = [0, 0]
for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c] in "@":
            robot = [r, c]
            break
print(robot)


def can_move(pos, dir_str):
    # print("can_move", pos, dir_str)
    dir = directions[dir_str]

    to = (pos[0] + dir[0], pos[1] + dir[1])
    to_object = board[to[0]][to[1]]

    if to_object == "#":
        return False
    elif to_object == ".":
        return True
    elif to_object == "[" or to_object == "]":
        if dir_str == "<" or dir_str == ">":
            return can_move(to, dir_str)
        elif dir_str == "^" or dir_str == "v":
            if to_object == "[":
                return can_move(to, dir_str) and can_move((to[0], to[1] + 1), dir_str)
            if to_object == "]":
                return can_move(to, dir_str) and can_move((to[0], to[1] - 1), dir_str)
        else:
            assert False


def move(pos, dir_str):
    dir = directions[dir_str]

    to = [pos[0] + dir[0], pos[1] + dir[1]]
    current_obj = board[pos[0]][pos[1]]
    to_obj = board[to[0]][to[1]]

    assert to_obj != "#"

    if to_obj == "[" or to_obj == "]":
        if dir_str == "<" or dir_str == ">":
            move(to, dir_str)
        elif dir_str == "^" or dir_str == "v":
            if to_obj == "[":
                move(to, dir_str)
                move((to[0], to[1] + 1), dir_str)
            elif to_obj == "]":
                move(to, dir_str)
                move((to[0], to[1] - 1), dir_str)
    else:
        assert to_obj == "."

    board[to[0]][to[1]] = current_obj
    board[pos[0]][pos[1]] = "."

    return to


# %%


for c in commands:
    can = can_move(robot, c)
    if can:
        robot = move(robot, c)
    # p()

# %%
sum = 0
for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c] == "[":
            sum += 100 * r + c
print("part 2:", sum)
# %%
