import json
import functools
from copy import deepcopy


def compare_packets(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None
    elif isinstance(left, list) and isinstance(right, list):
        while len(left) > 0 and len(right) > 0:
            left2 = left.pop(0)
            right2 = right.pop(0)
            tmp = compare_packets(left2, right2)
            if tmp is not None:
                return tmp
        if len(left) == 0 and len(right) > 0:
            return True
        elif len(left) > 0 and len(right) == 0:
            return False
        else:
            return None
    else:
        if isinstance(left, int):
            left = [left]
        else:
            right = [right]
        return compare_packets(left, right)


def cmp(left, right):
    x = compare_packets(deepcopy(left), deepcopy(right))
    return 1 * (x is False) + 0 * (x is None) - 1 * (x is True)


if __name__ == "__main__":
    all_packets = []
    with open("input13", "r") as f:
        for p in f.readlines():
            if p != "\n":
                all_packets.append(json.loads(p))

    answer_1 = 0
    for i in range(len(all_packets) // 2):
        packet_1 = deepcopy(all_packets[2 * i])
        packet_2 = deepcopy(all_packets[2 * i + 1])
        if compare_packets(packet_1, packet_2):
            answer_1 += i + 1
    print("Part 1 answer is", answer_1)


    all_packets.append([[2]])
    all_packets.append([[6]])

    all_packets.sort(key=functools.cmp_to_key(cmp))
    answer_2 = (1 + all_packets.index([[2]]))*(1 + all_packets.index([[6]]))
    print("Part 2 answer is", answer_2)
