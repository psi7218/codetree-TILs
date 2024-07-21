from collections import deque

n, m = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

graph = [list(map(int, input().split())) for _ in range(n)]
is_exist = [list(map(int, input().split())) for _ in range(n)]
lst = []

for i in range(n):
    for j in range(m):
        if is_exist[i][j] == 1:
            lst.append([i, j])

k = len(lst)
left = 0
right = 1000000001


def test():
    i, j = lst[0]

    visited = [[right] * m for _ in range(n)]
    visited[i][j] = 0

    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                val = abs(graph[x][y] - graph[nx][ny])
                if val < visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = val
    answer = 0
    for a, b in lst:
        answer = max(answer, visited[a][b])

    print(answer)


test()