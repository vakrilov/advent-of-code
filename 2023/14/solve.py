import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")


lines = [l.removesuffix("\n") for l in f.readlines()]
board = [list(l) for l in lines]


def eval(board):
    res = 0
    for i, row in enumerate(board):
        weight = len(board) - i
        res += sum([weight for c in row if c == "O"])
    return res


def tilt_north(board):
    for col in range(len(board[0])):
        available_row = 0
        for row in range(len(board)):
            ch = board[row][col]

            if ch == "#":
                available_row = row + 1

            if ch == "O":
                if  available_row != row:
                    board[available_row][col] = "O"
                    board[row][col] = "."
                    available_row += 1
                else:
                    available_row = row + 1
            

print("\n".join(["".join(r) for r in board]))
print()
tilt_north(board)
print("\n".join(["".join(r) for r in board]))
print(eval(board))
