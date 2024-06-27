n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))

INF = int(1e9)

dp = [[-1001 for _ in range(k + 2)] for _ in range(n + 1)]
answer = -INF

for i in range(1, n + 1):
    for j in range(1,k + 2):
        if j == 1:
            dp[i][j] = a[i]

        elif j >= k:
            dp[i][j] = max(dp[i - 1][j - 1] + a[i], dp[i-1][j] + a[i])
        else:
            dp[i][j] = dp[i - 1][j - 1] + a[i]
# for line in dp:
#     print(line)

for x in range(1, n+1):
    for y in range(k,k+2):
        answer = max(answer, dp[x][y])

print(answer)