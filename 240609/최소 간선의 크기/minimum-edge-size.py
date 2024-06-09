n, m = map(int, input().split())
s, e = map(int, input().split())

uf = [i for i in range(n+1)]
graph = [list(map(int, input().split())) for _ in range(m)]
graph.sort(key = lambda x : -x[2])
def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])

    return uf[x]

def union(x, y):
    a, b = find(x), find(y)
    uf[a] = b

for c, d, dist in graph:
    union(c, d)
    if find(s) == find(e):
        print(dist)
        break