import os
f = open(os.path.dirname(__file__) + "/input.txt", "r")

L = 256
loops = [int(x) for x in f.read().split(",")]
arr = [*range(L)]

current = 0
skip = 0
print(arr)

for loop in loops:
    for i in range(int(loop/2)):
        a, b = (current + i) % L, (current + loop - i - 1) % L
        arr[a], arr[b] = arr[b], arr[a]
    current += loop + skip
    current %= L
    skip += 1
    print(arr, current, skip)

print(arr[0] * arr[1])
