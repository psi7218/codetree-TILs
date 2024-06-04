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

orders = list(map(int, input().split()))

flag = False

for idx in range(k-1):
    if find(orders[idx]) == find(orders[idx+1]):
        continue

    else:
        flag = True

if flag:
    print(0)
else:
    print(1)