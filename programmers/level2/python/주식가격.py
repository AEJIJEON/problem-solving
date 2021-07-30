# O(n^2) brute force
def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices) - 1):
            # 떨어지는 지점 발견
            if prices[i] > prices[j]:
                # 떨어지지 않은 기간 계산(index끼리 빼주면 계산됨)
                answer[i] = j - i
                break
        # answer[i] 값 그래도인 경우(떨어지는 지점 존재x)
        if answer[i] == 0:
            # 끝까지 가격이 떨어지지 않았으므로
            # 전체 기간에서 index를 빼줘서 계산
            answer[i] = len(prices) - 1 - i

    return answer


print(solution([1, 2, 3, 2, 3, 1]))
