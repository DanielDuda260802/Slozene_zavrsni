# Nakraći put 

## Bellman-Fordov algoritam 

- Na početku se postavi udaljenost od inicijalnog vrha, a sve druge budu beskonačno
- Nakon toga se reduciraju udaljenosti pronalaženjem bridova koji smanjuju vrijednosti

### Način rješavanja:
1) Prebacimo matricu u dictionary bridova koji kao ključ ima par čvorova npr. (0,1), a vrijednost mu je težina tog brida
2) Stvorimo dictionary koji predstavlja udaljenosti od početnog čvora do svih drugih čvorova sa beskonačnim vrijednostima ( od izvornog do izvornog postavimo na 0)
3) Stvorimo dictionary paths za puteve od izvornog do svakog drugog čvora kao prazne liste ( put do izvorisnog je [source])
4) Prolazimo čitavim grafom range(nodes-1) i za svaki (u,v):weight odnosno svaki brid i njegovu težinu iz dictionary-a edges provjeravamo je li udaljenost od čvora do izvorišnog za u + težina manja od udaljenosti do čvora v i ako je ta udaljenost od v postaje težina + udaljesnost do čvora u. Također u paths do v dodajemo paths[u] + [v]

```python
    def matrix_to_edges_dict(matrix):
        edges = {}
        for i, row in enumerate(matrix):
            for j, weight in enumerate(row):
                if weight != 0:  
                    edges[(i+1, j+1)] = weight 
        return edges
```

```python
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
```

## Dijkstrin algoritam
- Učinkovitiji od Bellman-Ford algoritma, ali ne smije biti negativnih ciklusa u grafu
- procesuira svaki brid samo jednom

### Način rješavanja:
source - izvorni čvor
w_uv - težina(distance) između čvorova u i v
d_v - duljina puta od source to v
Pernament nodes: najkraće duljine puteva
Temporary nodes: gornje granice

1) Dodjelimo udaljenost od izvorišnog do svih čvorova na beskonačno, a do izvorišnog na 0
2) Označimo sve čvorove kao temporary
3) Odaberemo temporary čvor u sa najmanjom duljinom puta (path length) i označimo ga kao pernament
4) udaljenost d_v je minimalna udaljenost od d_v do d_u + w_uv za svaki temporary čvor v koji je susjedni u
5) ako više ne postoje temporary čvorovi, idemo na ponovno na 2. korak

```python
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
```