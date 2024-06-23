n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[1] * n for _ in range(n)]

order = []
for i in range(n):
    for j in range(n):
        order.append((arr[i][j], i, j))

order.sort()
answer = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for val,s,t in order:
    for k in range(4):
        nx = s + dx[k]
        ny = t + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[s][t] > arr[nx][ny]:
                dp[s][t] = max(dp[s][t], dp[nx][ny] + 1)
                answer = max(dp[s][t], answer)

print(answer)