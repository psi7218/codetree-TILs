n = int(input())
dp = [1] * n
ar = [tuple(map(int, input().split())) for _ in range(n)]
for i in range(1,n):
    for j in range(i):
        if ar[j][1] < ar[i][0]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))