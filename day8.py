import numpy as np
from itertools import product, chain

with open("input8", "r") as f:
    t = np.array([[int(entry) for entry in row.rstrip("\n")] for row in f.readlines()])


def visible(row, col):
    return t[row, col] > min(max(t[:row, col]), max(t[row+1:, col]), max(t[row, :col]), max(t[row, col+1:]))


def scenic_score(row, col):
    height = t[row, col]

    east = next(chain((e for e in range(1, col) if t[row, col - e] >= height), [col]))
    west = next(chain((w for w in range(1, 98 - col) if t[row, col + w] >= height), [98 - col]))
    north = next(chain((n for n in range(1, row) if t[row - n, col] >= height), [row]))
    south = next(chain((s for s in range(1, 98 - row) if t[row + s, col] >= height), [98 - row]))
    return east * west * north * south


print("Part 1:", 4 * 98 + sum(map(lambda coords: visible(*coords), product(range(1, 98), range(1, 98)))))
print("Part 2:", max(map(lambda coords: scenic_score(*coords), product(range(1, 98), range(1, 98)))))
