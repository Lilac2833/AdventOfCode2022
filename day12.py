# NOTE: This code is really bad. I wanted to try using a package to handle Dijkstra, but it complicated part 2
from dijkstar import Graph, find_path, NoPathError

lines = []
with open("input12", "r") as f:
    for line in f.readlines():
        lines.append([c for c in line[:-1]])  # ignore \n
graph = Graph()
for i in range(len(lines)):
    lines[i].insert(0, "{")  # ord("z") == 122 and ord("{") == 123
    lines[i].append("{")
lines.insert(0, ["{"] * len(lines[0]))
lines.append(["{"] * len(lines[0]))

nrows = len(lines)
ncols = len(lines[0])
all_a_pts = []

for r in range(1, nrows - 1):
    for c in range(1, ncols - 1):
        if lines[r][c] == "E":
            height = ord("z")
            end = (r, c)
        elif lines[r][c] == "S":
            start = (r, c)
            height = ord("a")
            all_a_pts.append((r, c))
        else:
            height = ord(lines[r][c])
            if lines[r][c] == "a":
                all_a_pts.append((r, c))

        nbhrs = [(r + p[0], c + p[1]) for p in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
        for nbhr in nbhrs:
            if ord(lines[nbhr[0]][nbhr[1]]) <= height + 1:
                graph.add_edge((r, c), nbhr, 1)
path = find_path(graph, start, end)
print("Part 1:", path.total_cost)

# Time complexity of this is not good
best_length = path.total_cost
for p in all_a_pts:
    try:
        find_path(graph, p, end)
    except NoPathError:
        pass
    else:
        best_length = min(best_length, find_path(graph, p, end).total_cost)
print("Part 2:", best_length)
