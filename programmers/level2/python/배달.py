# 1 ~ 모든 마을까지의 최단 경로 찾기
# 다익스트라 알고리즘 구현
# 최단 경로가 k이하인 마을 개수 count

import heapq

def solution(N, road, K):
    
    graph = [[] for _ in range(N)]
    for a, b, c in road:
        graph[a-1].append((b-1, c))
        graph[b-1].append((a-1, c))
    INF = 1e9
    distances = [INF for _ in range(N)]
    queue = []
    heapq.heappush(queue, (0, 0))
    distances[0] = 0
    
    while queue:
        now, dist = heapq.heappop(queue)
        if dist > distances[now]:
            continue
        for adj in graph[now]:
            cost = dist + adj[1]
            if cost < distances[adj[0]]:
                distances[adj[0]] = cost
                heapq.heappush(queue, (adj[0], cost))
    
    return len([dist for dist in distances if dist <= K])