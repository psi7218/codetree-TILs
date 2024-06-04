n, m = map(int, input().split())
uf = [i for i in range(n+1)]

def union(x, y):
    a, b = find(x), find(y)

    uf[a] = b

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

for _ in range(m):
    order = list(map(str, input().split()))
    if order[0] == 'x':
        union(int(order[1]), int(order[2]))

    else:
        print(uf.count(uf[int(order[1])]))