import sys
from collections import deque
INF = int(1e9)
n, m, fuel = map(int, input().split())

board = [[1]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    data = list(map(int, input().split()))
    for j in range(1, n+1):
        board[i][j] = data[j-1]


x, y = map(int, input().split())

peoples = []

for _ in range(m):
    peoples.append(tuple(map(int, input().split())))
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# bfs를 이용한 최단거리 구하기
def getDistance(start):
    q = deque()
    
    x, y = start[0], start[1]
    distances = [[INF]*(n+1) for _ in range(n+1)]
    q.append((x,y))
    distances[x][y] = 0
   
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 밖으로 안 벗어나고 벽이 아닌 경우
            if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 1:
                # 방문하지 않은 node
                if distances[nx][ny] == INF:
                    distances[nx][ny] = distances[x][y] + 1
                    q.append((nx, ny))
    
    return distances

result = -1
while True:
    # 모든 손님 이동 완료
    if not peoples:
        result = fuel
        break
    distances = getDistance((x,y))
    
    min_value = INF
    for p_x, p_y, p_z, p_w in peoples:
        min_value = min(min_value, distances[p_x][p_y])
    # 벽때문에? 이동 불가능 
    
    if min_value == INF:
        break

    # 최단거리 위치한 사람들 위치 담음
    min_peoples = []
    for p_x, p_y, p_z, p_w in peoples:
        if distances[p_x][p_y] == min_value:
            min_peoples.append((p_x, p_y))
    # 여러명 이상일 경우 행 번호가 작은 승객 
    # -> (행 번호 같은 경우) 열 번호가 작은 승객을 태움
    # 즉, 위치 (x1, x2)들의 lexicographical order로 체크
    # (now_x, now_y)는 태울 승객 위치
    now_x, now_y = min(min_peoples)
    
    # 남은 연료 계산
    fuel -=  min_value
    if fuel < 0:
        break
    # 승객 위치에서 목적지까지 최단거리 구하기 위해
    distances = getDistance((now_x, now_y))
    # print(distances)
    # 도착지 위치
    d_x, d_y = 0, 0

    for p_x, p_y, p_z, p_w in peoples:
        if (now_x, now_y) == (p_x, p_y):
            d_x, d_y = p_z, p_w
    
    # 승객 위치에서 목적지까지 최단거리 계산
    need_fuel = distances[d_x][d_y]
    
    # 벽 때문에 목적지로 이동할 수 없음
    if need_fuel == INF:
        break
    # 남은 연료 계산
    fuel -= need_fuel

    
    if fuel < 0:
        break
    # 연료 넣어주기
    fuel += need_fuel*2

    # 이동한 사람 제거
    peoples.remove((now_x, now_y, d_x, d_y))

    # 택시 위치 이동
    x, y = d_x, d_y

print(result)


