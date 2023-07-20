def part1score(pair):
    diffs = [3, 6, 0]
    return diffs[(pair[1] - pair[0]) % 3] + (pair[1] + 1)


def part2score(pair):
    return 3*pair[1] + 1 + (pair[0] + pair[1] + 2) % 3


with open("input2", "r") as f:
    pairs = [(ord(line[0]) - ord("A"), ord(line[2]) - ord("X")) for line in f.readlines()]

print("Part 1:", sum(map(part1score, pairs)))
print("Part 2:", sum(map(part2score, pairs)))
