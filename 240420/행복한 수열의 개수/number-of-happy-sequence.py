n, m = map(int, input().split())

answer = 0
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    cnt = 0
    temp = -1
    for j in range(n):
        if arr[i][j] == temp:
            cnt += 1
        else:
            cnt = 1
            temp = arr[i][j]

        if cnt >= m:
            answer += 1
            break

for b in range(n):
    cnt = 0
    temp = -1
    for a in range(n):
        if arr[a][b] == temp:
            cnt += 1
        else:
            cnt = 1
            temp = arr[a][b]

        if cnt >= m:
            answer += 1
            break

print(answer)