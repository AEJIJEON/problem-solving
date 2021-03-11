# 에라토스테네스의 체 알고리즘
# O(NloglogN)
# n의 크기만큼 리스트를 할당
import math

n = 1000
array = [True for _ in range(n + 1)]

# 2부터 n의 제곱근까지의 모든 수를 확인
for i in range(2, int(math.sqrt(n)) + 1):
    # i가 소수인 경우
    if array[i] == True:
        # i를 제외한 i의 모든 배수 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

print(array[1000])