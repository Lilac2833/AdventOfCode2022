directory_stack = []
current_size = 0
final_sizes = []

with open("input7", "r") as f:
    for line in f.readlines():
        line = line.split()
        if line[1] == "cd":
            if line[2] == "..":
                final_sizes.append(current_size)
                current_size += directory_stack.pop(0)
            else:
                directory_stack.insert(0, current_size)
                current_size = 0
        elif line[0].isnumeric():
            current_size += int(line[0])

# Clean up current file and stack:
final_sizes.append(current_size)
while len(directory_stack) > 1:
    current_size += directory_stack.pop(0)
    final_sizes.append(current_size)

# Part 1:
print(sum([s for s in final_sizes if s <= 100000]))
# Part 2:
amount_needed = 30000000 - (70000000 - max(final_sizes))
print(min([s for s in final_sizes if s >= amount_needed]))
