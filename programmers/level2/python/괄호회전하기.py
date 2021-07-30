# 완전 탐색, s = 0, 1, ..., len(s) - 1
# s를 왼쪽으로 1칸 회전하는 함수 구현
# 주어진 문자열이 올바른 괄호 문자열인지 확인하는 함수 구현
# 올바른 괄호 문자열인지 확인하는 방법
# stack 선언 후 문자를 stack에 하나씩 넣어주어
# 맨 위 두 개의 문자가 올바른 괄호 문자열일 경우 제거해 줌
# 모든 문자를 stack에 넣어준 후 stack이 빈 경우 올바른 괄호 문자열이 맞음
# O(N^2)

def is_right(s):
    stack = []
    for c in s:
        stack.append(c)
        if len(stack) >= 2 and stack[-2] + stack[-1] in ['()', '[]', '{}']:
            stack.pop()
            stack.pop()
    return True if not stack else False
    
    
def solution(s):
    count = 0
    for _ in range(len(s)):
        s = s[1:] + s[0]
        if is_right(s):
            count += 1
    return count