n, m, k = map(int, input().split())
uf= [i for i in range(n+1)]

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    a = find(x)
    b = find(y)

    uf[a] = b

for _ in range(m):
    i, j  = map(int, input().split())
    union(i, j)

s, e = map(int, input().split())

if find(s) == find(e):
    print(1)
else:
    print(0)