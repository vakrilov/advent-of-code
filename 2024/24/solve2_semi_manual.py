# %%
import os
from itertools import combinations

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

values = {}
gates = []
names = set()


def parse_value(l):
    name, val = l.split(": ")
    values[name] = int(val)
    names.add(name)


renames = {}


def parse_gate(l):
    # x00 AND y00 -> z00
    exp, out = l.split(" -> ")
    arg1, op, arg2 = exp.split(" ")
    if arg2.startswith("x"):
        arg1, arg2 = arg2, arg1

    # if arg1.startswith("x") and arg2.startswith("y"):
    #     if op == "AND":
    #         renames[out] = arg1 + "&" + arg2
    #     elif op == "OR":
    #         renames[out] = arg1 + "|" + arg2
    #     elif op == "XOR":
    #         renames[out] = arg1 + "^" + arg2

    gate = {"arg1": arg1, "op": op, "arg2": arg2, "out": out}
    gates.append(gate)

    names.add(arg1)
    names.add(arg2)
    names.add(out)


empty_line_idx = lines.index("")

for l in lines[:empty_line_idx]:
    parse_value(l)

for l in lines[empty_line_idx + 1 :]:
    parse_gate(l)


def p(gate):
    return f"{gate['arg1']} {gate['op']} {gate['arg2']} -> {gate['out']}"


def str_gate(gate):
    return f"{gate['arg1']} {gate['op']} {gate['arg2']} -> {gate['out']}"


# %%

levels = []


def get_level_gates(n, prev_carry):

    lvl_str = f"{n:02}"
    x_arg = "x" + lvl_str
    y_arg = "y" + lvl_str
    out_arg = "z" + lvl_str

    args = {x_arg, y_arg, prev_carry}
    res = set()

    carry_next = ""

    def check():
        carry = ""
        for g in gates:
            arg1, arg2, out = g["arg1"], g["arg2"], g["out"]
            if arg1 in args and arg2 in args:
                res.add(str_gate(g))
                args.add(out)
                if g["op"] == "OR":
                    carry = out

            if out == out_arg:
                res.add(str_gate(g))
                args.add(arg1)
                args.add(arg2)

        return carry

    carry_next = check()
    carry_next = check()
    carry_next = check()
    carry_next = check()

    if n == 0:
        assert len(res) == 2

    if n > 0:
        assert len(res) == 5

    assert carry_next != ""

    res = list(res)
    res.sort(reverse=True)

    return res, carry_next


# %%

# GOOD:
# Level 1:
# Prev carry: rhk
# x01 AND y01 -> hct
# x01 XOR y01 -> vsn
# rhk AND vsn -> tpp
# vsn XOR rhk -> z01
# tpp OR hct -> mbr

# BAD
# Level 29:
# Prev carry: dcf
# bfq XOR dcf -> gbs
# x29 AND y29 -> grd
# x29 XOR y29 -> bfq
# bfq AND dcf -> rpq
# grd OR rpq -> z29


def find_by_prefix(prefix, lvl_gates):
    results = [n for n in lvl_gates if n.startswith(prefix)]
    assert len(results) == 1, f"prefix: {prefix}, results: {results}"
    return results[0][-3:]


def find_by_prefix2(prefix1, prefix2, lvl_gates):
    results = [n for n in lvl_gates if n.startswith(prefix1) or n.startswith(prefix2)]
    assert (
        len(results) == 1
    ), f"prefix1: {prefix1}, prefix2: {prefix2}, results: {results}"
    return results[0][-3:]


def analyze_gates(lvl, lvl_gates, prev_carry, expected_next_carry):
    print("\n\nAnalyzing....")
    print(f"Level {lvl}:")
    print(f"Prev carry: {prev_carry}")
    print("\n".join(lvl_gates))
    print()

    lvl_str = f"{lvl:02}"
    x_arg = "x" + lvl_str
    y_arg = "y" + lvl_str
    out_arg = "z" + lvl_str

    xy_xor = find_by_prefix(f"{x_arg} XOR {y_arg}", lvl_gates)
    xy_and = find_by_prefix(f"{x_arg} AND {y_arg}", lvl_gates)

    print("xy_xor:", xy_xor)
    print("xy_and:", xy_and)

    z_out = find_by_prefix2(
        f"{prev_carry} XOR {xy_xor}", f"{xy_xor} XOR {prev_carry}", lvl_gates
    )
    print("z_out:", z_out)

    assert z_out == out_arg, f"z_out: {z_out} != {out_arg}"

    c_and_xy_xor = find_by_prefix2(
        f"{prev_carry} AND {xy_xor}", f"{xy_xor} AND {prev_carry}", lvl_gates
    )

    print("c_and_xy_xor:", c_and_xy_xor)

    next_carry = find_by_prefix2(
        f"{xy_and} OR {c_and_xy_xor}", f"{c_and_xy_xor} OR {xy_and}", lvl_gates
    )
    print("next_carry:", next_carry)

    assert (
        next_carry == expected_next_carry
    ), f"next_carry: {next_carry} != {expected_next_carry}"

    return next_carry


prev_carry = "rhk"
for lvl in range(1, 45):
    lvl_gates, expected_next_carry = get_level_gates(lvl, prev_carry)
    next_carry = analyze_gates(lvl, lvl_gates, prev_carry, expected_next_carry)
    prev_carry = next_carry


# %%

swaps = [
    "thm",
    "z08",
    "wrm",
    "wss",
    "z22",
    "hwq",
    "gbs",
    "z29",
]

swaps.sort()
print(",".join(swaps))

# %%
