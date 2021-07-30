# 지원자들을 그룹별로 분류한다.
# 예를 들어 “java backend junior pizza 150” 지원자의 경우 다름 아래의 16개의 그룹에 속하게 된다.
# "java	backend	junior	pizza"
# "– backend junior	pizza"
# "java	– junior	pizza	150"
# ...
# " –	–	–	-"

# 딕셔너리 선언, 그룹: [score1, score2, ...] (오름차순 정렬) 형태로 key: value 저장
# 각 쿼리를 key값으로 하여 해당 쿼리에 속해있는 점수들을 담은 배열을 가져와서
# 이분 탐색을 진행하여 X값 이상인 점수의 개수를 센다.
# info 길이: N, query 배열 길이: M
# 시간 복잡도: O(M*logN)

def binary_search_opt(arr, x):
    if x > arr[-1]: 
        return len(arr)
    start = 0
    end = len(arr) - 1
    result = int(1e9)
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= x:
            result = min(mid, result)
            end = mid - 1
        else:
            start = mid + 1
    return result

def solution(info, query):
    group = dict()


    for _info in info:
        l, p, t, so, sc = _info.split(" ")
        
        for i in ['-', l]:
            for j in ['-', p]:
                for k in ['-', t]:
                    for w in ['-', so]:
                        key = i+j+k+w
                        if key not in group:
                            group[key] = [int(sc)]
                        else:
                            group[key].append(int(sc))

    for key in group:
        group[key].sort()
    
    answer = []
    for q in query:
        temp = q.replace(" and ", "").split(" ")
        cond = "".join(temp[:-1])
        score = int(temp[-1])
        if cond not in group:
            answer.append(0)
        else:
            answer.append(len(group[cond]) - binary_search_opt(group[cond], score))
    
    return answer








print(
    solution(
        [
            "java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50",
        ],
        [
            "java and backend and junior and pizza 100",
            "python and frontend and senior and chicken 200",
            "cpp and - and senior and pizza 250",
            "- and backend and senior and - 150",
            "- and - and - and chicken 100",
            "- and - and - and - 150",
        ],
    )
)
