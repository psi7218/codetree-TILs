n, m = map(int, input().split())

loc = [0]
uf = [i for i in range(n+1)]
mst = []

def find(x):
    if uf[x] == x:
        return uf[x]
    uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    a, b = find(x), find(y)
    uf[a] = b 
for i in range(1, n+1):
    x, y = map(int, input().split())

    for j in range(1, len(loc)):
        x1, y1 = loc[j][0], loc[j][1]
        dist = ((x1 - x)**2 + (y1 - y)**2)**0.5
        mst.append([i,j, dist])
    loc.append([x,y])
mst.sort(key = lambda x : x[2])

for _ in range(m):
    val1, val2 = map(int, input().split())
    union(val1, val2)

answer = 0
cnt = m
for idx in mst:
    start, end, distance = idx
    if find(start) != find(end):
        answer += distance
        cnt += 1
        union(start, end)
    
    if cnt == n - 1:
        break

print(f"{answer:.2f}")