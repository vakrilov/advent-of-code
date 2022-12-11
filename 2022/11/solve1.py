import os
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

class Monkey:
    def __init__(self):
        self.items = []
        self.op = None
        self.op_arg = ""
        self.test_div = 0
        self.if_false = 0
        self.if_true = 0
        self.inspect_count = 0

    def inspect(self, worry):
        self.inspect_count +=1
        if self.op == "square":
            worry *= worry
        elif self.op == "*":
            worry *= self.op_arg
        else:
            worry += self.op_arg
        
        return worry // 3

    
    def test(self, worry):
        if worry % self.test_div == 0:
            return self.if_true
        else:
            return self.if_false

    def do_round(self, other_monkeys):
        for worry in self.items:
            new_worry = self.inspect(worry)
            throw_to = self.test(new_worry)
            other_monkeys[throw_to].items.append(new_worry)
        self.items = []


lines = [l.removesuffix("\n") for l in f.readlines()]

monkeys = []
for i in range(0,len(lines),7):
    monkey = Monkey()
    monkey.items = [int(worry) for worry in lines[i+1].removeprefix("  Starting items: ").split(", ")]
   
    op = lines[i+2].removeprefix("  Operation: new = old ")
    if op == "* old":
        monkey.op = "square"
    elif op.startswith("*"):
        num = int(op[2:])
        monkey.op = "*"
        monkey.op_arg = num
    elif op.startswith("+"):
        num = int(op[2:])
        monkey.op = "+"
        monkey.op_arg = num

    monkey.test_div = int(lines[i+3].removeprefix("  Test: divisible by "))
    monkey.if_true = int(lines[i+4].removeprefix("    If true: throw to monkey "))
    monkey.if_false = int(lines[i+5].removeprefix("    If false: throw to monkey "))

    monkeys.append(monkey)


for i in range(20):
    for m in monkeys:
        m.do_round(monkeys)

    print("Round", i+1)
    for i, m in enumerate(monkeys):
            print(f'  Monkey {i}: {m.items}')

active = [m.inspect_count for m in monkeys]
active.sort(reverse=True)


print(active[0] * active[1])
