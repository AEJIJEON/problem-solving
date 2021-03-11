data = [[0,0], [1,1], [0,2], [2,0], [0,3], [3,2], [1,4], [4,4], [100,50], [150,30]]
xs = []
ys = []

for i in range(len(data)):
    xs.append(data[i][0])
    ys.append(data[i][1])

xs = sorted(list(set(xs))) 
ys = sorted(list(set(ys)))

# O(n^2)
# x좌표 압축
for i in range(len(data)):
    for j in range(len(xs)):
        if data[i][0] == xs[j]:
            data[i][0] = j

# O(n^2)
# y좌표 압축
for i in range(len(data)):
    for j in range(len(ys)):
        if data[i][1] == ys[j]:
            data[i][1] = j

print(data)