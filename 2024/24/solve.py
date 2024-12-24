# %%
import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

values = {}
names = set()


def parse_value(l):
    # x00: 1

    name, val = l.split(": ")
    values[name] = int(val)
    names.add(name)


gates = []

operations = {
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "XOR": lambda x, y: x ^ y,
}


def parse_gate(l):
    # x00 AND y00 -> z00
    exp, out = l.split(" -> ")
    arg1, op, arg2 = exp.split(" ")
    gate = {"arg1": arg1, "op": operations[op], "arg2": arg2, "out": out}
    gates.append(gate)

    names.add(arg1)
    names.add(arg2)
    names.add(out)


empty_line_idx = lines.index("")

for l in lines[:empty_line_idx]:
    parse_value(l)

for l in lines[empty_line_idx + 1 :]:
    parse_gate(l)

while len(values) < len(names):
    for gate in gates:
        if gate["arg1"] in values and gate["arg2"] in values:
            values[gate["out"]] = gate["op"](values[gate["arg1"]], values[gate["arg2"]])

print(values)

z_keys = [k for k in values.keys() if k.startswith("z")]
z_keys.sort(reverse=True)
print(z_keys)

res = 0
for k in z_keys:
    res = res * 2 + values[k]
print(res)

# %%
