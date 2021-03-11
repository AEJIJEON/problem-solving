# O(logN)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


array = [1, 3, 5, 6, 7, 8]
print(binary_search(array, 6, 0, 6))