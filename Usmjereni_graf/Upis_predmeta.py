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

n, m = list(map(int, input().split()))

for i in range(m):
    x, y = input().split()
    graph[x].append(y)
    if x not in visited:
        visited[x] = False
    if y not in visited:
        visited[y] = False

for vertex in list(visited):
    dfs(vertex)

output.reverse()
print(output)
