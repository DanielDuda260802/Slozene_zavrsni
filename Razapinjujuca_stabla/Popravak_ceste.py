def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, x, y):
    parent[find(parent,y)] = find(parent,x)

def Kruskal(n, edges):
    results = []
    parent = []
    i, e = 0, 0

    sorted_edges = sorted(edges.items(), key=lambda item: item[1])

    for node in range(n):
        parent.append(node)
    
    while e < n-1:
        (u,v), weight = sorted_edges[i]
        i += 1
        x = find(parent,u-1)
        y = find(parent,v-1)

        if x != y:
            e += 1
            results.append(((u,v), weight))
            union(parent, x, y)
    
    if e != n - 1:
        return "NEMOGUĆE"
    else:
        return sum(cost for (u, v), cost in results)


n,m = list(map(int, input().split()))

gradovi = []
for i in range(n):
    gradovi.append(i+1)

ceste = {}
for i in range(m):
    a,b,c = list(map(int, input().split()))
    ceste[(a,b)] = c

print(Kruskal(n, ceste))