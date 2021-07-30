# X1 X2 ... Xm Xm+1 ... Xn -> k개의 수를 제거
# 숫자가 처음으로 증가하는 부분을 Xm, Xm+1이라고 한다면
# 즉, X1 >= X2 >= X3 ... Xm < Xm+1

# Xm을 제거한 숫자, Xm을 제거하지 않고 다른 수를 제거한 숫자 크기 비교(상위 m자리 비교)

# Xm 제외한 다른 수를 제거한 경우
# 1) Xm 상위에 있는 수를 제거: X1 X2 ...Xk-1 Xk+1... Xm Xm+1 ... Xn : length = n-1
# 2) Xm 하위에 있는 수를 제거: X1 X2 ... Xm Xm+1 ... Xq-1 Xq+1 ... Xn : length = n-1

# Xm을 제거한 경우
# 3) X1 X2 ... Xm-1 Xm+1 ... Xn  : length = n-1

# 1) X1 X2 ... Xk-1 Xk+1  Xk+2 ...   Xm Xm+1 : length = m
# 3) X1 X2 ... Xk-1  Xk   Xk+1 ... Xm-1 Xm+1 : length = m

# Xm을 제거한 숫자 >= 다른 수를 제거한 숫자

from collections import deque


def solution(number, k):
    # stack
    left = [number[0]]
    # queue
    right = deque(list(number[1:]))
    while right and k > 0:
        # 6 5 5 4 1 7(increasing number 발견)
        if left and left[-1] < right[0]:
            # 1 제거
            left.pop()
            k = k - 1
        else:
            left.append(right.popleft())
    result = "".join(map(str, left + list(right)))

    # k 개 제거하기 전에 내림차순으로 만들어진 경우
    # -> 맨 뒤에서 남은 k 개 숫자를 제거
    return result if k == 0 else result[: len(result) - k]


print(solution("4177252841", 4))
print(solution("7777", 3))