def solution(name):

    answer = 0
    arr = []
    for i in name:
        arr.append(min(ord(i) - ord("A"), 1 + ord("Z") - ord(i)))
    if "A" not in name:
        return len(name) - 1 + sum(arr)
    i = 0
    print(arr)
    while True:
        answer += arr[i]
        arr[i] = 0
        if sum(arr) == 0:
            break
        left, right = 1, 1
        while arr[i - left] <= 0:
            left += 1
        while arr[i + right] <= 0:
            right += 1

        if left < right:
            answer += left
            i += -left
        # 거리 같을 경우 오른쪽 선택해야 함... 왜지
        else:
            answer += right
            i += right
    return answer


print(solution("JEROAN"))