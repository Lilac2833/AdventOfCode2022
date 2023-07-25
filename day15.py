from re import findall


class Sensor:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def bdry(self):
        return {(self.x + i, self.y + sign * abs(i)) for i in range(-self.r - 1, self.r + 2) for sign in [+1, -1]}


class Beacon:
    def __init__(self, x, y):
        self.x = x
        self.y = y


with open("input15", "r") as f:
    lines = [[int(x) for x in findall("[-]*[0-9]+", line)] for line in f.readlines()]

sensors = {Sensor(line[0], line[1], abs(line[0] - line[2]) + abs(line[1] - line[3])) for line in lines}
beacons = {Beacon(line[2], line[3]) for line in lines}


def covered_range(sensor, row_number, part):
    available_radius = sensor.r - abs(sensor.y - row_number)
    if available_radius < 0:
        return None
    lower = max(0, sensor.x - available_radius) if part == 2 else sensor.x - available_radius
    upper = min(4000000, sensor.x + available_radius) if part == 2 else sensor.x + available_radius
    return [lower, upper]


def part1():
    total_covered = 0
    row = 2000000
    beacon_locations = {b.x for b in beacons if b.y == 2000000}
    intervals = sorted([covered_range(sensor, row, part=1) for sensor in sensors if covered_range(sensor, row, part=1)], key=lambda x: x[0])
    ivl = intervals[0]
    for e in intervals:
        if e[0] <= ivl[1] + 1:
            ivl[1] = max(ivl[1], e[1])
        else:
            total_covered += ivl[1] - ivl[0] + 1 - sum([1 for x in beacon_locations if ivl[0] <= x <= ivl[1]])
            ivl = e
    total_covered += ivl[1] - ivl[0] + 1 - sum([1 for x in beacon_locations if ivl[0] <= x <= ivl[1]])
    return total_covered


def part2():
    for row in range(4000000):
        ivl = [-1, -1]
        for e in sorted([covered_range(sensor, row, part=2) for sensor in sensors if covered_range(sensor, row, part=2)],
                        key=lambda x: x[0]):
            if e[0] > ivl[1] + 1:
                return 4000000 * (ivl[1] + 1) + row
            ivl[1] = max(ivl[1], e[1])
        if ivl[1] != 4000000:
            return 4000000 ** 2 + 4000000


print("Part 1:", part1())
print("Part 2:", part2())






