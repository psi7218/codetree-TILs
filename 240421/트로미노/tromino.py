n, m = map(int, input().split())


di = [0,1,0,-1]
dj = [1,0,-1,0]
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

answer = 0


def func(x, y, sum1, depth, visited):
    global answer

    if depth == 3:
        answer = max(answer, sum1)

        return

    for k in range(4):
        ni = x + di[k]
        nj = y + dj[k]

        if 0 <= ni < n and 0 <= nj < m:
            if [ni,nj] not in visited:
                func(ni, nj, sum1 + arr[ni][nj], depth + 1, visited + [ni,nj])


for i in range(n):
    for j in range(m):
        func(i, j, arr[i][j], 1, [[i,j]])

print(answer)