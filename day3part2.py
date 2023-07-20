def priority(c):
    if c.islower():
        return 1 + ord(c) - ord("a")
    else:
        return 27 + ord(c) - ord("A")


total = 0
with open("input3", "r") as f:
    lines = f.readlines()

for i in range(0, len(lines), 3):
    intersection = list(set(lines[i][:-1]) & set(lines[i+1]) & set(lines[i+2]))  # [:-1] to remove \n
    total += priority(intersection[0])

print(total)
