import heapq

def upiti(grad, cesta, opis):
    queue = [(0, cesta, [])]
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == opis:
                return cost, path
            for c, n in grad[node]:
                heapq.heappush(queue, (cost + c, n, path))
    return int(-1), []

def rjesi(n, m, q, grad, opisi):
    results = []
    for a, b in opisi:
        if a == b:
            results.append(-1)
        else:
            cost, path = upiti(grad, a, b)
            results.append(cost)
    return results

def unos():
    n, m, q = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))
    opisi = [tuple(map(int, input().split())) for _ in range(q)]
    return n, m, q, graph, opisi

def main():
    n, m, q, grad, opisi = unos()
    results = rjesi(n, m, q, grad, opisi)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()

    