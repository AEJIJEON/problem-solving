# 문자열 슬라이싱 사용하여 왼쪽 배열과 오른쪽 배열의 sum 값을 비교한다.

arr =list(map(int, input()))
print("LUCKY" if sum(arr[:len(arr)//2]) == sum(arr[len(arr)//2:]) else "READY")