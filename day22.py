from re import findall


with open("practice22", "r") as f:
    lines = f.readlines()

distances = findall("[RL]+", lines[-1])
directions = map(int, findall("\d+", lines[-1]))

print(distances)
print(directions)
