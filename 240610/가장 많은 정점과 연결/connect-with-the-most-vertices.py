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

answer = 0

for idx in range(2, n+1):
    standard = find(1)
    I = find(idx)

    if standard != I:
        answer += (points[idx] + points[1])
        union(1, idx)
    

if answer <= k:
    print(answer)
else:
    print('NO')