# prefix sum
# 구간 합 계산(a 번째 수부터 b 번째 수까지의 합)
# O(N)
# N개의 데이터와 M개의 쿼리 -> O(N+M)

n = 5
data = [10, 20, 30, 40, 50]


sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)


left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])