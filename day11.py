from operator import add, mul
from math import prod
from re import findall


class Monkey:
    def __init__(self, starting_items, other_data):
        self.items = starting_items
        self.n_inspected = 0
        self.modulus = other_data[2]
        if other_data[1] == "old":
            self.inspect = lambda x: {"+": add, "*": mul}[other_data[0]](x, x)
        else:
            self.inspect = lambda x: {"+": add, "*": mul}[other_data[0]](x, other_data[1])
        self.throw = lambda x: other_data[4] if x % self.modulus else other_data[3]


class Monkeys:
    def __init__(self, list_of_monkeys):
        self.monkeys = list_of_monkeys
        self.modulus = 3*prod([m.modulus for m in list_of_monkeys])  # Part 1 requires the 3

    def act(self, m, part):  # m = index of current monkey
        while self.monkeys[m].items:
            new_worry = self.monkeys[m].inspect(self.monkeys[m].items.pop(0))
            if part == 1:
                new_worry //= 3
            thrown_to = self.monkeys[m].throw(new_worry)
            reduced_worry = new_worry % self.modulus
            self.monkeys[thrown_to].items.append(reduced_worry)
            self.monkeys[m].n_inspected += 1


def parse_input():
    with open("input11", "r") as f:
        lines = [line for line in f.readlines() if line != "\n"]
    monkeys = []
    while lines:
        block = lines[1:6]
        del lines[:6]  # Not exactly the optimal way to go through blocks, but no big deal for such a small input
        starting_items = [int(x) for x in findall("[0-9]+", block[0])]
        other_data = [int(x) if x.isnumeric() else x for x in findall("[0-9]+|[\+\-\*\/]|old(?=\n)", "".join(block[1:]))]
        monkeys.append(Monkey(starting_items, other_data))
    return Monkeys(monkeys)


def answer(n_rounds, part):
    all_monkeys = parse_input()
    for _ in range(n_rounds):
        for m in range(8):
            all_monkeys.act(m, part)
    tmp = [mon.n_inspected for mon in all_monkeys.monkeys]
    tmp.sort()
    return tmp[-1]*tmp[-2]


print("Part 1:", answer(20, 1))
print("Part 2:", answer(10000, 2))
