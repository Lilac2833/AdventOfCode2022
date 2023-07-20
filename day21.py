from re import findall
from math import log2
from functools import lru_cache


class Monkey:
    def __init__(self, value=None, left=None, right=None, op=None):
        self.value = value
        self.left = left
        self.right = right
        self.op = op

    def evaluate(self, left_value, right_value):
        if self.op == "+":
            return left_value + right_value
        if self.op == "-":
            return left_value - right_value
        if self.op == "*":
            return left_value * right_value
        return left_value / right_value


def parse_line(line):
    tmp = findall("[a-z]+|\d+|[\+\-\*\/]", line)
    if len(tmp) == 2:
        return tmp[0], Monkey(value=int(tmp[1]))
    return tmp[0], Monkey(value=None, left=tmp[1], right=tmp[3], op=tmp[2])


def get_m():
    with open("input21", "r") as f:
        m = {name: monkey for name, monkey in map(parse_line, f.readlines())}
    return m

@lru_cache(maxsize=None)
def part1():
    m = get_m()
    def monkey_value(name):
        if m[name].value is not None:
            return m[name].value
        m[name].value = m[name].evaluate(monkey_value(m[name].left), monkey_value(m[name].right))
        return m[name].value

    return int(monkey_value("root"))


@lru_cache(maxsize=None)
def diff(x):
    # Let L and R be the children of "root". This function returns L.value - R.value
    m = get_m()

    def monkey_value(name):
        if m[name].value is not None:
            return m[name].value
        m[name].value = m[name].evaluate(monkey_value(m[name].left), monkey_value(m[name].right))
        return m[name].value

    m["humn"].value = x
    return monkey_value(m["root"].left) - monkey_value(m["root"].right)

def part2():
    x_l = 0
    x_r = 1

    # Construct interval inside which we will later perform bisection:
    while diff(x_l) * diff(x_r) > 0:
        x_r *= 2

    # Bisect
    while diff(x_r) and diff(x_l):
        x_m = (x_r + x_l)/2
        if diff(x_m) * diff(x_l) >= 0:
            x_l = x_m
        else:
            x_r = x_m

    return int(x_l) if not diff(x_l) else int(x_r)


print(part1())
print(part2())

#
# print(monkey_value("root"))
