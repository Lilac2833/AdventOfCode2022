total = 0
if __name__ == '__main__':
    with open("input2", "r") as f:
        for line in f:
            p1 = ord(line[0]) - ord("A")
            result = ord(line[2]) - ord("X")
            total += 3*result
            total += 1 + (p1 + result + 2)%3

    print(total)
