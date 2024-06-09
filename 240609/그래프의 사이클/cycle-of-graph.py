n, m = map(int, input().split())

uf = [i for i in range(n+1)]

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    a, b = find(x), find(y)
    uf[a] = b 

for idx in range(m):
    s, e = map(int, input().split())
    

    if find(s) == find(e):
        print(idx + 1)
        exit()
    union(s, e)
print('happy')