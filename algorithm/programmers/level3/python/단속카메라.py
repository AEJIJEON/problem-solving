def solution(routes):
    # 구간의 시작 점 기준으로 정렬
    start_order = sorted(routes, key=lambda x: x[0])
    # 구간의 끝 점 기준으로 정렬
    end_order = sorted(routes, key=lambda x: x[1])

    # end_order 배열 pointer
    # i 번째 끝 점에 카메라 설치
    i = 0
    count = 1

    for start in start_order:
        # start 점이 i 번째 끝 점을 벗어난 경우
        if start[0] > end_order[i][1]:
            # 다음 끝 점 index를 찾아줌
            # (아직 포함되지 않은 구간중 가장 start 점이 작은 구간의 끝 점)
            while start[0] > end_order[i][0]:
                i += 1
            count += 1

    return count


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
print(solution([[-2, -1], [1, 2], [-3, 0]]))  # 2
print(
    solution(
        [
            [0, 0],
        ]
    )
)  # 1
print(solution([[0, 1], [0, 1], [1, 2]]))  # 1
print(solution([[0, 1], [2, 3], [4, 5], [6, 7]]))  # 4
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2  실패
print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
print(solution([[-20, 15], [-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2 실패
