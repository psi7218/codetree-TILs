n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[[101,1] for _ in range(n)] for _ in range(n)]

dp[0][0] = [min(dp[0][0][0], arr[0][0]), max(dp[0][0][1], arr[0][0])]

for k in range(1,n):
    dp[k][0] = [min(dp[k-1][0][0], arr[k][0]), max(dp[k-1][0][1], arr[k][0])]
    dp[0][k] = [min(dp[0][k-1][0], arr[0][k]), max(dp[0][k-1][1], arr[0][k])]


for i in range(1,n):
    for j in range(1,n):
        dp[i][j][0] = min(min(dp[i-1][j][0], dp[i][j-1][0]), arr[i][j])
        dp[i][j][1] = max(min(dp[i-1][j][1], dp[i][j-1][1]), arr[i][j])

print(abs(dp[n-1][n-1][0] - dp[n-1][n-1][1]))