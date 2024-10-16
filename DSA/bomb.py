def maxDetonatedBombs(bombs):
    n = len(bombs)
    graph = [[] for _ in range(n)]

    for i in range(n):
        x1, y1, r1 = bombs[i]
        for j in range(n):
            if i != j:
                x2, y2, _ = bombs[j]
                dist_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if dist_squared <= r1**2:
                    graph[i].append(j)

    def dfs(bomb, visited):
        count = 1
        visited[bomb] = True
        for neighbor in graph[bomb]:
            if not visited[neighbor]:
                count += dfs(neighbor, visited)
        return count

    max_bombs = 0
    for i in range(n):
        visited = [False] * n  
        max_bombs = max(max_bombs, dfs(i, visited))

    return max_bombs



bombs1 = [[2, 1, 3], [6, 1, 4]]
print(maxDetonatedBombs(bombs1))

bombs2 = [[1, 1, 5], [10, 10, 5]]
print(maxDetonatedBombs(bombs2))

bombs3 = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]
print(maxDetonatedBombs(bombs3))
