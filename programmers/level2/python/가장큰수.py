def solution(numbers):
    numbers = list(map(str, numbers))
    # 각 string을 3 번 이어 붙여서 비교(lengh >= 3으로 만들어 줌)
    numbers.sort(key=lambda x: x * 3, reverse=True)
    # '0000'의 경우 '0'으로 처리
    return str(int("".join(numbers)))
