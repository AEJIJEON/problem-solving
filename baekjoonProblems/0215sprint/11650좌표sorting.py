import sys
input = sys.stdin.readline

n = int(input())

array = [0]*n

for i in range(n):
    array[i] = list(map(int, input().split()))

array.sort()

for i in range(n):
    print(*array[i])