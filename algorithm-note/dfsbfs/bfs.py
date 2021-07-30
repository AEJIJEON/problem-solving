# O(E+V)
from collections import deque

graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False] * 9


def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        now = queue.popleft()
        print(now)
        for adj in graph[now]:
            if not visited[adj]:
                queue.append(adj)
                visited[adj] = True


bfs(graph, 1, visited)
