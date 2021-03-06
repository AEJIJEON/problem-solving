#1:A, 2:B, 3:C라고 하면
# 21(ACC) = 1x3x3 + 3x3 + 3 
# divided by 3: 1x3 + 3 + 1 (remainder: 0) -> C로 들어감, 
# quotient is q - 1 = 1x3 + 3 ...
def solution(n):
    answer = ''
    while n > 0:
        q = n // 3
        r = n % 3

        # 0이면 C로("4"로)      
        if r == 0:
            r = 4
            # 맨 뒤 3을 나눈 quotient 제거 
            q -= 1
        n = q
        # 최 하위 자리부터 채워줌
        answer = str(r) + answer
     
     
    return answer

print(solution(9))