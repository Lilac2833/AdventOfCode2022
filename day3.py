def priority(c):
    return 1 + ord(c) - ord("a") if c.islower() else 27 + ord(c) - ord("A")


def part1_line_score(line):
    intersection = (set(line[len(line)//2:]) & set(line[:len(line)//2])).pop()
    return priority(intersection)


def part2_triple_score(triple):
    intersection = (set(triple[0]) & set(triple[1]) & set(triple[2])).pop()
    return priority(intersection)


with open("input3", "r") as f:
    lines = f.read().split("\n")[:-1]

print("Part 1:", sum(map(part1_line_score, lines)))
print("Part 2:", sum(map(part2_triple_score, zip(lines[::3], lines[1::3], lines[2::3]))))

