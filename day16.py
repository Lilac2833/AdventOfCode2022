with open("input16", "r") as f:
    lines = f.readlines()


class Valve:
    def __init__(self, name_, flow_, nbhd_):
        self.name = name_
        self.flow = flow_
        self.nbhd = nbhd_


valves = {}
for line in lines:
    line = line.split()
    name = line[1]
    flow = int(line[4][5:-1])
    nbhd = [x.rstrip(",") for x in line[9:]]
    valves[name] = Valve(name, flow, nbhd)


def max_pressure_released(time_left, current_valve, opened_valves, players, avoid=None):
    key = tuple([time_left, current_valve] + opened_valves + [players])
    if key in memos:
        return memos[key]

    # Here we make an educated guess:
    # The optimal strategy will probably involve both players opening similar numbers of valves
    if players == 2 and len(opened_valves) > 9:
        memos[key] = max_pressure_released(total_time, valves["AA"], opened_valves, players=1)
        return memos[key]

    if players == 1 and len(opened_valves) < 6:
        memos[key] = 0  # Not actually 0, but we can assume that such a distribution of labour will not be optimal
        return memos[key]

    if time_left == 1:
        if players == 2:
            memos[key] = max_pressure_released(total_time, valves["AA"], opened_valves, players=1)
        else:
            memos[key] = 0
        return memos[key]

    # Now go through possible scenarios
    best = 0
    # If current valve isn't open, we could open it:
    if current_valve.name not in opened_valves and current_valve.flow > 0:
        pressure_released = current_valve.flow * (time_left - 1)
        tmp = opened_valves + [current_valve.name]
        tmp.sort()
        best = max(best, pressure_released +
                   max_pressure_released(time_left - 1, current_valve, tmp, players))
    # We can also try moving:
    for neighbour in current_valve.nbhd:
        if neighbour != avoid:
            best = max(best, max_pressure_released(time_left - 1, valves[neighbour],
                                                   opened_valves, players, avoid=current_valve))

    memos[key] = best
    return best

memos = {}  # Memoization
total_time = 26

# For part 1, set total_time = 30, remove lines 26-34, and use the line below
# print("Part 1:", max_pressure_released(30, "AA", [], players=1))

print("Part 2:", max_pressure_released(total_time, valves["AA"], [], players=2))

