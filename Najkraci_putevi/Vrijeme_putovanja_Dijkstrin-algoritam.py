def matrix_to_edges_dict(matrix):
    edges = {}
    for i, row in enumerate(matrix):
        for j, weight in enumerate(row):
            if weight != 0:  
                edges[(i+1, j+1)] = weight 
    return edges

def dijkstrin(nodes, edges, source):
    path_lengths = {v: float('inf') for v in nodes}
    path_lengths[source] = 0

    adjacent_nodes = {v: {} for v in nodes}
    for (u,v), weight in edges.items():
        adjacent_nodes[u][v] = weight
        # adjacent_nodes[v][u] = weight --> ako je dvosmjerno

    temporary_nodes = [v for v in nodes]
    while len(temporary_nodes) > 0:
        upper_bounds = {v: path_lengths[v] for v in temporary_nodes}
        u = min(upper_bounds, key=upper_bounds.get)

        temporary_nodes.remove(u)

        for v, weight in adjacent_nodes[u].items():
            path_lengths[v] = min(path_lengths[v], path_lengths[u] + weight)
    
    return path_lengths

source, m = list(map(int, input().split()))
nodes = []
for i in range(m):
    nodes.append(i+1)

matrix = [
    [0, 5, 3, 2, 5], 
    [9, 0, 4, 0, 0], 
    [7, 6, 0, 2, 8],
    [2, 0, 1, 0, 3],
    [0, 7, 5, 5, 0],
]

edges = matrix_to_edges_dict(matrix)
shortest_path = dijkstrin(nodes,edges,source)

for shortest in shortest_path.values():
    print(shortest)
