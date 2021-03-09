


def solution(arr):
    count = 0

    # min_left와 right_sorted_arr은 두 번째 원소를 확인할 때부터 사용됨
    # 현재 확인하고자 하는 원소의 왼쪽에 있는 숫자들 중에 최솟값 담아줌
    min_left = arr[0]

    # 현재 확인하고자 하는 원소의 오른쪽에 있는 숫자들을 오름차순으로 담은 배열
    # 최솟값은 0 번째 index에 있는 수가 됨
    right_sorted_arr = arr[2:]
    right_sorted_arr.sort()

    for i in range(len(arr)):
        x = arr[i]
        # arr의 첫 번째, 마지막 원소는 항상 possible
        # x를 기준으로 왼쪽, 오른쪽 배열의 최솟값중 적어도 하나가 x보다 큰 경우
        if (
            i == 0
            or i == len(arr) - 1
            or not (min_left < x and right_sorted_arr[0] < x)
        ):
            print("x:", x, min_left, right_sorted_arr)
            count += 1

        min_left = min(min_left, x)

        if i != 0 and i <= len(arr) - 3:
        # remove()는 O(n) -> 시간 초과
        # pop()은 O(1) -> 어떻게 index 찾지?
        right_sorted_arr.pop(right_sorted_arr.index(arr[i + 1]))
        # if 0 < i <= len(arr) - 3 and arr[i + 1] == right_sorted_arr[0]:
        #     right_sorted_arr.popleft()

    return count


print(solution([9, -1, -5]))
