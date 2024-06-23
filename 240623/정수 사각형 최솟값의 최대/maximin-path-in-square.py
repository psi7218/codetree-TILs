n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = arr[0][0]
for j in range(1,n):
    dp[0][j] = min(arr[0][j], dp[0][j-1])
    dp[j][0] = min(arr[j][0], dp[j-1][0])

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]),arr[i][j])

print(dp[n-1][n-1])