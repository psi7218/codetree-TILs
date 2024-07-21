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
right = 1000000000
answer = 1000000000

def test(s, e, dist):
    si, sj = lst[s]
    ei, ej = lst[e]

    visited = [[0] * m for _ in range(n)]
    visited[si][sj] = 1

    q = deque()
    q.append((si, sj))

    while q:
        x, y = q.popleft()

        if x == ei and y == ej:
            return 1
        
        for p in range(4):
            nx = x + dx[p]
            ny = y + dy[p]

            if 0 <= nx < n and 0<= ny < m:
                if visited[nx][ny] == 0 and abs(graph[x][y] - graph[nx][ny]) <= dist:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

    return 0




def ispossible(dist):

    for a in range(k):
        for b in range(a+1, k):
            if not test(a, b, dist):
                return 0

    return 1


while left <= right:
    mid = (left + right) // 2

    if ispossible(mid):
        answer = min(answer, mid)
        right = mid - 1
    else:
        left = mid + 1

print(answer)