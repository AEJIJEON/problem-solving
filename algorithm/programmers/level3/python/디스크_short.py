# wow.............대박이다 이 코드.. heap/stack/queue 구현 너무 어렵다..
import heapq
from collections import deque


def solution(jobs):
    # (소요 시간, 요청 시점) tuples, 요청 시점 기준으로 오름차순 정렬
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    now_time, result = 0, 0
    while q:
        take_time, require_time = heapq.heappop(q)
        now_time = max(now_time + take_time, require_time + take_time)
        result += now_time - require_time

        while len(tasks) > 0 and tasks[0][1] <= now_time:
            # tasks에 있는 작업들 중 요청 시점이 현재 시간보다 이전인 작업들을 다 넣어줌
            heapq.heappush(q, tasks.popleft())

        # 처리되지 않은 작업들이 있지만 전부 다 요청 시점이 현재 시간보다 이후인 작업들인 경우
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())

    return result // len(jobs)