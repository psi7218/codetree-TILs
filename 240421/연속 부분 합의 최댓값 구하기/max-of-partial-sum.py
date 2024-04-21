n = int(input())
arr = list(map(int, input().split()))
INT_MIN = -1e9

dp = [INT_MIN] * n
dp[0] = arr[0]

answer = dp[0]
for i in range(1, n):
    dp[i] = max(dp[i-1] + arr[i], arr[i])
    answer = max(answer, dp[i])


print(answer)