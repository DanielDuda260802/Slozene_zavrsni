def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(n, edges):
    result = []  
    i, e = 0, 0  
    parent, rank = [], []

    for node in range(n):
        parent.append(node)
        rank.append(0)

    sorted_edges = sorted(edges.items(), key=lambda item: item[1])
    
    while e < n - 1:
        (u, v), cost = sorted_edges[i]
        i += 1
        x = find(parent, u - 1)
        y = find(parent, v - 1)
        
        if x != y: 
            e += 1
            result.append((u, v, cost))
            union(parent, rank, x, y)

    if e != n - 1:
        return "NEMOGUĆE"
    else:
        return sum(cost for u, v, cost in result)

n, m = map(int, input().split())
edges = {}
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a,b] = c

print(kruskal(n, edges))
