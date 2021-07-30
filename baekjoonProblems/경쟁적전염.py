# queue 자료구조 사용
# 번호가 작은 순서대로 바이러스의 위치와 초와 함께 queue에 넣어준다.
# bfs 탐색 진행
# s초가 넘은 경우 x,y 위치 확인

import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())


def bfs(arr, queue):

    while queue:
        num, sec, _x, _y = queue.popleft()
        if sec == s:
            break
        for i in range(4):
            nx, ny = _x + dx[i], _y + dy[i]
            if 0 <= nx <= n - 1 and 0 <= ny <= n - 1 and arr[nx][ny] == 0:
                arr[nx][ny] = num
                queue.append((num, sec + 1, nx, ny))


queue = []

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            queue.append((board[i][j], 0, i, j))
queue.sort()
queue = deque(queue)

bfs(board, queue)
print(board[x - 1][y - 1])