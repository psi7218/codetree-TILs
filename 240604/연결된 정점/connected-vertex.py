n, m = map(int, input().split())
uf = [i for i in range(n+1)]
size = [1] * (n+1)

def union(x, y):
    a, b = find(x), find(y)

    if a != b:
        uf[a] = b

        size[b] += size[a]

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
        val = find(int(order[1]))
        print(size[val])