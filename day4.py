from re import findall


def full_overlap(nums):
    return (nums[0] >= nums[2] and nums[1] <= nums[3]) or (nums[0] <= nums[2] and nums[1] >= nums[3])


def any_overlap(nums):
    return nums[0] <= nums[2] <= nums[1] or nums[2] <= nums[0] <= nums[3]


def get_numbers(line):
    return [int(x) for x in findall("[0-9]+", line)]


with open("input4", "r") as f:
    lines = f.readlines()

print("Part 1:", sum(map(lambda x: full_overlap(get_numbers(x)), lines)))
print("Part 2:", sum(map(lambda x: any_overlap(get_numbers(x)), lines)))
