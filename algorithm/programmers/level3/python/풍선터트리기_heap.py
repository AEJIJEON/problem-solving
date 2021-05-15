import heapq


def solution(arr):
    count = 0

    # min_left와 right_sorted_arr은 두 번째 원소를 확인할 때부터 사용됨
    # 현재 확인하고자 하는 원소의 왼쪽에 있는 숫자들 중에 최솟값 담아줌
    min_left = arr[0]

    # 현재 확인하고자 하는 원소의 오른쪽에 있는 숫자들을 오름차순으로 담은 배열
    # 최솟값은 0 번째 index에 있는 수가 됨
    right_arr = [(num, i) for i, num in enumerate(arr)]
    # heapify() -> O(n)
    heapq.heapify(right_arr)

    # arr의 첫 번째, 마지막 원소는 항상 possible
    count = 2
    for i in range(1, len(arr) - 1):
        x = arr[i]
        while i >= right_arr[0][1]:
            heapq.heappop(right_arr)
        # x를 기준으로 왼쪽, 오른쪽 배열의 최솟값중 적어도 하나가 x보다 큰 경우
        if not (min_left < x and right_arr[0][0] < x):

            count += 1

        min_left = min(min_left, x)

    return count


print(solution([9, -1, -5]))
