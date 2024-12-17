def program(initial_a):
    A = initial_a
    B = 0
    C = 0

    output = []
    while A > 0:
        B = A % 8  # 2,4
        B = B ^ 1  # 1,1
        C = A // 2**B  # 7,5
        B = B ^ 5  # 1,5
        B = B ^ C  # 4,3
        output.append(B % 8)  # 5,5
        A = A // 8  # 0,3

    return output


# %%
target = [2, 4, 1, 1, 7, 5, 1, 5, 4, 3, 5, 5, 0, 3, 3, 0]

A = 0
for pos in range(16):
    current_target = target[-pos - 1 :]
    print("Target: ", current_target)

    possibles = []
    for i in range(0, 8):
        newA = A * 8 + i
        out = program(newA)
        print("newA", newA, "Out: ", out)
        if out == current_target:
            print("Found A: ", i)
            possibles.append(newA)
    print("Possibles: ", possibles)
    A = possibles[0]
    print("A is now: ", A)


print("A: ", A)
print(program(A))

# %%


def find_A(target: list, A: int):
    if len(target) == 0:
        return [A]

    tail = target[1:]
    tailAs = find_A(tail, A)
    answers = []
    for tailA in tailAs:
        for i in range(0, 8):
            newA = tailA * 8 + i
            out = program(newA)
            if out == target:
                answers.append(newA)
    return answers


answers = find_A(target, 0)
print("part 2:", answers[0])

# %%
