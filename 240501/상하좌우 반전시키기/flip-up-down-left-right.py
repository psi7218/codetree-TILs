n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,1,0,-1]
dy = [0,1,0,-1,0]
check = [[0]* n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            for k in range(5):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    check[nx][ny] += 1

answer = 0
for a in range(n):
    for b in range(n):
        if check[a][b] % 2 == 1:
            for k in range(5):
                nx = a + dx[k]
                ny = b + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    arr[nx][ny] ^= 1
            answer += 1


cnt = 0
for line in arr:
    cnt += sum(line)

if cnt == n *n:
    print(answer)
else:
    print(-1)