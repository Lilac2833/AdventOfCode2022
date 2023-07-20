top3 = [0, 0, 0]

with open("input1", "r") as f:
    total = 0
    for line in f.readlines():
        if line.strip():
            total += int(line.strip())
        else:
            if total > min(top3):
                top3.remove(min(top3))
                top3.append(total)
            total = 0

print("Part 1:", max(top3))
print("Part 2:", sum(top3))
