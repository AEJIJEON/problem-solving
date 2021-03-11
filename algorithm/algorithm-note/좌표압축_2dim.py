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
xs = []
ys = []

for i in range(len(data)):
    xs.append(data[i][0])
    ys.append(data[i][1])

xs = {value: i for i, value in enumerate(sorted(list(set(xs))))}
ys = {value: i for i, value in enumerate(sorted(list(set(ys))))}

# O(n)!!
# x,y좌표 압축
for i in range(len(data)):
    data[i][0] = xs[data[i][0]]
    data[i][1] = ys[data[i][1]]


print(data)
