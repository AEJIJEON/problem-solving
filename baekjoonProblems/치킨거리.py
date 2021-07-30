# 최대 M개 -> 치킨집이 M개 이상 있을 경우 M개를 고려해서 치킨거리를 구해야
# 도시의 치킨거리의 최솟값을 구할 수 있다.
# 집 위치, 치킨집 위치 담는 배열 2개 선언
# combinations 모듈 사용하여 
# 치킨집을 M개 선택하는 모든 조합을 구해줌
# 치킨집이 선택된 모든 조합마다
# 모든 집에 대해 치킨 거리를 구해주고 다 더하여 도시의 치킨 거리를 구해줌
# 결괏값 업데이트

from itertools import combinations

INF = int(1e9)

n, m = map(int, input().split())
people = []
chicken = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            people.append((i, j))
        elif temp[j] == 2:
            chicken.append((i, j))

result = INF
for comb in combinations(chicken, m):
    chicken_d = 0
    for pos in people:
        dis = INF
        for x, y in comb:
            dis = min(dis, abs(pos[0]-x) + abs(pos[1]-y))
        
        chicken_d += dis
    result = min(result, chicken_d)

print(result)