from collections import deque

def podijeli_u_timove(n, prijateljstva):
    # inicijaliziramo prazni graf kao dictionary --> key od 1 do n
    graf = {i: [] for i in range(1, n + 1)}

    # dodajemo jedan drugoga na njihove liste prijatelja
    for a, b in prijateljstva:
        graf[a].append(b)
        graf[b].append(a)
    
    tim = {}  
    
    for ucenik in range(1, n + 1):
        if ucenik not in tim:
            tim[ucenik] = 1  
            # inicijaliziramo dvostrani red (BFS)
            queue = deque([ucenik])
            while queue:
                trenutni = queue.popleft()
                for susjed in graf[trenutni]:
                    if susjed not in tim:
                        tim[susjed] = 3 - tim[trenutni]  # Dodijeli ga u suprotni tim
                        queue.append(susjed)
                    elif tim[susjed] == tim[trenutni]:
                        return "NEMA"  # Nije moguće podijeliti, pronađen sukob
    
    return ' '.join(str(tim[i]) for i in range(1, n + 1))


n,m = list(map(int, input().split()))
friends = []
for i in range(m):
    a, b = list(map(int, input().split()))
    friends.append([a,b])

print(podijeli_u_timove(n, friends))
