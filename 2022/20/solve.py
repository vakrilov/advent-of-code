import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = list(f.readlines())
N = len(lines)


def find(predicate):
    for current_index, item in enumerate(mixed_nums):
        if predicate(item):
            return current_index


def move(original_index):
    global mixed_nums

    current_index = find(lambda pair: pair[0] == original_index)
    node = mixed_nums[current_index]

    value = node[1]
    if value == 0:
        return

    new_index = (current_index + value) % (N - 1)

    # if element is first, actually put it at the end
    if new_index == 0:
        new_index = N - 1

    mixed_nums.pop(current_index)
    mixed_nums.insert(new_index, node)


def calc_answer():
    zero_idx = find(lambda pair: pair[1] == 0)
    return sum(mixed_nums[(zero_idx + offset) % N][1]
               for offset in [1000, 2000, 3000])


mixed_nums = [(i, int(x)) for i, x in enumerate(lines)]
for i in range(N):
    move(i)

zero_idx = find(lambda pair: pair[1] == 0)
print("Part 1:", calc_answer())

# re-init input for part 2
mixed_nums = [(i, int(x) * 811589153) for i, x in enumerate(lines)]
for _ in range(10):
    for i in range(N):
        move(i)
print("Part 2:", calc_answer())
