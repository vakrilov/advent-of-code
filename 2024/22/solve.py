# %%
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]
nums = [int(l) for l in lines]


def step(num):
    tmp = num * 64
    num = tmp ^ num
    num = num % 16777216

    tmp = num // 32
    num = tmp ^ num
    num = num % 16777216

    tmp = num * 2048
    num = tmp ^ num
    num = num % 16777216

    return num


def do_steps(num, steps):
    for i in range(steps):
        num = step(num)
    return num


print("part 1:", sum([do_steps(n, 2000) for n in nums]))

# %%
NUMS = 2000


def get_seq(num):
    secrets = [num]
    for i in range(NUMS):
        num = step(num)
        secrets.append(num)
    only_last = [x % 10 for x in secrets]
    return only_last


def get_diff(seq):
    diffs = []
    for i in range(1, len(seq)):
        diffs.append(seq[i] - seq[i - 1])
    return diffs


prices = [get_seq(n) for n in nums]
diffs = [get_diff(s) for s in prices]
# %%


def generate_sequences():
    for n1 in range(-9, 10):
        for n2 in range(-9, 10):
            for n3 in range(-9, 10):
                for n4 in range(-9, 10):
                    total = n1 + n2 + n3 + n4
                    if -9 <= total <= 9:
                        yield (n1, n2, n3, n4)


seq = list(generate_sequences())
seq.reverse()
# %%


def calc_profit_single(seq, diff, price):
    for i in range(4, NUMS):
        if (
            diff[i - 3] == seq[0]
            and diff[i - 2] == seq[1]
            and diff[i - 1] == seq[2]
            and diff[i] == seq[3]
        ):
            return price[i + 1]
    return 0


def calc_profit(seq):
    return sum(
        [calc_profit_single(seq, diffs[i], prices[i]) for i in range(len(prices))]
    )


# max_profit = 0
# for i, s in enumerate(seq):
#     print(i, len(seq), max_profit)
#     profit = calc_profit(s)
#     max_profit = max(max_profit, profit)

# print("part 2:", max_profit)

# %%


def generate_sequences2():
    # get only sequences that occur in the diffs
    results = {}
    for diff in diffs:
        for start in range(len(diff) - 4):
            seq = tuple(diff[start : start + 4])
            results[seq] = results.get(seq, 0) + 1

    sorted_keys_desc = sorted(results, key=results.get, reverse=True)

    # return only the top 100 sequences that occur in most diffs
    return sorted_keys_desc[0:100]


seq2 = generate_sequences2()

# %%
max_profit = 0
for i, s in enumerate(seq2):
    profit = calc_profit(s)
    max_profit = max(max_profit, profit)

print("part 2:", max_profit)

# %%
