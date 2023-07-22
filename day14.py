from re import findall


class Point:
    def __init__(self, coord):
        self.x = coord[0]
        self.y = coord[1]


def get_input():
    cave = [[False for i in range(700)] for j in range(200)]
    with open("input14", "r") as f:
        lines = map(lambda ell: [int(x) for x in findall("[0-9]+", ell)], f.readlines())

    for line in lines:
        corners = [Point(coord) for coord in zip(line[::2], line[1::2])]

        for idx, c in enumerate(corners[:-1]):
            if c.x == corners[idx + 1].x:
                start, end = min(c.y, corners[idx + 1].y), max(c.y, corners[idx + 1].y)
                for ycoord in range(start, end + 1):
                    cave[ycoord][c.x] = True
            else:
                start, end = min(c.x, corners[idx + 1].x), max(c.x, corners[idx + 1].x)
                for xcoord in range(start, end + 1):
                    cave[c.y][xcoord] = True
    return cave


def part1():
    cave = get_input()
    ymax = 1 + next((len(cave) - idx - 1 for idx, row in enumerate(cave[::-1]) if any(row)))
    units = 0
    while True:
        units += 1
        sand = Point((500, 0))
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
    ymax = 2 + next((len(cave) - idx - 1 for idx, row in enumerate(cave[::-1]) if any(row)))
    cave = cave[:ymax + 1]
    cave[-1] = [True] * len(cave[-1])

    units = 0
    while not cave[0][500]:
        units += 1
        sand = Point((500, 0))
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


print("Part 1:", part1())
print("Part 2:", part2())

