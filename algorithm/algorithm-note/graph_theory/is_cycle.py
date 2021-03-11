# undirected graph에서만 적용!!!!!!!!!!!!!!!!!!!!!


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


v, e = 3, 3
edges = [(1, 2), (1, 3), (2, 3)]
parent = [i for i in range(v + 1)]

cycle = False

for a, b in edges:
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

print(cycle)
