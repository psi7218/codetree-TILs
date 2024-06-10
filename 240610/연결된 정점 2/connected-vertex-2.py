n = int(input())
uf = [i for i in range(100000+1)]
size = [1] * (100000 + 1)

def find(x):
    if uf[x] == x:
        return x 
    uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    a, b = find(x), find(y)
    if a != b:
        uf[a] = b 
        size[b] += size[a]


for _ in range(n):
    s, t = map(int, input().split())
    union(s, t)
    print(max(size[t], size[s]))