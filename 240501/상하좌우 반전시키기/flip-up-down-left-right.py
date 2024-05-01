n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,1,0,-1]
dy = [0,1,0,-1,0]
check = [[0]* n for _ in range(n)]
answer = 0
for i in range(1, n):
    for j in range(n):
        if arr[i-1][j] == 0:
            for k in range(5):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    arr[nx][ny] ^= 1
            answer += 1

cnt = 0
for line in arr:
    cnt += sum(line)

if cnt == n * n:
    print(answer)
else:
    print(-1)