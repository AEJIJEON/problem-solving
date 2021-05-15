def solution(routes):
    # 끝 지점 기준으로 정렬
    routes = sorted(routes, key=lambda x: x[1])
    # 마지막 카메라 위치 초기화
    last_cam = -30000

    count = 0

    for route in routes:
        # 해당 구간이 마지막으로 설치된 카메라에 포착x
        if last_cam < route[0]:
            # 구간 끝 지점에 카메라 설치
            count += 1
            last_cam = route[1]

    return count