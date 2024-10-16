def canFinish(numCourses, prerequisites):
    adj = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        adj[prereq].append(course)

    visited = [0] * numCourses

    def dfs(node):
        if visited[node] == -1:
            return False
        if visited[node] == 1:
            return True

        visited[node] = -1
        for neighbor in adj[node]:
            if not dfs(neighbor):
                return False

        visited[node] = 1
        return True

    for i in range(numCourses):
        if visited[i] == 0:
            if not dfs(i):
                return False

    return True


numCourses1 = 2
prerequisites1 = [[1, 0]]
print(canFinish(numCourses1, prerequisites1))

numCourses2 = 2
prerequisites2 = [[1, 0], [0, 1]]
print(canFinish(numCourses2, prerequisites2))
