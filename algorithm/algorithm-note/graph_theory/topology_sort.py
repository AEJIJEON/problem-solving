# O(V+E) 노드와 간선을 모두 확인
from collections import deque

v, e = 7, 8
indegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]
edges = [(1, 2), (1, 5), (2, 3), (2, 6), (3, 4), (4, 7), (5, 6), (6, 4)]
for a, b in edges:
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    queue = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        now = queue.popleft()
        print(now)
        for adj in graph[now]:
            indegree[adj] -= 1
            if indegree[adj] == 0:
                queue.append(adj)


topology_sort()
