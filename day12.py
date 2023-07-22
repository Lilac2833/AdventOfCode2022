# Not my best work :) But wanted to try using the dijkstar package
from dijkstar import Graph, find_path, NoPathError

with open("input12", "r") as f:
    lines = ["{" + line.rstrip() + "{" for line in f.readlines()]
lines.insert(0, "{" * len(lines[0]))   # ord("z") == 122 and ord("{") == 123
lines.append("{" * len(lines[0]))

graph = Graph()


def height(character):
    return ord({"S": "a", "E": "z"}[character]) if character.isupper() else ord(character)


list_of_a_points = set({})
for row_idx, line in enumerate(lines):
    for col_idx, char in enumerate(line):
        if char == "{":
            continue
        if char == "E":
            end = (row_idx, col_idx)
        elif char == "S":
            start = (row_idx, col_idx)
        if char == "a" or char == "S":
            list_of_a_points.add((row_idx, col_idx))

        for horiz_step, vert_step in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if height(lines[row_idx + horiz_step][col_idx + vert_step]) <= height(char) + 1:
                graph.add_edge((row_idx, col_idx), (row_idx + horiz_step, col_idx + vert_step), 1)

path = find_path(graph, start, end)
print("Part 1:", path.total_cost)

best_length = path.total_cost
for p in list_of_a_points:
    try:
        best_length = min(best_length, find_path(graph, p, end).total_cost)
    except NoPathError:
        pass

print("Part 2:", best_length)
