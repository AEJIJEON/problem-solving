# O(N*K) -> O((M+K)*logN) 줄일 수 있음
# 리프 노드 개수 N -> h = ceil(log2(N)), 전체 노드 개수 = 2 ** (h + 1) (tree 배열은 index 0 제외하고 index 1부터 시작)
# 입력받은 array는 index 0부터 시작(주의!)
from math import *


def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)
        return tree[node]


def update(node, i, diff, start, end):
    if not (start <= i <= end):
        return
    tree[node] += diff
    if start == end:
        return
    else:
        mid = (start + end) // 2
        update(node * 2, i, diff, start, mid)
        update(node * 2 + 1, i, diff, mid + 1, end)


def query(node, start, end, left, right):
    if left > end or start > right:
        return 0
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return query(node * 2, start, mid, left, right) + query(
        node * 2 + 1, mid + 1, end, left, right
    )


# main
n, m, k = map(int, input().split())

h = ceil(log2(n))
t_size = 2 ** (h + 1)

arr = []
tree = [0] * (t_size)

for _ in range(n):
    arr.append(int(input()))

init(1, 0, n - 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        diff = c - arr[b - 1]
        # arr 값 변경해줘야 함(diff 구할 때 필요함!)
        arr[b - 1] = c
        update(1, b - 1, diff, 0, n - 1)
    elif a == 2:
        print(query(1, 0, n - 1, b - 1, c - 1))
