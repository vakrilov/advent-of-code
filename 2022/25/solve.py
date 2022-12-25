import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

to_dec_map = {
    "=": -2,
    "-": -1,
    "0": 0,
    "1": 1,
    "2": 2
}

to_five_map = {
    #  (digit, carry)
    0: ("0", 0),
    1: ("1", 0),
    2: ("2", 0),
    3: ("=", 1),
    4: ("-", 1),
    5: ("0", 1),
}


def to_dec(str_num):
    s = 0
    for ch in str_num:
        s *= 5
        s += to_dec_map[ch]
    return s


def to_five(num):
    carry = 0
    res = []

    while num != 0 or carry != 0:
        digit, carry = to_five_map[carry + num % 5]
        num //= 5
        res.append(digit)

    return "".join(reversed(res))


total = sum(map(to_dec, lines))
print(to_five(total))
