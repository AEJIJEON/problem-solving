# dp 유형
# dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + arr[i][j]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (i + 1) for i in range(n)]

dp[0][0] = arr[0][0]
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = arr[i][j] + dp[i - 1][j]
        elif j == i:
            dp[i][j] = arr[i][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = arr[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[n - 1]))
