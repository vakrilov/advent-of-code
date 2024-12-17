# %%

# Register A: 38610541
# Register B: 0
# Register C: 0

# Program: 2,4, 1,1, 7,5, 1,5, 4,3, 5,5,  0,3,  3,0


def program(initalA):
    A = initalA
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

    # print(str(output).replace("[", "").replace("]", "").replace(", ", ","))
    return output


for i in range(0, 8):
    print("A:", i, "out:", program(i))


# %%
target = [2, 4, 1, 1, 7, 5, 1, 5, 4, 3, 5, 5, 0, 3, 3, 0]
# target.reverse()

A = 0
for pos in range(16):
    current_target = target[-pos-1:]
    print("Target: ", current_target)

    possibles =[]
    for i in range(0, 8):
        newA = A * 8 + i
        out = program(newA)
        print("newA", newA, "Out: ", out)
        if out == current_target:
            print("Found A: ", i)
            # A = newA
            possibles.append(newA)
    print("Possibles: ", possibles)
    A = possibles[0]
    print("A is now: ", A)
        

print("A: ", A)
print(program(A))

# %%
# for i in range(20534862392785*8, 20534862392785


# %%
bin(4)
# %%
