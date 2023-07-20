def explore_directory(directory_name):
    global i, lines, all_sizes
    size = 0
    while i < len(lines):
        line = lines[i].split()  # For easier parsing
        i += 1
        if line[1] == "cd":
            if line[2] == "..":
                all_sizes.append(size)
                return size
            else:  # else it's "cd subdirectory_name"
                size += explore_directory(line[2])
        elif line[0].isnumeric():  # line looks like "filesize filename"
            size += int(line[0])
        # else line is "$ ls" or "dir something", which we can ignore
    # need the next two lines in case i == len(lines)
    all_sizes.append(size)
    return size


all_sizes = []
i = 0  # Global variable counting which line we are on
with open("input7", "r") as f:
    lines = f.readlines()[1:]  # ignore the first line
explore_directory("/")

# Part 1
print(sum([s for s in all_sizes if s <= 100000]))
# Part 2:
amount_needed = 30000000 - (70000000 - max(all_sizes))
print(min([s for s in all_sizes if s >= amount_needed]))
