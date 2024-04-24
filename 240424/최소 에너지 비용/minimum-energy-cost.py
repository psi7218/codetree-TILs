n = int(input())
dis = list(map(int, input().split()))
cost = list(map(int, input().split()))

pre = [1e9] * n
pre[0] = cost[0]
for i in range(1,n):
    pre[i] = min(cost[i-1], cost[i])

answer = 0
for j in range(n-1):
    answer += dis[j] * pre[j]


print(answer)