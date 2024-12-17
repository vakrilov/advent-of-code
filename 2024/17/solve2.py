# %%

# Register A: 38610541
# Register B: 0
# Register C: 0

# Program: 2,4,1,1,7,5,1,5,4,3,5,5,0,3,3,0

A = 38610541
B = 0
C = 0

while A > 0:
    B = A % 8
    B = B ^ 1
    C = A % 8
    B = B ^ 5
    B = B ^ C
    print(B)
    A = A // 8

# %%
