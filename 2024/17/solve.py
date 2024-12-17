# %%
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

A = int(lines[0][len("Register A: ") :])
B = int(lines[1][len("Register B: ") :])
C = int(lines[2][len("Register C: ") :])
program = [int(x) for x in lines[4][len("Program: ") :].split(",")]
output = []

pointer = 0

print(A, B, C)
print(program)


def combo(code):
    if code <= 3:
        return code
    if code == 4:
        return A
    if code == 5:
        return B
    if code == 6:
        return C
    assert False


def adv(op):
    global A
    A = A // 2 ** combo(op)


def bxl(op):
    global B
    B = B ^ op


def bst(op):
    global B
    B = combo(op) % 8


def jnz(op):
    global pointer
    if A != 0:
        pointer = op - 2


def bxc(op):
    global B
    B = B ^ C


def out(op):
    output.append(combo(op) % 8)


def bdv(op):
    global B
    B = A // 2 ** combo(op)


def cdv(op):
    global C
    C = A // 2 ** combo(op)


instructions = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}


def execute():
    if pointer >= len(program):
        print("HALT")
        return False

    assert pointer < len(program) - 1

    opcode = program[pointer]
    operand = program[pointer + 1]

    instructions[opcode](operand)
    return True


while execute():
    pointer += 2

print("part1:", str(output).replace("[", "").replace("]", "").replace(", ", ","))


# %%
