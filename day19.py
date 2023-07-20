from re import findall
from numpy import prod
import pulp

with open("input19", "r") as f:
    blueprints = list(map(lambda line: tuple(map(int, findall(r"\d+", line))), f.readlines()))


def optimize_blueprint(bp, t_max):
    # Define LP variables
    ores = pulp.LpVariable.dicts("ores", range(t_max + 1), lowBound=0, cat="Integer")
    clays = pulp.LpVariable.dicts("clays", range(t_max + 1), lowBound=0, cat="Integer")
    obsidians = pulp.LpVariable.dicts("obsidians", range(t_max + 1), lowBound=0, cat="Integer")
    geodes = pulp.LpVariable.dicts("geodes", range(t_max + 1), lowBound=0, cat="Integer")

    ore_robots = pulp.LpVariable.dicts("ore_robots", range(t_max + 1), lowBound=0, cat="Integer")
    clay_robots = pulp.LpVariable.dicts("clay_robots", range(t_max + 1), lowBound=0, cat="Integer")
    obsidian_robots = pulp.LpVariable.dicts("obsidian_robots", range(t_max + 1), lowBound=0, cat="Integer")
    geode_robots = pulp.LpVariable.dicts("geode_robots", range(t_max + 1), lowBound=0, cat="Integer")

    ore_robot_built = pulp.LpVariable.dicts("ore_robot_built", range(t_max + 1), cat="Binary")
    clay_robot_built = pulp.LpVariable.dicts("clay_robot_built", range(t_max + 1), cat="Binary")
    obsidian_robot_built = pulp.LpVariable.dicts("obsidian_robot_built", range(t_max + 1), cat="Binary")
    geode_robot_built = pulp.LpVariable.dicts("geode_robot_built", range(t_max + 1), cat="Binary")

    # Now define optimization problem
    prob = pulp.LpProblem("Geode_maximization_problem", pulp.LpMaximize)
    prob += geodes[t_max]  # Want to optimize geodes at time t_max

    # Now add all the constraints! Start with initial conditions
    prob += ores[0] == 0
    prob += clays[0] == 0
    prob += obsidians[0] == 0
    prob += geodes[0] == 0

    prob += ore_robots[0] == 1
    prob += clay_robots[0] == 0
    prob += obsidian_robots[0] == 0
    prob += geode_robots[0] == 0

    prob += ore_robot_built[0] == 0
    prob += clay_robot_built[0] == 0
    prob += obsidian_robot_built[0] == 0
    prob += geode_robot_built[0] == 0

    for t in range(1, t_max + 1):
        # Building new robots.
        prob += ore_robots[t] == ore_robots[t-1] + ore_robot_built[t]
        prob += clay_robots[t] == clay_robots[t - 1] + clay_robot_built[t]
        prob += obsidian_robots[t] == obsidian_robots[t - 1] + obsidian_robot_built[t]
        prob += geode_robots[t] == geode_robots[t - 1] + geode_robot_built[t]

        # Must be able to afford any robots built:
        prob += ores[t-1] >= bp[1]*ore_robot_built[t] + bp[2]*clay_robot_built[t] + bp[3]*obsidian_robot_built[t] + bp[5]*geode_robot_built[t]
        prob += clays[t-1] >= bp[4]*obsidian_robot_built[t]
        prob += obsidians[t-1] >= bp[6]*geode_robot_built[t]

        # Can't build more than one robot per minute:
        prob += 1 >= ore_robot_built[t] + clay_robot_built[t] + obsidian_robot_built[t] + geode_robot_built[t]

        # Robots build materials:
        prob += ores[t] == ores[t-1] + ore_robots[t-1] - (bp[1]*ore_robot_built[t] + bp[2]*clay_robot_built[t] + bp[3]*obsidian_robot_built[t] + bp[5]*geode_robot_built[t])
        prob += clays[t] == clays[t-1] + clay_robots[t-1] - bp[4]*obsidian_robot_built[t]
        prob += obsidians[t] == obsidians[t - 1] + obsidian_robots[t - 1] - bp[6]*geode_robot_built[t]
        prob += geodes[t] == geodes[t-1] + geode_robots[t-1]

    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    return pulp.value(prob.objective)


print("Part 1:", sum(map(lambda b: b[0] * optimize_blueprint(b, t_max=24), blueprints)))
print("Part 2:", prod([optimize_blueprint(b, t_max=32) for b in blueprints[:3]]))
