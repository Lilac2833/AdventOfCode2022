total = 0
with open("input4", "r") as f:
    for line in f:
        line = line.replace(",", " ").replace("-", " ")
        line = line.split()
        nums = [int(x) for x in line]
        print(nums)
        if (nums[0] >= nums[2] and nums[1] <= nums[3]) or (nums[0] <= nums[2] and nums[1] >= nums[3]):
            total += 1

print(total)
