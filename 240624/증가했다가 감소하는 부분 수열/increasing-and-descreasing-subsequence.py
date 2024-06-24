MAX_K = 2

n = int(input())
arr = list(map(int, input().split()))


dp = [[0] * MAX_K for _ in range(n)]

for i in range(n):
    dp[i][0] = 1
    dp[i][1] = 1

    for j in range(i):
        if arr[j] < arr[i]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)

        if arr[j] > arr[i]:
            dp[i][1] = max(dp[i][1], dp[j][1] + 1)

    dp[i][1] = max(dp[i][1], dp[i][0])

ans = 0
for i in range(n):
    for j in range(MAX_K):
        ans = max(ans, dp[i][j])

print(ans)