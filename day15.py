import re
from collections import Counter


class Sensor:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.bdry = [(x, y+r+1), (x+r+1, y), (x, y-r-1), (x-r-1, y)]  # For part 2

class Beacon:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_input():
    sensors = []
    beacons = []
    with open("input15", "r") as f:
        for line in f.readlines():
            temp = re.findall("\d+", line)
            temp = [int(t) for t in temp]
            radius = abs(temp[0] - temp[2]) + abs(temp[1] - temp[3])
            sensors.append(Sensor(temp[0], temp[1], radius))
            beacons.append(Beacon(temp[2], temp[3]))
    return sensors, set(beacons)


def part1():
    sensors, beacons = get_input()
    beacon_x_pts = set([b.x for b in beacons if b.y == 2000000])
    pts_within_radii = []
    for s in sensors:
        if abs(s.y - 2000000) < s.r:
            r_avail = s.r - abs(s.y - 2000000)
            pts_within_radii += [s.x + i for i in range(-r_avail, r_avail + 1)]
            if r_avail == 0:
                pts_within_radii.append(s.x)
    return len(set(pts_within_radii) - beacon_x_pts)


def part2():
    sensors, beacons = get_input()
    candidates = []
    for s in sensors:
        for i in range(-s.r - 1, s.r + 2):
            if 0 <= s.x + i <= 4000000 and 0 <= s.y + s.r + 1 - i <= 4000000:
                candidates.append((s.x + i, s.y + (s.r + 1 - i)))
        print(len(candidates))
    ctr = Counter(candidates)
    for c in ctr:
        if ctr[c] == 4:
            return c



def sensor_intersection(s1, s2):
    pts = []
    for i in [0, 1, 2]:



#print(part1())
print(part2())


