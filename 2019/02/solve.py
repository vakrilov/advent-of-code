import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

input = [int(num) for num in f.read().split(",")]

ops = { 
    1: lambda x,y: x + y, 
    2: lambda x,y: x * y
}

def run(nums, noun, verb):
    nums[1] = noun
    nums[2] = verb
    for i in range(0, len(nums), 4):
        if nums[i] == 99:
            break

        op = ops[nums[i]]
        arg1 = nums[nums[i + 1]]
        arg2 = nums[nums[i + 2]]
        out = nums[i + 3]

        nums[out] = op(arg1, arg2)

    return nums[0]

print(f"Part 1: {str(run(input.copy(), 12, 2))}")

for noun in range(100):
    for verb in range(100):
        if run(input.copy(),noun, verb) == 19690720:
            print(f"Part 2: {noun}{verb}")
            break   
