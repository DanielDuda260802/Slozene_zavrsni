""" TREBA UPOTPUNIT """

def Floyd_Warshall(n,edges):
    distance = {(u,v): float('inf') if u!=v else 0 for u in n for v in n}
    for (u,v), weight in edges.items():
        distance[(u,v)] = weight

    for k in n:
        for u in n:
            for v in n:
                distance[(u,v)] = min(distance[(u,v)], distance[(u,v)] + distance[k,v]) 

    if any(distance[(u,v)] < 0 for u in n):
        print('Graph has a negative cycles')

    return distance

n,m  = list(map(int,input().split()))
nodes = []
for i in range(n):
    nodes.append(i+1)
edges = {}
for i in range(m):
    a,b,c = list(map(int,input().split()))
    edges[(a,b)] = c

print(Floyd_Warshall(nodes,edges))