def solution(skill, skill_trees):
    answer = 0
    d = {}
    for i in range(len(skill)):
        # 순서대로 0, 1, ... 숫자 부여
        d[skill[i]] = i

    for skill_tree in skill_trees:
        s = ""
        # skill에 포함된 문자들 있을 시 s에 추가
        for c in skill_tree:
            if c in skill:
                s += str(d[c])
        # 순서 동일할 경우
        if list(map(int, s)) == list(range(0, len(s))):
            print(s)
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
d