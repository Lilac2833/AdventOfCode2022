class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, direction):
        self.x += (direction == "R") - (direction == "L")
        self.y += (direction == "U") - (direction == "D")
        return self

    def pos(self):
        return self.x, self.y


def update(parent, child):
    if max(abs(parent.x - child.x), abs(parent.y - child.y)) == 2:
        if parent.x == child.x or parent.y == child.y:  # Linearly separated
            child.x += -1 * (child.x > parent.x) + 1 * (child.x < parent.x)
            child.y += -1 * (child.y > parent.y) + 1 * (child.y < parent.y)
        else:  # Diagonally separated
            child.x += (-1) ** (child.x > parent.x)
            child.y += (-1) ** (child.y > parent.y)
    return child


def the_answer(n):
    # n = number of knots = (2 for part 1, 10 for part 2)
    knots = [Point() for i in range(n)]  # Head is knots[0], tail is knots[-1]
    visited = [(0, 0)]
    with open("input9", "r") as f:
        for line in f:
            line = line.split()
            d = line[0]
            amt = int(line[1])

            for _ in range(amt):
                knots[0] = knots[0].move(d)
                for i in range(1, n):
                    knots[i] = update(knots[i-1], knots[i])
                visited.append(knots[-1].pos())

    return len(set(visited))


print(the_answer(2))  # Part 1
print(the_answer(10))  # Part 2
