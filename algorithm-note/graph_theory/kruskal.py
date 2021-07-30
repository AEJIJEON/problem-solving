# O(ElogE) 가장 오래 걸리는 부분이 간선을 정렬하는 작업임
# (서로소 집합 알고리즘의 시간 복잡도는 정렬 알고리즘의 시간 복잡도보다 작으므로 무시!)


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


v, e = 7, 9
edge_input = [
    (1, 2, 29),
    (1, 5, 75),
    (2, 3, 35),
    (2, 6, 34),
    (3, 4, 7),
    (4, 6, 23),
    (4, 7, 13),
    (5, 6, 53),
    (6, 7, 25),
]
parent = [i for i in range(v + 1)]

edges = []
for a, b, cost in edge_input:
    # 비용순으로 정렬 -> 튜플의 첫 번째 원소를 비용으로 설정 중요!
    edges.append((cost, a, b))

# 가장 시간이 오래 걸리는 부분(간선 정렬하는 작업)
edges.sort()
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)