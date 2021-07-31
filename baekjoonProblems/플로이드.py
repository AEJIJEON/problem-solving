# 도시: 그래프의 노드, A -> B로 가는 버스를 사용할 때 필요한 비용이 c라고 하면
# : A -> B로의 가중치 c의 간선
# 모든 노드 -> 모든 노드로 가는 최단 거리를 구해준다.
# 플로이드워셜 알고리즘 사용
INF = int(1e9)
n = int(input())
k = int(input())
distance = [[INF] * n for _ in range(int(n))]
for i in range(n):
    distance[i][i] = 0

for _ in range(k):
    a, b, w = map(int, input().split())
    if distance[a - 1][b - 1] > w:
        distance[a - 1][b - 1] = w
for k in range(n):
    for a in range(n):
        for b in range(n):
            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

for i in range(n):
    print(" ".join(map(str, distance[i])).replace(str(INF), "0"))
