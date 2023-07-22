with open("input6", "r") as f:
    s = f.read()


def get_answer(n_distinct):
    i = 0
    while len(set(s[i:i+n_distinct])) != n_distinct:
        i += 1
    return i + n_distinct


print("Part 1:", get_answer(4))
print("Part 2:", get_answer(14))
