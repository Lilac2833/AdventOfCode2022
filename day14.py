class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_input():
    cave = [[False for i in range(700)] for j in range(200)]
    with open("input14", "r") as f:
        for line in f.readlines():
            line = line.replace("-", "").replace(">", "").replace(",", " ").split()
            pairs = [Point(int(line[2*i]), int(line[2*i+1])) for i in range(0, len(line)//2)]

            while len(pairs) > 1:
                current = pairs.pop(0)
                if current.x == pairs[0].x:
                    start = min(current.y, pairs[0].y)
                    end = max(current.y, pairs[0].y)
                    for ycoord in range(start, end + 1):
                        cave[ycoord][current.x] = True
                else:
                    start = min(current.x, pairs[0].x)
                    end = max(current.x, pairs[0].x)
                    for xcoord in range(start, end + 1):
                        cave[current.y][xcoord] = True
    return cave


def part1():
    cave = get_input()

    ymax = 1 + max([row for row in range(len(cave)) if max(cave[row])])
    units = 0
    while True:
        units += 1
        sand = Point(500, 0)
        while True:
            if sand.y == ymax:
                return units - 1
            if not cave[sand.y + 1][sand.x]:
                sand.y += 1
            elif not cave[sand.y + 1][sand.x - 1]:
                sand.y += 1
                sand.x -= 1
            elif not cave[sand.y + 1][sand.x + 1]:
                sand.y += 1
                sand.x += 1
            else:
                cave[sand.y][sand.x] = True
                break


def part2():
    cave = get_input()
    ymax = 2 + max([row for row in range(len(cave)) if max(cave[row])])
    cave = cave[:ymax + 1]
    for i in range(len(cave[-1])):
        cave[-1][i] = True
    units = 0
    while not cave[0][500]:
        units += 1
        sand = Point(500, 0)
        while True:
            if not cave[sand.y + 1][sand.x]:
                sand.y += 1
            elif not cave[sand.y + 1][sand.x - 1]:
                sand.y += 1
                sand.x -= 1
            elif not cave[sand.y + 1][sand.x + 1]:
                sand.y += 1
                sand.x += 1
            else:
                cave[sand.y][sand.x] = True
                break
    return units


print(part1())
print(part2())

