def bfsOfGraph(V, adj):
    visited = [False] * V
    queue = [0]
    visited[0] = True
    result = []

    while queue:
        node = queue.pop(0)
        result.append(node)

        for neighbor in adj[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

    return result


V = 5
adj = [[1, 2, 3], [], [], [], []]

print("BFS Traversal of the Graph:", bfsOfGraph(V, adj))
