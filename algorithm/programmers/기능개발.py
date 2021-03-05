import math
def solution(progresses, speeds):

    answer = []
    
    left_days = []

    for i in range(len(progresses)):
        # 완성까지 남은 날짜 계산
        left_days.append(math.ceil((100-progresses[i])/speeds[i]))
    
    i, count = 0, 0
    # 현재 선택된 기능을 배포시킬 때까지 걸린 day
    now = left_days[i]
    while i <= len(left_days) - 1:
        # 오른쪽 기능들 순차적으로 체크
        # 현재 선택된 기능(now)보다 기능 완성이 더 일찍 끝난 경우
        if now >= left_days[i]:
            count += 1
            i += 1
        else:
            answer.append(count)
            count = 0
            now = left_days[i]
    # 마지막 요소는 따로 추가해줌
    answer.append(count)


    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))