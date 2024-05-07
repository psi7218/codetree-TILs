n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

L,R = [0] * n, [0] * n

for i in range(1,n):
    L[i] = abs(arr[i][0] - arr[i-1][0]) + abs(arr[i][1] - arr[i-1][1]) + L[i-1]

for j in range(n-2,-1,-1):
    R[j] = abs(arr[j][0] - arr[j+1][0]) + abs(arr[j][1] - arr[j+1][1]) + R[j+1]


answer = 1e9
for k in range(1, n-1):
    answer = min(answer, L[k-1] + R[k+1] + abs(arr[k+1][0] - arr[k-1][0]) + abs(arr[k+1][1] - arr[k-1][1]))

print(answer)