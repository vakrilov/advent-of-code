import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")


class Board:
    def __init__(self, board):
        self.board = board

    def get(self, r, c, dir):
        if dir == "N":
            return self.board[r][c]
        elif dir == "W":
            return self.board[LEN - c - 1][r]
        elif dir == "S":
            return self.board[LEN - r - 1][LEN - c - 1]
        elif dir == "E":
            return self.board[c][LEN - r - 1]

    def set(self, r, c, v, dir):
        if dir == "N":
            self.board[r][c] = v
        elif dir == "W":
            self.board[LEN - c - 1][r] = v
        elif dir == "S":
            self.board[LEN - r - 1][LEN - c - 1] = v
        elif dir == "E":
            self.board[c][LEN - r - 1] = v

    def eval(self):
        res = 0
        for i, row in enumerate(self.board):
            weight = len(self.board) - i
            res += sum([weight for c in row if c == "O"])
        return res

    def toStr(self):
        return "\n".join(["".join(r) for r in self.board])

    def p(self):
        print(self.toStr())
        print()


lines = [l.removesuffix("\n") for l in f.readlines()]
myBoard = Board([list(l) for l in lines])
LEN = len(lines)


def tilt(board, dir):
    for col in range(LEN):
        available_row = 0
        for row in range(LEN):
            ch = board.get(row, col, dir)

            if ch == "#":
                available_row = row + 1

            if ch == "O":
                if available_row != row:
                    board.set(available_row, col, "O", dir)
                    board.set(row, col, ".", dir)
                    available_row += 1
                else:
                    available_row = row + 1
    # print(dir)
    # board.p()


# cycles = 0
# while cycles < 50:
#     cycles += 1
#     tilt(myBoard, "N")
#     tilt(myBoard, "W")
#     tilt(myBoard, "S")
#     tilt(myBoard, "E")

#     print(cycles, myBoard.eval())
# exit()

states = []
cycles = 0
found = False
while cycles < 1000_000_000:
    tilt(myBoard, "N")
    tilt(myBoard, "W")
    tilt(myBoard, "S")
    tilt(myBoard, "E")
    cycles += 1

    if not found:
        str = myBoard.toStr()

        if str in states:
            idx = states.index(str)
            d = cycles - idx - 1
            print("Found cycle with length", d, "found at idx", idx)
            left = 1000_000_000 - cycles
            cycles += (left // d) * d
            found = True

        states.append(str)

print(myBoard.eval())
