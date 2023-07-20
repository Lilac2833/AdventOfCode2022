total = 0
with open("input4", "r") as f:
    for line in f:
        line = line.replace(",", " ").replace("-", " ")
        line = line.split()
        nums = [int(x) for x in line]
        if not (nums[1] < nums[2] or nums[3] < nums[0]):
            total += 1

print(total)
