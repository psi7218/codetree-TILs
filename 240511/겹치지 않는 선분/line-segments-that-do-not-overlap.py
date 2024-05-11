n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
y = [0] * n 
for i in range(n):
    y[i] = arr[i][1]
y.sort()
arr.sort(key=lambda x: x[0])

for j in range(n):
    if y[j] == arr[j][1]:
        answer += 1

print(answer)