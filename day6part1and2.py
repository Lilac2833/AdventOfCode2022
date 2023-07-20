with open("input6", "r") as f:
    s = f.read()

i = 0
while True:
    if len(set(s[i:i+14])) == 14:  # Use 4 for part 1
        break
    else:
        i = i+1
print(i + 14)  # Use 4 for part 1