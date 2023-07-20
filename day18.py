from itertools import combinations, product


def are_neighbours(v1, v2):
    return sum(map(lambda x: abs(x[0] - x[1]), zip(v1, v2))) == 1


def enumerate_neighours(triple):  # Kinda lazy, but simple
    return (
        (triple[0] + 1, triple[1], triple[2]),
        (triple[0] - 1, triple[1], triple[2]),
        (triple[0], triple[1] + 1, triple[2]),
        (triple[0], triple[1] - 1, triple[2]),
        (triple[0], triple[1], triple[2] + 1),
        (triple[0], triple[1], triple[2] - 1),
    )


def surface_area(vertex_set):
    return 6 * len(vertex_set) - sum(map(lambda x: 2 * are_neighbours(x[0], x[1]), combinations(vertex_set, 2)))


def explore_connected_component(v0):
    queue = adj[v0]
    while queue:
        q = queue.pop()
        cc[q] = cc[v0]
        queue.update({r for r in adj[q] if not cc[r]})
    return


with open("input18", "r") as f:
    V_G = {(int(v1), int(v2), int(v3)) for [v1, v2, v3] in map(lambda x: x.strip("\n").split(","), f.readlines())}

m = max(map(max, V_G))
V_H = {a for a in product(set(range(-1, m + 2)), repeat=3) if a not in V_G}
adj = {v: {w for w in enumerate_neighours(v) if w in V_H} for v in V_H}
cc = {v: None for v in V_H}

cc[(-1, -1, -1)] = 1
explore_connected_component((-1, -1, -1))
n_cc = 1
for v in V_H:
    if not cc[v]:
        n_cc += 1
        cc[v] = n_cc
        explore_connected_component(v)

interior_surface_area = 0
for c in range(2, n_cc + 1):
    V_c = {v for v in V_H if cc[v] == c}
    interior_surface_area += surface_area(V_c)

print("Part 1: ", surface_area(V_G))
print("Part 2:", surface_area(V_G) - interior_surface_area)
