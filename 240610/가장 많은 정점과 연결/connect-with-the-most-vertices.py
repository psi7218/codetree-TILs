n, m, k = map(int, input().split())
points = [0] + list(map(int, input().split()))


uf = [i for i in range(n+1)]

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    a, b = find(x), find(y)

    if a != b:
        uf[a] = b
        points[a], points[b] = min(points[a], points[b]), min(points[a], points[b])

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

standard = points[find(1)]
for index in range(len(points)):
    points[index] = [points[index], index]

points.sort(key = lambda x : x[0])

answer = 0

for idx in range(1, len(points)):
    point = points[idx][0]
    ix = points[idx][1]

    I = find(ix)
    if find(1) != I:
        answer += (standard + point)

        standard = min(standard, point)
        uf[find(1)] = I

if answer <= k:
    print(answer)
else:
    print('NO')