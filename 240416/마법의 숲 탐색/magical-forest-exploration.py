from collections import deque

r, c, k = map(int, input().split())
arr = [[0] * c for _ in range(r + 3)]

def downmove(x, y, dir):
    global isTrue, location
    num = [0,1,2,3]
    flag1 = False
    flag2 = False
    flag3 = False

    if x == r + 3:
        location = [x-1, y, dir]
        isTrue = True
        return

    if arr[x][y] == 0 and arr[x-1][y-1] == 0  and arr[x-1][y+1] == 0:
        ## 한칸 내리기
        flag1 = True
    if 0 <= y - 2:
        if arr[x-3][y-1] == 0 and arr[x-2][y-2] == 0 and arr[x-1][y-2] == 0 and arr[x-1][y-1] == 0 and arr[x][y-1] == 0:
            flag2 = True

    if y + 2 < c:
        if arr[x-3][y+1] == 0 and arr[x-2][y+2] == 0 and arr[x-1][y+1] == 0 and arr[x-1][y+2] == 0 and arr[x][y+1] == 0:
            ## 동쪾으로
            flag3 = True

    if flag1:
        downmove(x+1,y, num[dir])
    elif flag2:
        downmove(x+1,y-1, num[dir-1])
    elif flag3:
        downmove(x+1,y+1, num[(dir+1) % 4])

    else:
        if x >= 5:
            location = [x-1, y, dir]
            isTrue = True
            return

        else:
            return

def findmaxcol(s,t):
    global answer

    di = [0,1,0,-1]
    dj = [1,0,-1,0]


    max_val = 0
    visited = [[0] * c for _ in range(r + 3)]

    q = deque()
    visited[s][t] = 1
    q.append((s,t, arr[s][t]))

    while q:
        i, j, current = q.popleft()
        max_val = max(max_val, i - 2)

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 3 <= ni < r + 3 and 0 <= nj < c:
                if visited[ni][nj] == 0 and current == arr[ni][nj]:
                    q.append((ni,nj,current))
                    visited[ni][nj] = 1
                if visited[ni][nj] == 0 and direction[i][j] and arr[ni][nj] != 0:
                    q.append((ni,nj,arr[ni][nj]))
                    visited[ni][nj] = 1

    answer += max_val
    # print(max_val)
answer = 0
temp = 1 ## 골렘 숫자
direction = [[0] * c for _ in range(r + 3)]
for z in range(k):
    col, dir = map(int, input().split())


    tmp = col - 1  ## 입력 받은 열 값
    isTrue = False
    location = []
    downmove(2, tmp, dir)
    if isTrue:
        i, j, dir = location[0], location[1], location[2]

        arr[i][j] = temp
        arr[i-1][j] = temp
        arr[i-1][j-1] = temp
        arr[i-1][j+1] = temp
        arr[i-2][j] = temp

        loc = [(i-2,j), (i-1,j+1), (i,j) ,(i-1,j-1)]
        a, b = loc[dir][0], loc[dir][1]
        direction[a][b] = temp
        findmaxcol(i - 1, j)
    else:
        arr = [[0] * c for _ in range(r + 3)]
        direction = [[0] * c for _ in range(r + 3)]
    temp += 1


#     print(z, answer)
#
# for line in arr:
#     print(*line)
# print('-----------------------')
# for lane in direction:
#     print(*lane)
print(answer)
# print(direction)