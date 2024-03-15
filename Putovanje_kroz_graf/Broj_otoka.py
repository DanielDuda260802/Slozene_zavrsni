def broj_otoka(matrica):
    def dfs(i,j):
        if i < 0 or j < 0 or i >= len(matrica) or j >= len(matrica[0]) or matrica[i][j] == 0:
            return
        matrica[i][j] = 0
        dfs(i, j+1)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i-1,j)

    count = 0
    for i in range(len(matrica)):
        for j in range(len(matrica[0])):
            if matrica[i][j] == 1:
                dfs(i,j)
                count += 1
    return count


m,n = list(map(int, input().split()))
matrica = []
for i in range(m):
    red = list(map(int, input().split()))
    matrica.append(red)

print(broj_otoka(matrica))
