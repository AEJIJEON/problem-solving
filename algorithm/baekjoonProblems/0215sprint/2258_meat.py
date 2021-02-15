# greedy 유형.. not binary search
import sys
input = sys.stdin.readline

n, need = map(int, input().split())

# 입력받은 고기들 (무게, 가격)
array = [0]*n 

for i in range(n):
    array[i] = tuple(map(int, input().split()))

# 가격에 대해 오름차순, 같은 경우 무게에 대해 내림차순으로 정렬
array.sort(key = lambda x: (x[1], -x[0]))

# 싼 가격의 덩어리 무게부터 다 더해감
weight = 0

# pay = int(1e9)로 설정하면 문제에서 주어지는 무게의 총 합보다 작은 값으로 설정되어 
# min값을 구할 수 없게 됨 -> int(1e10) or sys.maxmize
pay = sys.maxsize
same = 0
flag = False
for i in range(n):
    weight += array[i][0]

    # 같은 고기 가격을 가지는 덩어리들이 계산되는 경우
    if i >= 1 and array[i][1] == array[i-1][1]:
        # 같은 고기 가격을 가지는 덩어리들의 무게가 몇 번 더해졌는지(현재 계산되는 덩어리는 제외)
        same += array[i][1]
    else:
        same = 0
    
    if weight >= need:
        # 같은 고기 가격의 덩어리들이 동시에 계산되는 경우를 고려하기 위해
        # pay값을 다음과 같이 update시켜줌
        pay = min(pay, array[i][1] + same)
        flag = True

print(pay if flag else -1)
