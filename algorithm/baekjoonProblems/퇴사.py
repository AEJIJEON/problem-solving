# dp 유형
# dp[i]: i일부터 상담을 시작할 때 얻을 수 있는 최대 수익
# dp[i] = max(dp[i+1], Pi + dp[i + Ti]) if i + Ti <= N + 1 else dp[i+1]
# i = N, N-1, N-2, ..., 1 dp 테이블 업데이트

n = int(input())
t = [0] * (n + 1)
p = [0] * (n + 1)
dp = [0] * (n + 2)

for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())

for i in range(n, 0, -1):
    dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]]) if i + t[i] <= n + 1 else dp[i + 1]

print(dp[1])