n, m = map(int, input().split())
alpha = [0] + list(map(str, input().split()))

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
    X, Y = find(x), find(y)
    uf[X] = Y

answer = 0

for k, i, j in mst:
    if find(i) == find(j):
        continue
    
    if alpha[i] == alpha[j]:
        continue
    
    union(i,j)
    answer += k

print(answer)