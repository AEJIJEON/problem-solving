from collections import deque


def solution(priorities, location):
    result = 1
    q = deque()
    for i in range(len(priorities)):
        q.append((i, priorities[i]))
    while True:
        inx, prio = q.popleft()
        if prio >= max(q, key=lambda x: x[1])[1]:
            if inx == location:
                break
            result += 1
        else:
            q.append((inx, prio))

    return result