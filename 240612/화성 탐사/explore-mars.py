from collections import deque
import heapq

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
number = [[0] * n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
mst = []

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    a, b = find(x), find(y)
    uf[a] = b

count = 1
num = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 or arr[i][j] == 2:
            number[i][j] = num
            num += 1

        if arr[i][j] == 2:
            count += 1

uf = [i for i in range(num+1)]


def bfs(c,d):
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((c, d))
    visited[c][d] = 0

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1:
                    if arr[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx,ny))
                    if arr[nx][ny] == 1 or arr[nx][ny] == 2:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
                        mst.append((visited[nx][ny], number[c][d], number[nx][ny]))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 or arr[i][j] == 2:
            bfs(i,j)

mst.sort()

answer = 0
for cost, start, end in mst:
    if find(start) != find(end):
        union(start, end)
        answer += cost
        count -= 1

if count == 1:
    print(answer)
else:
    print(-1)