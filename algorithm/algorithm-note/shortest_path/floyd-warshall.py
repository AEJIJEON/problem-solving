# O(n^3) shortest paths from all nodes to all nodes
INF = int(1e9)
n, m = 4, 7
# a -> b weight: c about (a, b, c)
edges = [(1, 2, 4), (1, 4, 6), (2, 1, 3), (2, 3, 7), (3, 1, 5), (3, 4, 4), (4, 3, 2)]
distance = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용 0
for i in range(1, n + 1):
    distance[i][i] = 0

for a, b, c in edges:
    distance[a][b] = c

# implementing floye-warshall algorithm
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            distance[i][j] = min(distance[i][k] + distance[k][j], distance[i][j])

print(distance)
