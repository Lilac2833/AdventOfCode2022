directory_stack = []
current_size = 0
final_sizes = []

with open("input7", "r") as f:
    lines = map(str.split, f.readlines())

for line in lines:
    if line[1] == "cd":
        if line[2] == "..":
            final_sizes.append(current_size)
            current_size += directory_stack.pop(0)
        else:
            directory_stack.insert(0, current_size)  # Inserting at index 0 is not optimal, but it's good enough here.
            current_size = 0
    elif line[0].isnumeric():
        current_size += int(line[0])

# Clean up current file and stack:
final_sizes.append(current_size)
while directory_stack:
    current_size += directory_stack.pop(0)
    final_sizes.append(current_size)

print("Part 1:", sum([s for s in final_sizes if s <= 100000]))
amount_needed = 30000000 - (70000000 - max(final_sizes))
print("Part 2:", min([s for s in final_sizes if s >= amount_needed]))
