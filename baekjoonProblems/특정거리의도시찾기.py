# bfs 알고리즘을 사용하여 도시 X로부터 다른 모든 도시까지의 최단 거리를 계산한다.
# 최단 거리가 정확히 K인 모든 도시들의 번호를 출력한다.

from collections import deque

def bfs(start, graph, distance):
    q = deque([start])
    distance[start] = 0
    while q:
        now = q.popleft()
        for adj in graph[now]:
            if distance[adj] == INF:
                distance[adj] = distance[now] + 1
                q.append(adj)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

INF = int(1e9)
distance = [INF]*(n+1)


bfs(x, graph, distance)

result = [i for i in range(1, n+1) if distance[i] == k]
if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)