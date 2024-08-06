from collections import deque

n, m = map(int, input().split())
graph = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

left = 1
right = 500
answer = 501


def muterable(diff):
    for i in range(1, 501 - diff):
        if is_possible(i, i + diff):
            return True

    return False


def is_possible(lo, hi):
    visited = [[0] * m for _ in range(n)]

    q = deque()
    if graph[0][0] < lo or graph[0][0] > hi:
        return False

    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        if x == n-1 and y == m-1:
            return True

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if lo <= graph[nx][ny] <= hi:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    return False


while left <= right:
    mid = (left + right) // 2

    if muterable(mid):
        right = mid - 1
        answer = min(answer, mid)

    else:
        left = mid + 1

print(answer)