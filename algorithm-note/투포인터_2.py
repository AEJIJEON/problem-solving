# 정렬되어 있는 두 리스트의 합집합(merge algorithm)
# 중복된 원소들도 다 포함
# O(N+M)

n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

# 리스트 a와 b의 모든 원소를 담을 수 있는 크기의 결과 리스트 초기화
result = [0] * (n + m)
i, j, k = 0, 0, 0

# 모든 원소가 결과 리스트에 담길 때까지
while i < n or j < m:
    # 리스트 b가 처리되었거나 리스트 a의 원소가 더 적을 때
    if j >= m or (i < n and a[i] <= b[j]):
        result[k] = a[i]
        i += 1
    # 리스트 ㅁ가 처리되었거나 리스트 b의 원소가 더 적을 때
    else:
        result[k] = b[j]
        j += 1
    k += 1

print(*result)
print(*["1", "2", "3"], sep=",")
print(*["a", "b", "c"], sep="")
