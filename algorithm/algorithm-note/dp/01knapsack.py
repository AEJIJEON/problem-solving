# knapsack algorithm

N, W = map(int, input().split())

# 1~N items에 대한 무게, 가치 담는 arrays
weights = [0] * (N + 1)
values = [0] * (N + 1)

for i in range(1, N + 1):
    weights[i], values[i] = map(int, input().split())


dp = [[0] * (N + 1) for _ in range(W + 1)]

for i in range(1, N + 1):
    for w in range(1, W + 1):
        # 현재 item을 가방에 넣을 수 없을 때
        if w < weights[i]:
            dp[w][i] = dp[w][i - 1]
        else:
            # 현재 item을 가방에 넣는 경우, 넣지 않는 경우중에 max값으로 update
            dp[w][i] = max(dp[w - weights[i]][i - 1] + values[i], dp[w][i - 1])

print(dp[W][N])