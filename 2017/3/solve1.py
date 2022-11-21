import math
n = 325489

x = 1
while (2*x + 1)**2 < n:
    x += 1

leftover = n - (2*x+1)**2
leftover %= 2*x

answer = leftover if leftover > x else 2*x - leftover
print(answer)
