# 2 dimension 좌표 압축 O(n)
data = [
    [0, 0],
    [1, 1],
    [0, 2],
    [2, 0],
    [0, 3],
    [3, 2],
    [1, 4],
    [4, 4],
    [100, 50],
    [150, 30],
]
xs = sorted(list(set([x[0] for x in data])))
ys = sorted(list(set([x[1] for x in data])))

xs = {value: i for i, value in enumerate(xs)}
ys = {value: i for i, value in enumerate(ys)}

# O(n)!!
# x,y좌표 압축
for i in range(len(data)):
    data[i][0] = xs[data[i][0]]
    data[i][1] = ys[data[i][1]]


print(data)
