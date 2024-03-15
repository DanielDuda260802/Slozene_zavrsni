def najveci_otok(matrica):
    def dfs(i,j):
        if i >= 0 and j >= 0 and i < len(matrica) and j < len(matrica[0]) and matrica[i][j] == 1:
            matrica[i][j] = 0
            return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i, j+1) + dfs(i, j-1)
        return 0

    najveci = 0
    for i in range(len(matrica)):
        for j in range(len(matrica[0])):
            if matrica[i][j] == 1:
                najveci = max(najveci, dfs(i,j))
    return najveci

m,n = list(map(int, input().split()))
matrica = []
for i in range(m):
    red = list(map(int, input().split()))
    matrica.append(red)

print(najveci_otok(matrica))