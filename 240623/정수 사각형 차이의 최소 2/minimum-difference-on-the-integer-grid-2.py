n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[[101,1] for _ in range(n)] for _ in range(n)]

dp[0][0] = [min(dp[0][0][0], arr[0][0]), max(dp[0][0][1], arr[0][0])]

for k in range(1,n):
    dp[k][0] = [min(dp[k-1][0][0], arr[k][0]), max(dp[k-1][0][1], arr[k][0])]
    dp[0][k] = [min(dp[0][k-1][0], arr[0][k]), max(dp[0][k-1][1], arr[0][k])]


for i in range(1,n):
    for j in range(1,n):
        val1 = max(arr[i][j], dp[i-1][j][1]) - min(arr[i][j], dp[i-1][j][0])
        val2 = max(arr[i][j], dp[i][j-1][1]) - min(arr[i][j], dp[i][j-1][0])

        if val1 > val2:
            dp[i][j] = [min(arr[i][j], dp[i][j-1][0]), max(arr[i][j], dp[i][j-1][1])]
        else:
            dp[i][j] = [min(arr[i][j], dp[i-1][j][0]), max(arr[i][j], dp[i-1][j][1])]


# for line in dp:
#     print(line)
print(abs(dp[n-1][n-1][0] - dp[n-1][n-1][1]))