def find(parent,i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])
    
def union(parent, x,y):
    parent[find(parent,y)] = find(parent,x)

def minimum_component(broj_gradova,ceste):
    parent = [i for i in range(broj_gradova)]
    nove_ceste = []
    components = broj_gradova

    for x,y in ceste:
        xroot = find(parent, x-1)
        yroot = find(parent, y-1)
        if xroot != yroot:
            union(parent, xroot, yroot)
            components -= 1

    representer = {find(parent, i): i for i in range(n)}
    rep_list = list(representer.keys())

    for i in range(1, len(rep_list)):
        nove_ceste.append((representer[rep_list[i - 1]] + 1, representer[rep_list[i]] + 1))

    print(components - 1)
    print(*nove_ceste)

n,m = list(map(int, input().split()))
gradovi = []

for i in range(n):
    gradovi.append(i+1)

ceste = []
for i in range(m):
    a,b = list(map(int, input().split()))
    ceste.append((a,b))

minimum_component(n,ceste)