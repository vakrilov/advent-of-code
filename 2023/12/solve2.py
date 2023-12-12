import os

f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

rows = []
factor = 5

for line in lines:
    [template, nums_part] = line.split()
    numbers = [int(x) for x in nums_part.split(",")] * factor

    template = (template + "?") * factor
    template = template[:-1]

    rows.append((template, numbers))


def is_valid(template, prefix):
    for i in range(len(prefix)):
        if template[i] != "?" and template[i] != prefix[i]:
            return False
    return True


def gen(template, nums):
    if template == "":
        yield ""
        return

    if len(nums) == 0:
        rest = "." * len(template)
        if is_valid(template, rest):
            yield rest
        return

    free = len(template) - sum(nums) - len(nums) + 1
    for i in range(free + 1):
        prefix = "." * i + nums[0] * "#" + "."
        if len(prefix) > len(template):
            prefix = prefix[: len(template)]
        if is_valid(template, prefix):
            for suffix in gen(template[len(prefix) :], nums[1:]):
                yield prefix + suffix


def split_on_dot(template, nums, mid):
    left = template[:mid]
    right = template[mid + 1 :]
    res = 0
    for num_idx in range(len(nums)):
        left_nums = nums[:num_idx]
        right_nums = nums[num_idx:]

        left_res = solve_split(left, left_nums)
        right_res = solve_split(right, right_nums) if left_res > 0 else 0

        res += left_res * right_res
    return res


def split_on_hash(template, nums, mid):
    result = 0
    for num_idx in range(len(nums)):
        num = nums[num_idx]
        left_nums = nums[:num_idx]
        right_nums = nums[num_idx + 1 :]

        str = "." + "#" * num + "."
        for i in range(num):
            check = template[mid - i - 2 : mid + num - i]
            if is_valid(check, str):
                left_template = template[: mid - i - 1]
                right_template = template[mid + num - i + 1 :]

                left_res = solve_split(left_template, left_nums)
                right_res = (
                    solve_split(right_template, right_nums) if left_res > 0 else 0
                )
                # if left_res * right_res > 0:
                #     print("split_on_hash", template, nums)
                #     print("  check:", check, str)
                #     print("  left:", left_template, left_nums)
                #     print("  right:", right_template, right_nums)

                result += left_res * right_res
    return result


def solve_split(template, nums):
    result = 0
    if len(template) < 16:
        result = sum(1 for _ in gen(template, nums))

    elif len(nums) == 0:
        is_valid(template, "." * len(template))
        result = 1 if is_valid(template, "." * len(template)) else 0

    else:
        mid = len(template) // 2
        mid_char = template[mid]

        if mid_char == ".":
            result = split_on_dot(template, nums, mid)
        elif mid_char == "#":
            result = split_on_hash(template, nums, mid)
        else:
            dot = split_on_dot(template, nums, mid)
            hash = split_on_hash(template, nums, mid)
            result = dot + hash
    # if(result > 0):
    #     print("solve_split", template, nums)
    #     print("  result:", result)
    return result


# (t, n) = rows[4]
# print(t)
# print(solve_split(t, n))
# print(sum(1 for _ in gen(t, n)))

for t, n in rows:
# for t, n in rows[0:1]:
    print()
    print(t, n)
    print("solve:", solve_split(t, n))
    print("  gen:", sum(1 for _ in gen(t, n)))

    # for candidate in gen(t, n):
    #     print(candidate)

# t = "???.###????.###????"
# n = [1, 1, 3, 1, 1, 3]
# print("solve:", solve_split(t, n))
# print("  gen:", sum(1 for _ in gen(t, n)))
# for candidate in gen(t, n):
#     print(t)
#     print(candidate)


res = 0
for t, n in rows[1:2]:
    # print(t, n)
    res += solve_split(t, n)
    # r = 0
    # for candidate in gen(t, n):
    #     r += 1
    # print(r)
    # res += r
print("part2", res)
