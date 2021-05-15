# key array 오른쪽으로 회전
def turn_right(key):
    m = len(key)
    n_key = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            n_key[j][m - i - 1] = key[i][j]
    return n_key


# lock의 정 가운데 원소들이 전부 1인지 check
def check_fit(lock, n):

    flag = True
    for i in range(n):
        for j in range(n):
            # 0이거나(홈과 홈이 만남) 2(돌기와 돌기가 만남)
            if lock[n + i][n + j] != 1:
                return False
    # 열쇠의 돌기 부분들이 자물쇠의 모든 홈 부분에 딱 맞게 채워짐
    return True


def solution(key, lock):
    n, m = len(lock), len(key)
    # m <= n -> lock array를 3N x 3N 으로 늘려줌
    big_lock = [[0] * (3 * n) for _ in range(3 * n)]

    # 늘린 lock의 (N,N) ~ (2N-1, 2N-1) 부분(3N x 3N의 정 가운데)에 lock 넣어줌
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 1:
                big_lock[n + i][n + j] = 1
    # (0,0) ~ (3N-M, 3N-M) key를 움직이면서 자물쇠가 풀릴 수 있는지 check
    for start_x in range(3 * n - m):
        for start_y in range(3 * n - m):

            # key를 4 번 회전시켜줌
            for _ in range(4):

                # key와 big_lock의 원소 값들을 더해줌
                for i in range(m):
                    for j in range(m):
                        big_lock[start_x + i][start_y + j] += key[i][j]
                # lock 부분의 원소들이 전부 1인 경우
                # 즉, 열쇠의 돌기 부분들이 자물쇠의 모든 홈 부분에 딱 맞게 채워짐

                if check_fit(big_lock, n):
                    return True
                # big_lock 원상복구
                for i in range(m):
                    for j in range(m):
                        big_lock[start_x + i][start_y + j] -= key[i][j]
                key = turn_right(key)
    return False

    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))