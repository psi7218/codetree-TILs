n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

L,R = [0] * n, [0] * n

for i in range(1,n):
    L[i] = abs(arr[i][0] - arr[0][0]) + abs(arr[i][1] - arr[0][1]) 

for j in range(n-2,-1,-1):
    R[j] = abs(arr[j][0] - arr[n-1][0]) + abs(arr[j][1] - arr[n-1][1])

answer = 1e9
for k in range(1, n-1):
    answer = min(answer, L[k] + R[k])

print(answer)