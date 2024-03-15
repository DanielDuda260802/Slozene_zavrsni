"""
Postoji n gradova i m zračnih veza između njih. Vaš zadatak je odrediti duljinu najkraće rute od grada Rijeke do svakog grada u zadanoj listi. 

ULAZNI PODACI

U prvom retku za unos nalaze se dva cijela broja n i m: broj gradova i letova. Gradovi su označeni brojevima 1,2,...,n, a grad 1 je Rijeka.

Nakon toga slijedi m redaka koji opisuju letove. Svaki red ima tri cijela broja: a,b i c. Let počinje u gradu a, završava u gradu b, a duljina mu je c.
Svaki let je let u jednom smjeru. Možete pretpostaviti da je moguće putovati iz Rijeke u sve ostale gradove.

ISPIS

Ispiši n cijelih brojeva: duljine najkraće rute od Rijeke do 1,...,n.

1. Unos:
3 4
1 2 6
1 3 2
3 2 3
1 3 4

Ispis:
0 5 2
"""

def edges_from_input(matrix):
    edges = {}
    for i,row in enumerate(matrix):
        edge_key = (row[0], row[1])
        if edge_key not in edges:
            edges[edge_key] = row[2]
        else:
            if edges[edge_key] > row[2]:
                edges[edge_key] = row[2]
    return edges

def dijkstrin(nodes, edges, source):
    paths_lengths = {v: float('inf') for v in nodes}
    paths_lengths[source] = 0

    adjacent_nodes = {v: {} for v in nodes}
    for (u,v), weight in edges.items():
        adjacent_nodes[u][v] = weight

    temporary_nodes = [v for v in nodes]
    while len(temporary_nodes) > 0:
        upper_boands = {v: paths_lengths[v] for v in temporary_nodes} 
        u = min(upper_boands, key=upper_boands.get)

        temporary_nodes.remove(u)

        for v, weight in adjacent_nodes[u].items():
            paths_lengths[v] = min(paths_lengths[v], paths_lengths[u]+weight)
    
    return paths_lengths

n, m = list(map(int, input().split()))
source = 1
nodes = []
for i in range(n):
    nodes.append(i+1)

matrix = []
for i in range(m):
    row = list(map(int,input().split()))
    matrix.append(row)


edges = edges_from_input(matrix)
paths_length = dijkstrin(nodes, edges, source)

for value in paths_length.values():
    print(value)
