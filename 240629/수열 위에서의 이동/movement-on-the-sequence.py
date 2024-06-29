n = int(input())
ar = list(map(int, input().split()))
dp = [int(1e9)] * n
dp[0] = 0
for i in range(n-1):
    for j in range(i + 1, i + 1 + ar[i]):
        if j < n:
            dp[j] = min(dp[i] + 1, dp[j])

if dp[-1] == int(1e9):
    print(-1)
else:
    print(dp[-1])