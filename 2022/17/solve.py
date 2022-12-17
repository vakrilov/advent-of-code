import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")
instruction_pattern = f.read()
L = 20_000
chamber = [["."] * 7 for _ in range(L+10)]
height = 0


instruction = 0


def read_directions():
    global instruction
    while True:
        if instruction_pattern[instruction % len(instruction_pattern)] == "<":
            yield (-1, 0)
        elif instruction_pattern[instruction % len(instruction_pattern)] == ">":
            yield (1, 0)
        else:
            print("PANIC!!!")
        instruction += 1


def valid_point(x, y):
    if x < 0 or x >= 7 or y < 0:
        return False

    return chamber[y][x] == "."


def valid(shape):
    for s in shape:
        if not valid_point(*s):
            return False
    return True


def spawn_shape():
    while True:
        yield [[2, 0], [3, 0], [4, 0], [5, 0]]
        yield [[3, 0], [2, 1], [3, 1], [4, 1], [3, 2]]
        yield [[2, 0], [3, 0], [4, 0], [4, 1], [4, 2]]
        yield [[2, 0], [2, 1], [2, 2], [2, 3]]
        yield [[2, 0], [3, 0], [2, 1], [3, 1]]


def move(shape, d):
    return list([sh[0] + d[0], sh[1] + d[1]] for sh in shape)


def p(shape):
    for y in range(height, height-20, -1):
        for x in range(7):
            if [x, y] in shape:
                print("@", end="")
            else:
                print(chamber[y][x], end="")
        print()
    print("-------")
    print("height:", height)


turn = 0
shapes = spawn_shape()
directions = read_directions()

heights = []


while height < L:
    turn += 1

    current_shape = move(next(shapes), [0, height+3])

    landed = False
    while not landed:
        # blow
        dir = next(directions)
        moved_shape = move(current_shape, dir)
        if valid(moved_shape):
            current_shape = moved_shape

        # move down
        moved_shape = move(current_shape, [0, -1])
        if valid(moved_shape):
            current_shape = moved_shape
        else:
            landed = True
            for x, y in current_shape:
                chamber[y][x] = "#"
            prev_h = height
            height = max(height, max(s[1] for s in current_shape)+1)
            heights.append(height - prev_h)

print("part 1:", sum(heights[0: 2022]))


MAX_SKIP = 500
MAX_PATTERN = 2000


def find_pattern():
    for skip_first in range(MAX_SKIP):
        r = heights[skip_first:]
        for i in range(20, MAX_PATTERN, 5):
            if r[0:i] == r[i:2*i]:
                return skip_first, i


skip, pattern = find_pattern()
skip_height = sum(heights[:skip])
pattern_height = sum(heights[skip: skip+pattern])


def calc_height_at(goal):
    times = (goal - skip) // pattern
    leftover = (goal - skip) % pattern
    leftover_height = sum(heights[skip: skip+leftover])
    return skip_height + pattern_height*times + leftover_height


print("Part 2:", calc_height_at(1000000000000))
