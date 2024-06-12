import heapq

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
INF = int(1e9)
c, d = 0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            c, d = i, j

visited = [[INF] * n for _ in range(n)]
q = []
heapq.heappush(q, (0, c, d))
visited[c][d] = 0

answer = 0
while q:
    cost, x, y = heapq.heappop(q)

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n:
            if cost + 1 < visited[nx][ny]:
                if arr[nx][ny] == 0:
                    heapq.heappush(q, (cost+1, nx, ny))
                    visited[nx][ny] = cost + 1

                elif arr[nx][ny] == 2 and visited[nx][ny] == INF:
                    heapq.heappush(q, (0, nx, ny))
                    answer += cost + 1
                    visited[nx][ny] = cost + 1

if answer == 0:
    print(-1)
else:
    print(answer)