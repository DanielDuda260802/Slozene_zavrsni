"""
Ulazni Podaci:

Prvi red sadrži tri cijela broja: n (broj gradova), m (broj cesta) i q (broj upita za najkraći put).
Sljedećih m redova sadrži opise cesta: svaki red sadrži tri cijela broja a, b i c koji predstavljaju da postoji cesta između gradova a i b s troškom 
(ili duljinom) c. Sljedećih q redova sadrži parove gradova za koje se traži najkraći put.
Zadatak:

Za svaki upit (par gradova) izračunajte najkraći put od prvog do drugog grada. Potrebno je odrediti minimalni trošak putovanja između dva grada, 
koristeći ceste koje povezuju gradove.

Izlazni Podaci:

Za svaki upit, ispišite najmanji trošak putovanja između dva grada. Ako između dva grada ne postoji put, ispišite -1.

INPUT:
10 20 10
2 4 5
2 7 8
1 2 3
9 10 6
8 9 6
8 10 9
1 6 6
2 5 7
6 9 7
3 4 9
4 8 2
5 6 2
7 8 5
5 9 8
7 9 7
4 6 8
2 3 6
6 7 10
4 9 3
4 5 4
3 2
9 8
10 4
5 9
6 10
8 9
4 10
1 2
10 2
6 10

OUTPUT:
6
5
9
7
13
5
9
3
14
13
"""
def matrix_to_edges(matrix):
    edges = {}
    for i, row in enumerate(matrix):
        edge_key = (row[0],row[1])
        if edge_key not in edges:
            edges[row[0],row[1]] = row[2]
        elif edges[edge_key] > row[2]:
            edges[edge_key] = row[2]
    return edges

def upiti(q):
    upiti_lista_izvor = []
    upiti_lista_kraj = []
    for i in range(q):
        prvi, drugi = list(map(int,input().split()))
        upiti_lista_izvor.append(prvi)
        upiti_lista_kraj.append(drugi)
    return upiti_lista_izvor, upiti_lista_kraj

def dijkstrin(nodes, edges, prvi, drugi):
    path_lengths = {v: float('inf') for v in nodes}
    path_lengths[prvi] = 0

    adjacent_nodes = {v: {} for v in nodes}
    for (u,v), weight in edges.items():
        adjacent_nodes[u][v] = weight
        adjacent_nodes[v][u] = weight

    temporary_nodes = [v for v in nodes]
    while len(temporary_nodes) > 0:
        upper_bounds = {v: path_lengths[v] for v in temporary_nodes}
        u = min(upper_bounds, key=upper_bounds.get)

        temporary_nodes.remove(u)

        for v, weight in adjacent_nodes[u].items():
            path_lengths[v] = min(path_lengths[v],path_lengths[u] + weight)
    return path_lengths[drugi]

n, m, q = list(map(int, input().split()))
nodes = []
for i in range(n):
    nodes.append(i+1)

matrix = []
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)


edges = matrix_to_edges(matrix)
lista_upita_izvora, lista_upita_kraja = upiti(q)
rj = []
for i in range(len(lista_upita_izvora)):
    rj.append(dijkstrin(nodes, edges, lista_upita_izvora[i], lista_upita_kraja[i]))

print(rj)


