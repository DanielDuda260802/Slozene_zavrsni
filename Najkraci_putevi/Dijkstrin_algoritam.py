def dijkstra(nodes, edges, source):
    """
    :param list nodes: the set od nodes e.g. nodes = [0,1,2,3,4]
    :param dict edges: the set od edges e.g. edges = {(node, node) = distance}
    :return: the shortest distantes from the source node
    """
    path_lengths = {v: float('inf') for v in nodes}
    path_lengths[source] = 0

    adjacent_nodes = {v: {} for v in nodes} # lista susjeda koja se pohranjuje u obliku (u,v) : weight za svaki čvor u grafu
    for (u,v), weight in edges.items():
        adjacent_nodes[u][v] = weight
        adjacent_nodes[v][u] = weight

    temporary_nodes = [v for v in nodes] # privremeni čvorovi koji još nisu obrađeni
    while len(temporary_nodes) > 0:
        upper_bounds = {v: path_lengths[v] for v in temporary_nodes} # dictionary u koji pohranjujemo najkraću udaljenost do v čvora iz temporary_nodes-a
        u = min(upper_bounds, key=upper_bounds.get)

        temporary_nodes.remove(u)

        for v, weight in adjacent_nodes[u].items():
            path_lengths[v] = min(path_lengths[v], path_lengths[u]+weight)

    return path_lengths 

edges = {
    (0,1):1.0, 
    (0,2):1.5,
    (0,3):2.0, 
    (1,3):0.5, 
    (1,4):2.5, 
    (2,3):1.5, 
    (3,5):1.0
    }

nodes = [0,1,2,3,4,5]

print(*dijkstra(nodes, edges, 0).values())