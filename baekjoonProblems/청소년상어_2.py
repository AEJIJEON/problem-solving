import copy 

# 4x4 공간 만들기
arr = [[None]*4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    # [물고기 번호, 방향] 저장
    for j in range(4):
        arr[i][j] = [data[j*2], data[j*2+1] - 1]

# 8가지 방향으로 이동하기 위한 위치 변화량 
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

# 왼쪽으로 회전
def turn_left(direction):
    return (direction + 1) % 8


# 해당 번호의 물고기의 위치 반환하는 함수
def getPosOfFish(arr, index):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == index:
                return (i,j)
    return None

# 1번부터 16번까지 차례대로 물고기 이동시키는 함수
def moveFishes(arr, now_x, now_y):
    for i in range(1, 17):
        pos = getPosOfFish(arr, i)
        if pos != None:
            x, y = pos[0], pos[1]
            direction = arr[x][y][1]

            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]

                if 0 <= nx < 4 and 0 <= ny < 4:
                    # 청소년 상어가 존재하는 위치가 아닐 경우
                    if nx != now_x or ny != now_y:

                        arr[x][y][1] = direction
                        # 해당 방향에 있는 물고기와 자리 바꿈
                        arr[nx][ny], arr[x][y] = arr[x][y],  arr[nx][ny] 
                        break
                direction = turn_left(direction)

# 상어가 이동할 수 있는 위치들을 반환하는 함수
def getPossOfShark(arr, now_x, now_y):
    poss = []
    direction = arr[now_x][now_y][1]

    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]

        if 0 <= now_x < 4 and 0 <= now_y < 4:
            if arr[now_x][now_y][0] != -1:
                poss.append((now_x, now_y))
    return poss

# 완전 탐색을 수행하기 위한 함수
def dfs(arr, now_x, now_y):
    # 결과값 global로 정의 
    # 모든 단계에서 같은 변수에 대해 update가 가능
    global result 
    global total
    # 각 단계에서 사용되는 arr 값 새로 정의
    # 다음 단계를 위해 dfs 함수를 호출하는 데 사용               
    arr = copy.deepcopy(arr)

    
    # 상어가 먹는 물고기 번호
    num = arr[now_x][now_y][0]

    arr[now_x][now_y][0] = -1

    moveFishes(arr, now_x, now_y)

    poss = getPossOfShark(arr, now_x, now_y)

    # 상어가 이동할 곳이 없는 경우
    if len(poss) == 0:

        # 마지막으로 먹은 물고기 번호 추가        
        result = max(result, total + num)
        return
    # 상어가 이동할 수 있는 모든 경우에 대해
    # dfs 함수 호출
    for next_x, next_y in poss:
        # 원래 위치에 있는 물고기 먹고
        # 다른 위치로 이동
        total += num
        dfs(arr, next_x, next_y)
        # 호출 끝나고 값 되돌려 놓기
        total -= num

# global 변수로 설정
total = 0
result = 0
dfs(arr, 0, 0)
print(result)