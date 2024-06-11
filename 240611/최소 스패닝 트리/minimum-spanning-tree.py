n, m = map(int, input().split())

uf = [i for i in range(n+1)]
mst = []

for _ in range(m):
    a, b, c = map(int, input().split())
    mst.append([c, a, b])

mst.sort(key = lambda x : x[0])

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    s, t = find(x), find(y)
    uf[s] = t

answer = 0
for i,j,k in mst:
    if find(i) == find(j):
        continue
    union(i,j)
    answer += k

print(answer)