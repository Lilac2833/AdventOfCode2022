import numpy as np

t = np.empty((99,99))
with open("input8", "r") as f:
    lines = f.readlines()

for row in range(99):
    for col in range(99):
        t[row][col] = int(lines[row][col])

def part2():
    best = 0
    for r in range(1, 98):
        for c in range(1, 98):
            east = west = north = south = 1
            while c - east > 0 and t[r, c - east] < t[r, c]:
                east += 1
            while c + west < 98 and t[r, c + west] < t[r, c]:
                west += 1
            while r - north > 0 and t[r - north, c] < t[r, c]:
                north += 1
            while r + south < 98 and t[r + south, c] < t[r, c]:
                south += 1
            best = max(best, east*west*north*south)

    print(best)

def part1():
    total = 4*98
    for row in range(1, 98):
        for col in range(1, 98):
            if t[row,col] > min(max(t[:row,col]), max(t[row+1:,col]), max(t[row,:col]), max(t[row,col+1:])):
                total += 1
    print(total)

part1()
part2()
