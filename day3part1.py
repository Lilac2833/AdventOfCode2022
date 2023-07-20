def priority(c):
    if c.islower():
        return 1 + ord(c) - ord("a")
    else:
        return 27 + ord(c) - ord("A")


total = 0
with open("input3", "r") as f:
    for line in f:
        temp = (len(line) - 1)//2  # Last char is \n
        intersection = list(set(line[:temp]) & set(line[temp:-1]))
        for i in intersection:
            total += priority(i)

print(total)