# 후보 키의 최대 개수 구하기
# 모든 튜플 조합 완전 탐색 -> 각 조합에 대해 유일성, 최소성 체크
# 유일성 체크하는 법
# 해당 조합에 해당하는 튜플들을 set에 모두 넣은 후 원소의 개수가 전체 레코드 개수와 같은 지 확인
#
# 최소성 체크하는 법
# 튜플 조합을 탐색하는 동안
# 후보키 집합에 있는 모든 후보키에 대해서
# 후보키를 포함하고 있지 않은 경우

from itertools import combinations
def solution(relation):
    n, m = len(relation), len(relation[0])
    candidates = []
    for i in range(1, m+1):
        
        for comb in combinations(range(m), i):
            flag = True
            for candidate in candidates:
                if len(candidate - set(comb)) == 0:
                    flag = False
                    break
            if not flag:
                continue
            tuple_set = set([tuple([record[c] for c in comb]) for record in relation])

            if len(tuple_set) == n:
                candidates.append(set(comb))
    return len(candidates)