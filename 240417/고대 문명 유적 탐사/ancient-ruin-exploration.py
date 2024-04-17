from collections import deque
from copy import deepcopy

k , m = map(int, input().split())
arr = []
for _ in range(5):
    arr.append(list(map(int, input().split())))

q = deque(map(int, input().split()))


dx = [0,1,0,-1]
dy = [1,0,-1,0]
coordinate = [[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]]

def turn90(n,m):
    newmap = [ar[:] for ar in arr]
    partmap = [ar[m-1:m+2] for ar in arr[n-1:n+2]]
    partmap1 = [[0] * 3 for _ in range(3)]

    for i in range(3):
        for j in range(3):
            partmap1[j][3-i-1] = partmap[i][j]

    for x in range(3):
        for y in range(3):
            newmap[n-1+x][m-1+y] = partmap1[x][y]


    return newmap

def turn180(n,m):
    newmap = [ar[:] for ar in arr]
    partmap = [ar[m - 1:m + 2] for ar in arr[n - 1:n + 2]]
    partmap1 = [[0] * 3 for _ in range(3)]

    for i in range(3):
        for j in range(3):
            partmap1[3-i-1][3-j-1] = partmap[i][j]

    for x in range(3):
        for y in range(3):
            newmap[n-1+x][m-1+y] = partmap1[x][y]


    return newmap

def turn270(n,m):
    newmap = [ar[:] for ar in arr]
    partmap = [ar[m - 1:m + 2] for ar in arr[n - 1:n + 2]]
    partmap1 = [[0] * 3 for _ in range(3)]

    for i in range(3):
        for j in range(3):
            partmap1[3 - j - 1][i] = partmap[i][j]

    for x in range(3):
        for y in range(3):
            newmap[n-1+x][m-1+y] = partmap1[x][y]

    return newmap

def getitem(array):
    visited = [[0] * 5 for _ in range(5)]
    amount = 0
    for i in range(5):
        for j in range(5):

            include = [[i,j]]
            q = deque()
            if visited[i][j] == 0:
                q.append((i,j, array[i][j]))
                visited[i][j] = 1
                while q:
                    x, y, val = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if array[nx][ny] == val and visited[nx][ny] == 0:
                                include.append([nx,ny])
                                visited[nx][ny] = 1
                                q.append((nx,ny,val))

            if len(include) >= 3:
                amount += len(include)
                for inc in include:
                    i, j = inc[0], inc[1]
                    array[i][j] = 0


    return [amount, array, amount == 0]

for _ in range(k):
    answer = 0
    collect = []
    for coor in coordinate:
        x, y = coor[0], coor[1]

        val1 = getitem(turn90(x,y))

        val2 = getitem(turn180(x,y))

        val3 = getitem(turn270(x,y))

        collect.append([val1, 90, x, y])
        collect.append([val2, 180, x, y])
        collect.append([val3, 270, x, y])
    ## 1. 획득가치 2. 각도가 작은 방법 3. 회전 중심 좌표의 열(x)이 작은 구간 4. 열이 같다면 행(y)이 작은 구간
    collect.sort(key=lambda x: (-x[0][0], x[1], x[3], x[2]))
    # print(collect)
    check = collect.pop(0)[0]

    while not check[2]:
        answer += check[0]
        new_arr = check[1]

        for j in range(5):
            for i in range(4,-1,-1):
                if new_arr[i][j] == 0:
                    new_arr[i][j] = q.popleft()

        check = getitem(new_arr)

    arr = check[1]
    if answer == 0:
        break
    else:
        print(answer, end=" ")