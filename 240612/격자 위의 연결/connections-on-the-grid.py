n, m = tuple(map(int, input().split()))
edges = []
uf = [0] * (n * m + 1)

for i in range(1, n + 1):
    costs = list(map(int, input().split()))
    for j in range(1, m):

        x = (i - 1) * m + j
        y = (i - 1) * m + j + 1

        edges.append((costs[j - 1], x, y))

for i in range(1, n):
    costs = list(map(int, input().split()))
    for j in range(1, m + 1):
        x = (i - 1) * m + j
        y = i * m + j

        edges.append((costs[j - 1], x, y))


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    X = find(x)
    Y = find(y)
    uf[X] = Y

edges.sort()

for i in range(1, n * m + 1):
    uf[i] = i

ans = 0
for cost, x, y in edges:
    if find(x) != find(y):
        ans += cost
        union(x, y)

print(ans)