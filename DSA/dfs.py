def dfs(node, visited, adj, result):
    visited[node] = True
    result.append(node)

    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, adj, result)


def dfsOfGraph(V, adj):
    visited = [False] * V
    result = []
    dfs(0, visited, adj, result)
    return result


V = 5
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]

print("DFS Traversal of the Graph:", dfsOfGraph(V, adj))
