n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
dp[0][0] = 1

for k in range(1, n):
    arr[k][0] = int(1e9)

for l in range(1, m):
    arr[0][l] = int(1e9)

for i in range(1, n):
    for j in range(1, m):
        for s in range(i):
            for t in range(j):
                if arr[s][t] < arr[i][j] and arr[0][0] < arr[i][j]:
                    dp[i][j] = max(dp[i][j], dp[s][t] + 1)

answer = 1
for x in range(1, n):
    for y in range(1, m):
        answer = max(answer, dp[x][y])



print(answer)