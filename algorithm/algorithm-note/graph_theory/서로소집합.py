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


v, e = 6, 4
# union 연산
lst = [(1, 4), (2, 3), (2, 4), (5, 6)]
# 부모를 자기 자신으로 초기화
parent = [i for i in range(v + 1)]
for a, b in lst:
    union_parent(parent, a, b)
# 여기서 parent 출력해보면 경로 압축 적용 안된 node 존재함
# 3번 node는 (2,3)에서 한 번만 압축 되므로 parent[3] = 2
# 경로 압축 끝까지 적용 됐는지 확인할 필요 있음
# 답 계산하기 전에 모든 node들에 대해서 find_parent 적용 시키면 될 듯
for i in range(1, v + 1):
    find_parent(parent, i)

for i in range(1, v + 1):
    print(parent[i])
