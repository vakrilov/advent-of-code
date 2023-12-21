import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]


def p(fr, pulse, to):
    # print(f"{fr} {pulse} -> {to}")
    pass


class BroadcasterModule:
    def __init__(self, name, inputs, outputs):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs

    def __str__(self):
        return f"{self.name} {self.inputs} {self.outputs}"

    def process(self, pulse, fr):
        p(fr, pulse, self.name)

        return [(self.name, pulse, out) for out in self.outputs]


class ResetModule:
    def __init__(self, name, inputs, outputs):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs

    def __str__(self):
        return f"{self.name} {self.inputs} {self.outputs}"

    def process(self, pulse, fr):
        print("END")
        exit(0)


class FlipFlopModule:
    def __init__(self, name, inputs, outputs):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.state = "off"

    def __str__(self):
        return f"{self.name} {self.inputs} {self.outputs}"

    def process(self, pulse, fr):
        p(fr, pulse, self.name)

        if pulse == "low":
            self.state = "off" if self.state == "on" else "on"
            out_pulse = "high" if self.state == "on" else "low"
            return [(self.name, out_pulse, out) for out in self.outputs]
        else:
            return []


class ConjunctionModule:
    def __init__(self, name, inputs, outputs):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.state = dict((i, "off") for i in inputs)

    def __str__(self):
        return f"{self.name} {self.inputs} {self.outputs}"

    def process(self, pulse, fr):
        p(fr, pulse, self.name)

        self.state[fr] = pulse
        out_pulse = "low" if all(v == "high" for v in self.state.values()) else "high"
        return [(self.name, out_pulse, out) for out in self.outputs]


mod_defs = []
broadcast_outs = []
for l in lines:
    spl = l.split(" -> ")

    if spl[0] == "broadcaster":
        type = "b"
        name = "broadcaster"
    else:
        type = spl[0][0]
        name = spl[0][1:]

    outs = spl[1].split(", ")

    mod_defs.append((type, name, outs))

inputs = dict((mod[1], []) for mod in mod_defs)
for m in mod_defs:
    for o in m[2]:
        if o not in inputs:
            inputs[o] = []

        inputs[o].append(m[1])

modules = dict()
broadcast_outs = []
for m in mod_defs:
    if m[0] == "%":
        modules[m[1]] = FlipFlopModule(m[1], inputs[m[1]], m[2])
    elif m[0] == "&":
        modules[m[1]] = ConjunctionModule(m[1], inputs[m[1]], m[2])
    else:
        modules[m[1]] = BroadcasterModule(m[1], inputs[m[1]], m[2])


modules["rx"] = BroadcasterModule("rx", inputs["rx"], [])
# modules["output"] = BroadcasterModule("output", inputs["output"], [])


def press():
    lows = 0
    highs = 0
    queue = [("button", "low", "broadcaster")]
    while len(queue) > 0:
        fr, pulse, to = queue.pop(0)

        if pulse == "low":
            lows += 1
        else:
            highs += 1

        new_pulses = modules[to].process(pulse, fr)
        queue.extend(new_pulses)

    return lows, highs


for i in range(1, 1000000):
    lows, highs = press()
    print(f"{i:>10}, {lows:>2}, {highs:>2}")
