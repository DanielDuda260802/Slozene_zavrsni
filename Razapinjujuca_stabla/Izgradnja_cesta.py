"""
 NIJE DOBRO JER NIJE KRUSKAL ALGORITAM... 
 - treba samo dodati bridove na one već postojeće, a ne s kruskalom pronaći najmanji put
"""

def find(parent, i):
    if parent[i] == i:
        return i
    else: 
        return find(parent, parent[i])
    
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[yroot] < rank[xroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def Kruskal(gradovi, povezani_gradovi):
    result = []
    i, e = 0, 0
    parent, rank = [], []
    sorted_edges = sorted(povezani_gradovi.items(), key=lambda item: item[1])
    print(sorted_edges)

    for i in range(gradovi):
        parent.append(i+1)
        rank.append(0)

    while e < gradovi-1:
        (u,v), weight = sorted_edges[i]
        x = find(parent,u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append(((u,v),weight))
            union(parent,rank,x,y)

    return result, e

gradovi, ceste = list(map(int, input().split()))

povezani_gradovi = {}
for i in range(ceste):
    a,b = list(map(int,input().split()))
    povezani_gradovi[(a, b)] = 1

ispis, broj = Kruskal(gradovi, povezani_gradovi)

print(broj)
for (u,v), weight in ispis:
    print(f"({u} {v}")
