def region(grid):

    def dfs(i,j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 'O':
            grid[i][j] = 'T'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1),
            dfs(i, j - 1) 

    # Pozivaj DFS samo na rubovima matrice
    for i in range(len(grid)):
        dfs(i, 0)  # Lijevi rub
        dfs(i, len(grid[0]) - 1)  # Desni rub

    for j in range(len(grid[0])):
        dfs(0, j)  # Gornji rub
        dfs(len(grid) - 1, j)  # Donji rub

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                grid[i][j] = 'X'
            elif grid[i][j] == 'T':
                grid[i][j] = 'O'

# Primjer 1
grid = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]
region(grid)
for row in grid:
    print(' '.join(row))    

# Primjer 2
grid2 = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'O', 'X', 'X', 'O'],
    ['X', 'X', 'X', 'X', 'X', 'O', 'O'],
    ['X', 'X', 'O', 'X', 'X', 'O', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'O'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X']
]
region(grid2)
for row in grid2:
    print(' '.join(row))



