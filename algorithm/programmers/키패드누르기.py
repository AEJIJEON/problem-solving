from collections import deque

INF = int(1e9)
# 키패드 -> graph로
graph = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# num 위치부터 target위치까지 최단경로 return(using dijkstra)
def get_dis(num, target):
    # graph에서 num의 위치를 찾아줌
    x, y = (num - 1) // 3, (num - 1) % 3
    # graph에서의 target 위치를 찾아줌
    t_x, t_y = (target - 1) // 3, (target - 1) % 3

    distance = [[INF] * 3 for _ in range(4)]
    distance[x][y] = 0
    q = deque([(x, y)])
    while q:
        now = q.popleft()
        dist = distance[now[0]][now[1]]
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            # 인덱스 에러 x and 아직 최단경로가 계산이 안 된 경우
            if 0 <= nx <= 3 and 0 <= ny <= 2 and distance[nx][ny] == INF:
                distance[nx][ny] = dist + 1
                q.append((nx, ny))
    print(distance)
    return distance[t_x][t_y]


def solution(numbers, hand):
    result = ""
    # "*" -> 10
    left = 10
    # "#" -> 12
    right = 12

    for num in numbers:
        # "0" -> 11
        if num == 0:
            num = 11
        if num in [1, 4, 7]:
            left = num
            result += "L"
        elif num in [3, 6, 9]:
            right = num
            result += "R"
        else:
            left_d = get_dis(left, num)
            right_d = get_dis(right, num)
            # 왼쪽 손가락이 위치한 곳과 오른쪽 손가락이 위치한 곳으로부터 다음 숫자까지의 거리가 같고
            # 왼손 잡이인 경우
            # 다음 숫자의 위치부터 왼쪽 손가락이 위치한 곳까지가 더 가까운 경우
            if (left_d == right_d and hand == "left") or left_d < right_d:
                left = num
                result += "L"
            else:
                right = num
                result += "R"
        print(left, right, num)
    return result


numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

print(solution(numbers, hand))