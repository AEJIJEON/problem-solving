# 완전탐색
# 가로 길이 >= 세로 길이
# total = brown + yello
# 3 <= 세로 길이 <= floor(sqrt(total))
#  가로 길이 = total / 세로 길이 
# 갈색 격자 수 = 2 * w + 2 * (h - 2)
# 노란색 격자 수 = total - 갈색 격자 수
# return [w, h] if 갈색 격자 수 == brown and 노란색 격자 수 == yello

import math

def solution(brown, yellow):
    total = brown + yellow
    for h in range(3, math.floor(math.sqrt(total)) + 1):
        if total % h != 0:
            continue
        w = total // h

        brown_num = 2 * w + 2 * (h - 2)
        yello_num = total - brown_num

        if brown_num == brown and yello_num == yellow:
            return [w, h]



# test
print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))