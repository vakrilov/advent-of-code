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
        B = A % 8       # 2,4
        B = B ^ 1       # 1,1
        C = A // 2**B   # 7,5
        B = B ^ 5       # 1,5    
        B = B ^ C       # 4,3
        output.append(B % 8)    # 5,5
        A = A // 8      # 0,3

    print(str(output).replace("[", "").replace("]", "").replace(", ", ","))


for i in range(0, 32):
    program(i)

# %%
