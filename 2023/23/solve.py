import os
import sys
sys.setrecursionlimit(1_000_000)

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

board = [l.removesuffix("\n") for l in f.readlines()]

def is_valid(row, col):
    return 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] != "#"

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

def next(r, c):
  
    current = board[r][c]

    if current == ">":
        return [(r, c + 1)]
    if current == "<":
        return [(r, c - 1)]
    if current == "^":
        return [(r - 1, c)]
    if current == "v":
        return [(r + 1, c)]

    if current == ".":
        possible = [(r, c + 1), (r, c - 1), (r - 1, c), (r + 1, c)]

        return [p for p in possible if is_valid(*p)]


start = (0, 1)
end = (len(board) - 1, len(board[0]) - 2)

def solve(current, dist, visited):
    if current == end:
        return dist

    visited.add(current)
    # p(board, visited)

    possible = [pos for pos in next(*current) if pos not in visited]

    if len(possible) == 0:
        return 0

    return max([solve(pos, dist + 1, visited.copy()) for pos in possible])

print(solve(start, 0, set()))
