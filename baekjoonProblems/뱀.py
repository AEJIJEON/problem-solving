# 자료구조 queue 사용
# 머리를 위치시킬 위치 가져와서 벽 or 몸과 부딪히는 지 체크
# 종료되지 않는다면 queue에 위치를 넣어줌
# 그 다음 사과가 있는지 체크 -> 사과가 있다면 그대로 진행, 없다면 queue에서 pop(꼬리가 위치한 칸을 비워줌)

from collections import deque

def turn(d, dir):
    if dir == "L":
        return d - 1 if d - 1 >= 0 else 3
    elif dir == "D":
        return d + 1 if d + 1 <= 3 else 0

n = int(input())
k = int(input())

board = [[0]*n for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

pos_queue = deque([(0, 0)])
change_dir = deque()
for _ in range(int(input())):
    x, c = input().split()
    change_dir.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

time = 1
d = 0

while True:
    nx, ny = pos_queue[-1][0] + dx[d], pos_queue[-1][1] + dy[d]
    if not (0 <= nx <= n-1 and 0 <= ny <= n-1 and (nx, ny) not in pos_queue):
        break
    
    # 몸길이를 늘려 머리를 다음칸에 위치시킴
    pos_queue.append((nx, ny))
    # 사과가 있는 경우 사과를 칸에서 제거
    if board[nx][ny] == 1:
        board[nx][ny] = 0
    # 사과가 없는 경우 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌
    else:
        pos_queue.popleft()
    if change_dir and time == change_dir[0][0]:
        d = turn(d, change_dir.popleft()[1])
    time += 1
print(time)


