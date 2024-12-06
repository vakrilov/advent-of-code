# %%
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

linesRaw = [l.removesuffix("\n") for l in f.readlines()]

L = len(linesRaw)

board = [list(l) for l in linesRaw]

# %%
directions = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0),
}

start_pos = (0, 0)
for y, line in enumerate(board):
    if "^" in line:
        start_pos = (line.index("^"), y)
        break

# %%


def p(trace):
    for y, l in enumerate(board):
        for x, char in enumerate(l):
            tr = trace.get((x, y))
            if tr != None:
                if (0 in tr or 2 in tr) and (1 in tr or 3 in tr):
                    print("+", end="")
                elif 0 in tr or 2 in tr:
                    print("|", end="")
                else:
                    print("-", end="")
            else:
                print(char, end="")
        print()
    print()
    print()


# %%


def traverse(start_position):
    trace = dict()
    pos = start_position
    dir = 0

    trace[pos] = [dir]

    while True:
        dx, dy = directions[dir]
        nx, ny = pos[0] + dx, pos[1] + dy

        if nx < 0 or nx >= L or ny < 0 or ny >= L:
            return False, trace

        new_pos = (nx, ny)

        if board[ny][nx] == "#":
            dir = (dir + 1) % 4
        elif dir in trace.get(new_pos, []):
            return True, trace
        else:
            pos = new_pos
            trace[pos] = trace.get(pos, []) + [dir]


isLoop, original_trace = traverse(start_pos)
print("part1:", len(original_trace))

# %%
obstacle_positions = [k for k in original_trace.keys() if k != start_pos]

count = 0
for obstacle_pos in obstacle_positions:
    board[obstacle_pos[1]][obstacle_pos[0]] = "#"

    isLoop, trace = traverse(start_pos)
    if isLoop:
        count += 1

    board[obstacle_pos[1]][obstacle_pos[0]] = "."

print("part2:", count)
# %%
