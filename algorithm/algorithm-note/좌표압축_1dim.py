# 1 dimention
poss = [6, 10, 8, 9, 6]
s = sorted(list(set(poss)))
# s[i] -> i로 좌표 압축(i는 0 ~ len(s))
d = {s[i]: i for i in range(len(s))}
# d가지고 ... ex)  X'i: Xi > Xj를 만족하는 서로 다른 좌표의 개수라고 하면
print(*[d[x] for x in poss])
