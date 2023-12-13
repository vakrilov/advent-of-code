import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

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
    if len(template) < len(prefix):
        print("THIS SHOULD NOT HAPPEN")
        exit()

    for i in range(len(prefix)):
        if template[i] != "?" and template[i] != prefix[i]:
            return False
    return True

def split_on_dot(template, nums, mid):
    left = template[:mid]
    right = template[mid + 1 :]
    res = 0
    for num_idx in range(len(nums) + 1):
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

        add_dot_start = 0 if num_idx == 0 else 1
        add_dot_end = 0 if num_idx == (len(nums) - 1) else 1

        str = "." * add_dot_start + "#" * num + "." * add_dot_end

        for i in range(num):
            str_start = mid - i - add_dot_start
            str_end = str_start + len(str)

            if str_start < 0 or str_end > len(template):
                continue

            check = template[str_start:str_end]

            if is_valid(check, str):
                left_template = template[:str_start]
                right_template = template[str_end:]

                left_res = solve_split(left_template, left_nums)
                right_res = (
                    solve_split(right_template, right_nums) if left_res > 0 else 0
                )

                result += left_res * right_res
    return result


def solve_split(template, nums):
    result = 0
    if len(nums) == 0:
        is_valid(template, "." * len(template))
        result = 1 if is_valid(template, "." * len(template)) else 0
    elif sum(nums) + len(nums) - 1 > len(template):
        result = 0
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

    return result

print("part2:", sum(solve_split(t, n) for t, n in rows))
