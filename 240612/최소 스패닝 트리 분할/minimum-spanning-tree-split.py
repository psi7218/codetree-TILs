n, m = map(int, input().split())

uf = [i for i in range(n+1)]

mst = []
for _ in range(m):
    start, end, dist = map(int, input().split())
    mst.append([start,end,dist])

mst.sort(key = lambda x : x[2])

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    a, b = find(x), find(y)
    uf[a] = b 

cnt = 0
answer = 0
for lst in mst:
    s, e, val = lst
    if find(s) != find(e):
        answer += val
        cnt += 1
        union(s, e)
    
    if cnt == n - 2:
        break

print(answer)