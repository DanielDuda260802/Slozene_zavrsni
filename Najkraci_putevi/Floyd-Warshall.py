def FloydWarshall(nodes,edges):
    distance = {(u,v): float('inf') if u != v else 0 for u in nodes for v in nodes}
    for (u,v), weight in edges.items():
          distance[(u,v)] = weight 

    for k in nodes:
        for u in nodes:
              for v in nodes:
                    distance[(u,v)] = min(distance[(u,v)], distance[(u,v)] + distance[(k,v)])
    
    if any(distance[(u,v)] < 0 for u in nodes):
        print('Graph has a negative-weight cycle')

    return distance


nodes = [0,1,2,3,4,5]
edges = {
    (0,1):1,
    (0,2):1.5,
    (0,3):2,
    (1,0):1,
    (1,3):0.5,
    (1,4):2.5,
    (2,0):1.5,
    (2,3):1.5,
    (3,0):2.0,
    (3,1):0.5,
    (3,2):1.5,
    (4,1):2.5,
    (4,5):2.0,
    (5,3):-4.5,
    (5,4):2.5
    }

print(*FloydWarshall(nodes,edges).values())