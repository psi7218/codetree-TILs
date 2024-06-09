n = int(input())
uf = [i for i in range(n+1)]

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    a, b = find(x), find(y)
    uf[a] = b

for _ in range(n-2):
    s, e = map(int, input().split())
    union(min(s, e), max(s, e))
for i in range(2, n+1):
    I = find(i)
    if I != find(1):
        print(1, i)
        break