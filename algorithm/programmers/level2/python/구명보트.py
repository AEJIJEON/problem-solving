# queue 사용하지 않고 two pointer 사용

# 구명보트 1개 -> 최대 2명
# people 배열을 오름차순으로 정렬
# 제일 무게 작은 사람 탑승 -> 두 번째 사람으로는 limit를 초과하지 않는 범위에서 제일 무게가 큰 사람 탑승
# 제일 무게가 큰 사람 탑승 -> limit값에서 탑승한 사람 무게를 뺀 값이 탑승하지 않은 사람들 중 제일 무게가 작은 값 이상인 경우 같이 탑승, 그렇지 않은 경우 혼자 태움


def solution(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    count = 0

    while i <= j:
        # 구명보트 추가
        count += 1
        # 마지막으로 남은 사람을 보트에 혼자 탑승시킴
        if i == j:
            break
        # j 번째 사람과 함께 탑승할 수 있는 사람이 존재(i 번째 사람)
        if people[i] + people[j] <= limit:
            # i 번째 사람 탑승
            i += 1
        # j 번째 사람 탑승
        j -= 1

    return count