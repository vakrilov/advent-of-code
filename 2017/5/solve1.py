f = open("./5/input.txt", "r")


instructions = list(map(int, f.readlines()))
current = 0
moves = 0
while current >= 0 and current < len(instructions):
    # print(current, instructions)
    tmp = instructions[current]
    instructions[current] += 1
    current += tmp
    moves += 1

print(moves)
