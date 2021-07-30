import copy

def is_possible(structure):
    for elem in structure:
        x, y, a = elem
        # 기둥
        if a == 0:
            # not (바닥 위 or 다른 기둥 위 or 바로 왼쪽에 보 or 바로 오른쪽에 보)
            if not (y == 0 or [x, y-1, 0] in structure or [x-1, y, 1] in structure or [x, y, 1] in structure):
                return False
        # 보
        else:
            # not (왼쪽 끝 부분이 기둥 위 or 오른쪽 끝 부분이 기둥 위 or 양쪽 끝 부분이 다른 보와 동시에 연결)
            if not ([x, y-1, 0] in structure or [x+1, y-1, 0] in structure or ([x-1, y, 1] in structure and [x+1, y, 1] in structure)):
                return False
    return True

def solution(n, build_frame):
    result = []
    
    for elem in build_frame:
        x, y, a, b = elem
        # 삭제
        if b == 0:
            result.remove([x, y, a])
            if not is_possible(result):
                result.append([x, y, a])
        # 추가
        else:
            result.append([x, y, a])
            if not is_possible(result):
                result.remove([x, y, a])
    result.sort()
    return result