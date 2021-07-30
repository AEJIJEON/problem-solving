# 노드 nC2개 -> n*(n-1)/2
# 간선 비용: min(|xA-xB|, |yA-yB|, |zA-zB|)
# => x축, y축, z축에서의 인접한 노드들의 간선만 고려

# (11 -15 -15) (14 -5 -15) (-1 -1 -5) (10 -4 -1) (19 -4 19)
# 11 14 -1 10 19 -> -1 10 11 14 19 -> 11 1 3 5

# proof
# T라는 mst에 x축에서 인접하지 않은 노드 A, B를 연결하는 간선이 있다고 가정, Ax Cx Bx
# Ax ~ Bx -> Ax ~ Cx, Cx ~ Bx로 대체 -> 총 비용 변화 x, 간선 total n개, cycle 발생
# cycle 이루는 간선들 중 하나 지우면 T보다 비용이 더 작은 mst가 만들어 짐 -> T가 mst라는 가정에 모순

import sys

input = sys.stdin.readline

# find 연산 수행
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# union 연산 수행
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n = int(input())

parent = [0] * n
for i in range(n):
    parent[i] = i

x, y, z = [], [], []

for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

edges = []

# x, y, z 축에서 인접한 node들의 간선 추가
for i in range(n - 1):
    edges.append((abs(x[i][0] - x[i + 1][0]), x[i][1], x[i + 1][1]))
    edges.append((abs(y[i][0] - y[i + 1][0]), y[i][1], y[i + 1][1]))
    edges.append((abs(z[i][0] - z[i + 1][0]), z[i][1], z[i + 1][1]))

# 3*(n-1)개 간선들을 정렬
edges.sort()

result = 0

for edge in edges:
    cost, a, b = edge

    # 두 node가 포함된 집합이 서로소 집합인 경우
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        # MST에 포함
        result += cost

print(result)

# 시간 복잡도: O(nlogn)