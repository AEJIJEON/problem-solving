# O(ElogV) shortest paths from v1 to all nodes
import heapq

INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstara(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 같다고 놓으면 안 됨
        # distance가 a로 바뀌고 heap에 넣어주었고, 그 후에 이 node에 접근하지 않다가 heap에서 pop되면 distance가 a임
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstara(start)
print(distance)