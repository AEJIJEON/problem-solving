# 빈칸에 벽을 3개 세울 수 있는 모든 조합을 고려한다.
# itertools module의 combinations 함수를 사용해서 모든 조합 구해준다.
# 조합은 dfs 알고리즘을 사용한 완전 탐색을 진행한다.



# 벽 3개를 세운 후 dfs 알고리즘을 사용하여 바이러스 전파를 진행한다. dfs 알고리즘을 사용하여 바이러스를 
# 전파하는 함수 정의
# 바이러스 전파가 끝난 후의 연구소에서 빈 칸의 개수를 세어주어 최댓값으로 업데이트한다.


from itertools import combinations
import copy

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(arr, x, y, n, m):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= n - 1 and 0 <= ny <= m - 1 and arr[nx][ny] == 0:
            arr[nx][ny] = 2
            dfs(arr, nx, ny, n, m)


n, m = map(int, input().split())
empty = []
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == 0:
            empty.append((i, j))

result = 0

for comb in combinations(empty, 3):

    for x, y in comb:
        board[x][y] = 1

    temp = copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                dfs(temp, i, j, n, m)


    result = max(result, sum(arr.count(0) for arr in temp))

    for x, y in comb:
        board[x][y] = 0

print(result)