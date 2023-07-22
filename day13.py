import json


def compare_packets(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return None if left == right else left < right

    elif isinstance(left, list) and isinstance(right, list):
        for left_elt, right_elt in zip(left, right):
            tmp = compare_packets(left_elt, right_elt)
            if tmp is not None:
                return tmp
        return None if len(left) == len(right) else len(right) > len(left)

    else:  # Else one is int and one is list
        if isinstance(left, int):
            left = [left]
        else:
            right = [right]
        return compare_packets(left, right)


with open("input13", "r") as f:
    all_packets = [json.loads(p) for p in f.readlines() if p != "\n"]

print("Part 1:", sum([idx + 1 for idx, pair in enumerate(zip(all_packets[::2], all_packets[1::2])) if
                      compare_packets(pair[0], pair[1])]))

loc2 = sum([1 for p in all_packets if compare_packets(p, [[2]])])
loc6 = sum([1 for p in all_packets if compare_packets(p, [[6]])]) + 1
print("Part 2:", (1 + loc2) * (1 + loc6))
