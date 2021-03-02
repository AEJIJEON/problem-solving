def solution(dartResult):
    # i+1 번째에 몇 점을 얻는지 기록
    answer = [0] * 3
    exp = {"S": 1, "D": 2, "T": 3}
    # 현재 몇 회차인지 기록(idx+1회)
    idx = 0
    i = 0
    while i < len(dartResult):
        if dartResult[i].isdigit():
            num = dartResult[i]
            # 숫자가 2자리인 경우(10)
            if i + 1 < len(dartResult) and dartResult[i + 1].isdigit():
                num += dartResult[i + 1]
                i += 1
            # 점수 그대로 넣어줌
            answer[idx] = int(num)
        # 1제곱, 2제곱, 3제곱 
        elif dartResult[i] in ["S", "D", "T"]:
            answer[idx] **= exp[dartResult[i]]
        # 이전 점수, 현재 점수 2배씩
        elif dartResult[i] == "*":
            answer[idx] *= 2
            # 2회차 이상인 경우
            if idx > 0:
                answer[idx - 1] *= 2
        # 현재 점수에 -1 곱해줌
        elif dartResult[i] == "#":
            answer[idx] *= -1
        i += 1
        # 다음 character가 숫자인 경우 다음 회차로..
        if i < len(dartResult) and dartResult[i].isdigit():
            idx += 1
    return sum(answer)


print(solution("1S2D*3T"))