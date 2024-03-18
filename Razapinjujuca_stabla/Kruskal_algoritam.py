def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, x, y):
    parent[find(parent,y)] = find(parent,x)

def kruskal(n, edges):
    result = []  
    i, e = 0, 0  
    parent = []

    sorted_edges = sorted(edges.items(), key=lambda item: item[1])

    for node in range(n):
        parent.append(node)

    while e < n - 1:
        (u, v), weight = sorted_edges[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append(((u, v), weight))
            union(parent, x, y)

    for (u, v), weight in result:
        print(f"({u}, {v}) -> {weight}")

edges = {(0, 1): 10, (0, 2): 6, (0, 3): 5, (1, 3): 15, (2, 3): 4}
kruskal(4, edges)  
