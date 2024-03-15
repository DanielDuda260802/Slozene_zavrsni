def matrix_to_edges_dict(matrix):
    edges = {}
    for i, row in enumerate(matrix):
        for j, weight in enumerate(row):
            if weight != 0:  
                edges[(i+1, j+1)] = weight 
    return edges

def bellman_ford(source, nodes, edges):
    distance_from_node_to_source = {v: float('inf') for v in nodes} 
    distance_from_node_to_source[source] = 0

    paths = {v: [] for v in nodes}
    paths[source] = [source] 

    for _ in range(len(nodes)-1):
        for (u,v), weight in edges.items():
            if distance_from_node_to_source[u] + weight < distance_from_node_to_source[v]:
                distance_from_node_to_source[v] = distance_from_node_to_source[u] + weight
                paths[v] = paths[u] + [v]   
    
    # AKO OVO VRIJEDI POSTOJI NEGATIVNI CIKLUS
    for (u,v), weight in edges.items():
        if distance_from_node_to_source[u] + weight < distance_from_node_to_source[v]:
            print('Graph has a negative weight cycle.')

    return distance_from_node_to_source

source, city_number = list(map(int,input().split()))
nodes = []
for i in range(city_number):
    nodes.append(i+1)

matrix = [
    [0, 5, 3, 2, 5], 
    [9, 0, 4, 0, 0], 
    [7, 6, 0, 2, 8],
    [2, 0, 1, 0, 3],
    [0, 7, 5, 5, 0],
]


edges = matrix_to_edges_dict(matrix)
shortest_path = bellman_ford(source,nodes,edges)

for shortest in shortest_path.values():
    print(shortest)