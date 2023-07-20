from re import findall

with open("input1", "r") as f:
    elf_totals = sorted([sum([int(x) for x in findall("[0-9]+", elf)]) for elf in f.read().split("\n\n")], reverse=True)

print("Part 1:", elf_totals[0])
print("Part 2:", sum(elf_totals[:3]))
