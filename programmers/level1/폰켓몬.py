def solution(nums):
    n = len(nums)
    distinct_n = len(set(nums))
    return n // 2 if distinct_n >= n // 2 else distinct_n


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
