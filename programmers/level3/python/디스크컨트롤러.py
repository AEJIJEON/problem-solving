import heapq
import copy


def solution(jobs):
    result = 0
    # (소요 시간, 요청 시점) tuples 담아줌
    time_q = [(j, i) for i, j in jobs]
    temp_time_q = []
    # 제일 먼저 처리되는 작업의 요청 시점
    now_time = min(time_q, key=lambda x: (x[1], x[0]))[1]

    heapq.heapify(time_q)

    # 처리되지 않은 작업이 존재할 경우
    while time_q:
        # 현재 처리하려고 하는 job을 담을 변수
        get_job = None
        while time_q:
            # 현재 시간보다 이후에 요청된 작업인 경우(이전에 요청된 작업을 찾아줘야 함)
            # 또는 현재 처리할 job을 발견한 경우
            if get_job or time_q[0][1] > now_time:
                temp_time_q.append(heapq.heappop(time_q))
            # 현재 시간보다 이전에 요청된 작업인 경우
            # -> 소요 시간이 제일 작은 job을 pop
            else:
                get_job = heapq.heappop(time_q)

        # 현재 시간보다 이전에 요청된 작업이 없는 경우
        if not get_job:
            # 먼저 요청이 들어온 작업을 선택해 줌
            # 같은 시간에 요청이 들어왔을 경우에는 소요 시간이 제일 작은 job을 선택
            get_job = min(temp_time_q, key=lambda x: (x[1], x[0]))
            # 제거
            temp_time_q.remove(get_job)
            # 현재 시간을 작업이 끝난 시간으로 설정
            now_time = get_job[1] + get_job[0]
        else:
            # 현재 시간을 작업이 끝난 시간으로 설정
            now_time += get_job[0]
        # 작업의 요청부터 종료까지 걸린 시간을 더해줌
        result += now_time - get_job[1]
        # 다음 계산을 위해 time_q에 temp_time_q를 옮겨줌
        time_q = copy.deepcopy(temp_time_q)
        temp_time_q = []
        heapq.heapify(time_q)
        # print(now_time, result)
    # 작업의 요청부터 종료까지 걸린 시간의 평균
    return result // len(jobs)


print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]))
print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]))
print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[0, 1]]))
print(solution([[1000, 1000]]))
print(solution([[0, 1], [0, 1], [0, 1]]))
print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]))
print(solution([[0, 1], [1000, 1000]]))
print(solution([[100, 100], [1000, 1000]]))
print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]))
print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]))
