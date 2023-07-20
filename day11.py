from operator import add, mul
from math import prod


class Monkey:
    def __init__(self, items, bin_op, arg2, modulus, if_true, if_false):
        self.items = items
        self.n_inspected = 0
        self.modulus = modulus
        if arg2 == "old":
            self.inspect = lambda x: {"+": add, "*": mul}[bin_op](x, x)
        else:
            self.inspect = lambda x: {"+": add, "*": mul}[bin_op](x, int(arg2))
        self.throw = lambda x: if_true*(x % modulus == 0) + if_false*(x % modulus != 0)


class Monkeys:
    def __init__(self, list_of_monkeys):
        self.monkeys = list_of_monkeys
        self.modulus = 3*prod([m.modulus for m in list_of_monkeys])  # Part 1 requires the 3

    def act(self, m, part):  # m = index of current monkey
        while self.monkeys[m].items:
            i = self.monkeys[m].items.pop(0)
            new_worry = self.monkeys[m].inspect(i)
            if part == 1:
                new_worry //= 3
            thrown_to = self.monkeys[m].throw(new_worry)
            reduced_worry = new_worry % self.modulus
            self.monkeys[thrown_to].items.append(reduced_worry)
            self.monkeys[m].n_inspected += 1


def parse_input():
    with open("input11", "r") as f:
        lines = f.readlines()
    monkeys = []
    for i in range(8):
        item_line = lines[7*i + 1].replace(',', '').split()
        items = [int(x) for x in item_line if x.isnumeric()]

        operation_line = lines[7*i + 2].split()
        bin_op = operation_line[-2]
        arg2 = operation_line[-1]

        modulus = int(lines[7*i + 3].split()[-1])
        if_true = int(lines[7*i + 4].split()[-1])
        if_false = int(lines[7*i + 5].split()[-1])

        monkeys.append(Monkey(items, bin_op, arg2, modulus, if_true, if_false))
    return Monkeys(monkeys)


def answer(n_rounds, part):
    all_monkeys = parse_input()
    for _ in range(n_rounds):
        for m in range(8):
            all_monkeys.act(m, part)
    tmp = [mon.n_inspected for mon in all_monkeys.monkeys]
    tmp.sort()
    return tmp[-1]*tmp[-2]


print(answer(20, 1))  # Part 1
print(answer(10000, 2))  # Part 2
