import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 각 램프마다 연결되어있는 스위치 개수 담음
count = [0]*(m+1)

switchs = []

for i in range(n):
    switchs.append(list(map(int, input().split()))[1:])
    for lamp in switchs[i]:
        count[lamp] += 1


# 모든 램프가 최소한 1개 이상의 스위치와 연결되어 있는지 체크
def check_right(count):
    check = True
    for i in range(1, m+1):
        if count[i] == 0:
            check = False
            break
    return check

flag = False

for i in range(n):
    # i-1 번째 스위치를 제거하는 경우 
    for lamp in switchs[i]:
        count[lamp] -= 1

    if check_right(count):
        flag = True
        break
    # i-1 번째 스위치를 다시 연결
    for lamp in switchs[i]:
        count[lamp] += 1

print(1 if flag else 0)