n, m = map(int, input().split())

uf = [i for i in range(n+1)]
cnt = 0
def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    a, b = find(x), find(y)
    uf[a] = b
    
for _ in range(m):
    s, e = map(int, input().split())
    if find(s) == find(e):
        cnt += 1
    else:
        union(s, e)
    
for d in range(2, n + 1):
    if find(1) != find(d):
        cnt += 1
        union(d, 1)
print(cnt)