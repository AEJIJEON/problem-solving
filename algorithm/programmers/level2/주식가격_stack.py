# using stack -> O(n)
def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i, price in enumerate(prices):
        # 가격이 떨어지는 구간 발견 -> stack에 담
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        # stack에는 가격이 증가하는 순서대로
        # index들로 담아줌
        # index를 담아주어야 index 값 차이를 가지고 시간 계산할 수 있게 됨
        stack.append(i)

    # for문 다 돌고 Stack에 남아있는 값 -> 끝까지 가격이 떨어지지 않은 경우
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer


print(solution([1, 2, 3, 2, 3, 1]))