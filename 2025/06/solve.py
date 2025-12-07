# %%
import os

# f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

op_map = {
    "+": ((lambda x, y: x + y), 0),
    "*": ((lambda x, y: x * y), 1),
}

# %%
nums = [[int(x) for x in line.split(" ") if x != ""] for line in lines[:-1]]
ops = [line for line in lines[-1].split(" ") if line != ""]
l = len(nums[0])


part1 = 0
for i in range(0, l):
    curr_op, res = op_map[ops[i]]
    for num in nums:
        res = curr_op(res, num[i])

    part1 += res

print("part1:", part1)
# %%


def trans(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


nums = lines[:-1]

transposed_nums = ["".join(x).strip() for x in trans(nums)]
print(transposed_nums)
ops_line = lines[-1]
print(ops_line)

idx = 0
part2 = 0
while idx < len(ops_line):
    curr_op, res = op_map[ops_line[idx]]
    while idx < len(ops_line) and not transposed_nums[idx] == "":
        res = curr_op(res, int(transposed_nums[idx]))
        idx += 1
    part2 += res
    idx += 1

print("part2:", part2)

# %%
