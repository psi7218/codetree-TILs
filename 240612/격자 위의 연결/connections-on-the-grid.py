n, m = map(int, input().split())
mst = []

uf = [[[] for _ in range(m)] for _ in range(n)]
for s in range(n):
    for t in range(m):
        uf[s][t] = [s,t]

def find(lst):
    x, y = lst
    if uf[x][y] == [x,y]:
        return uf[x][y] 
    uf[x][y] = find(uf[x][y])
    return uf[x][y]

def union(c, d):
    Cx,Cy = find(c)
    Dx,Dy = find(d)

    uf[Cx][Cy] = [Dx,Dy]
    

for i in range(n):
    num_list = list(map(int, input().split()))
    for j in range(m-1):
        mst.append([[i,j],[i,j+1],num_list[j]])

for a in range(n-1):
    num_list = list(map(int, input().split()))
    for b in range(m):
        mst.append([[a,b],[a+1,b], num_list[b]])

mst.sort(key = lambda x : x[2])

cnt = 0
answer = 0
for z in range(len(mst)):
    start, end, val = mst[z]
    if find(start) != find(end):
        union(start, end)
        answer += val
        cnt += 1

    if cnt == n*m - 1:
        break

print(answer)