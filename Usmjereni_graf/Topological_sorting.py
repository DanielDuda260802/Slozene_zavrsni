from collections import defaultdict

def dfs(vertex):
    if not visited[vertex]:  
        visited[vertex] = True  
        for neighbor in graph[vertex]: 
            dfs(neighbor)
        output.append(vertex)  

graph = defaultdict(list)
visited = {} 
output = []  

n = 6
m = 5
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F')]

for x, y in edges:
    graph[x].append(y)
    visited[x] = False
    visited[y] = False


for vertex in visited:
    dfs(vertex)

output.reverse()
print(output)
