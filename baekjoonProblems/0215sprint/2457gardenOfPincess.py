
import sys
input = sys.stdin.readline

n = int(input())

flowers = [0]*n

result = 0

# 현재 포함시키려는 날짜를 담는 변수 
# 3/1을 포함시키는 것부터 시작할것이므로 3,1로 초기화
now_month, now_day = 3, 1

# input으로 주어지는 꽃들의 정보를 tuple로 담아줌
for i in range(n):
    flowers[i] = tuple(map(int, input().split()))
    
# 꽃이 피는 날짜에 대해 오름차순으로 정렬
flowers.sort()

# 현재 체크할 꽃의 index
i = 0

# 3/1~11/30까지 매일 최소한 하나의 꽃이 필 수 있는지를 나타냄
flag = True

# 현재 포함하려는 날짜가 11/30을 넘어설 때까지 반복문을 돌려줌
while (now_month, now_day) <= (11, 30):

    # 모든 꽃들을 가지고도 매일 최소한 
    # 하나의 꽃을 피울 수 없는 경우
    if i >= n:
        flag = False
        break
    
    # 찾고자하는 꽃이 지는 날짜를 담는 변수
    next_month, next_day = now_month, now_day

    # 현재 체크하고 있는 꽃이 피기 시작하는 날이 우리가 포함하고자 하는 날짜 이전인 경우
    # 꽃이 지는 날이 우리가 포함하고자 하는 날짜 후인 경우
    # 위의 두 가지를 다 만족하는 꽃들 중에서 꽃이 지는 날의 최댓값을 찾아줌
    while i < n and (flowers[i][0], flowers[i][1]) <= (now_month, now_day):
        if (next_month, next_day) < (flowers[i][2], flowers[i][3]):
            next_month, next_day = flowers[i][2], flowers[i][3]
           
        i += 1
        
    # 해당 날짜를 포함시키지 못함 -> 불가능
    if (next_month, next_day) == (now_month, now_day):
        flag = False
        break

    # 다음으로 포함하려는 날짜 update
    now_month, now_day = next_month, next_day
    # 결과값 카운트
    result += 1

print(result if flag else 0)
    
        