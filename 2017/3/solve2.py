from itertools import product
target = 325489
n = 101

arr = [[0 for i in range(n)] for j in range(n)]
print(arr)


def next(x: int, y: int):
    left = arr[y][x-1] == 0
    right = arr[y][x+1] == 0
    up = arr[y-1][x] == 0
    down = arr[y+1][x] == 0

    if left and right and up and down:
        return x+1, y
    elif not up and right:
        return x+1, y
    elif not left and up:
        return x, y-1
    elif not down and left:
        return x-1, y
    elif not right and down:
        return x, y+1
    else:
        print("kuuur")


x, y = int(n/2), int(n/2)
arr[y][x] = 1
for i in range(2, 100):
    x, y = next(x, y)
    sum = 0
    for x1, y1 in product(range(x-1, x+2), range(y-1, y+2)):
        sum += arr[y1][x1]
    if sum >= target:
        print(sum)
        exit(0)
    arr[y][x] = sum

print(arr)
