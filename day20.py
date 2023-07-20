class Pair:
    def __init__(self, val, order):
        self.val = val
        self.order = order


def get_answer(part):
    with open("input20", "r") as f:
        a = [Pair(int(x.rstrip("\n")), idx) for idx, x in enumerate(f.readlines())]

    n = len(a)

    nreps = 1 if part == 1 else 10
    if part == 2:
        for p in a:
            p.val *= 811589153
    for _ in range(nreps):
        for i in range(n):
            j, v = next((idx, p.val) for idx, p in enumerate(a) if p.order == i)
            a.pop(j)
            new_idx = (n - 1 + j + v) % (n-1)
            a.insert(new_idx, Pair(v, i))

    b = [p.val for p in a]
    idx_0 = next(idx for idx, val in enumerate(b) if val == 0)

    return b[(idx_0 + 1000) % n] + b[(idx_0 + 2000) % n] + b[(idx_0 + 3000) % n]


print(get_answer(part=1))
print(get_answer(part=2))
