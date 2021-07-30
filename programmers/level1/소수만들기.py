from itertools import combinations

# nums 원소는 최대 1000
is_prime = [True] * 3001
is_prime[1] = False

# 에라토스테네스의 체 이용
for i in range(2, 3001):
    if is_prime[i]:
        j = 2
        while i * j <= 3000:
            is_prime[i * j] = False
            j += 1


def solution(nums):
    count = 0
    # nums 배열의 원소들 중 3개를 골라 더해준 후 소수인지 check
    for x in combinations(nums, 3):
        if is_prime[sum(x)]:
            count += 1

    return count


print(solution([1, 2, 7, 6, 4]))
