n, m, p, c, d = map(int, input().split())
graph = [[0] * n for _ in range(n)]

rr, rc = map(int, input().split())
rr -= 1
rc -= 1
graph[rr][rc] = -1  ## 루돌프 위치 (-1)
santa = []
_dx, _dy = [1,1,1,0,-1,-1,-1, 0], [1,0,-1,-1,-1,0,1, 1]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
score = [0] * (p+1)
death = [False] * (p + 1)
for _ in range(p):
    num, x, y = map(int, input().split())
    santa.append((num, x - 1, y - 1))
    graph[x - 1][y - 1] = num ## 산타 위치 (산타의 각 번호)
status = [0] * (p + 1)

def rudolph_move():
    global rr, rc
    santa.sort(key=lambda x: ((x[1] - rr)**2 + (x[2] - rc)**2, -x[1], -x[2]))

    santa_num, santa_x, santa_y = santa[0]
    maxval = [2 * n**2, [], -1]
    for k in range(8):
        rx = rr + _dx[k]
        ry = rc + _dy[k]
        if not (0 <= rx < n and 0 <= ry < n):
            continue
        if (rx - santa_x)**2 + (ry - santa_y)**2 < maxval[0]:
            maxval = [(rx - santa_x)**2 + (ry - santa_y)**2, [rx, ry], k]


    graph[rr][rc] = 0
    rr, rc = maxval[1][0], maxval[1][1]
    if graph[rr][rc] > 0:
        santa.sort()

        number, sa_x, sa_y = santa[graph[rr][rc] - 1]
        score[number] += c

        status[number] = 2

        temp_x, temp_y = sa_x + _dx[maxval[2]] * c, sa_y + _dy[maxval[2]] * c

        if not (0 <= temp_x < n and 0 <= temp_y < n):
            santa[number - 1] = (number, -1, -1)
            death[number] = True
            graph[rr][rc] = -1
            if death[1:] == [True] * p:
                print(*score[1:])
                exit()
            return

        while True:
            if graph[temp_x][temp_y]:
                santa[number - 1] = (number, temp_x, temp_y)

                now_num = graph[temp_x][temp_y]
                now_santa = santa[now_num - 1]
                temp_x = now_santa[1] + _dx[maxval[2]]
                temp_y = now_santa[2] + _dy[maxval[2]]

                number = now_num

                if not (0 <= temp_x < n and 0 <= temp_y < n):
                    santa[number - 1] = (number, -1, -1)
                    death[number] = True
                    if death[1:] == [True] * p:
                        print(*score[1:])
                        exit()
                    break
            if graph[temp_x][temp_y] == 0:
                santa[number - 1] = (number, temp_x, temp_y)
                break
        for numb, xx, yy in santa:
            if xx == -1 and yy == -1:
                continue
            graph[xx][yy] = numb
    graph[rr][rc] = -1



def santa_move():
    global rr, rc
    santa.sort()

    for num, x, y in santa:
        if status[num] > 0:
            continue
        flag = False
        if x == -1 and y == -1:
            continue

        temp = [(rr - x)**2 + (rc - y)**2, [], -1]

        for k in range(4):
            sx = x + dx[k]
            sy = y + dy[k]

            if not (0 <= sx < n and 0 <= sy < n):
                continue

            if (rr - sx)**2 + (rc - sy)**2 < temp[0]:
                if graph[sx][sy] > 0: ## 움직인 곳에 산타가 있으면 패스
                    continue

                temp = [(rr - sx)**2 + (rc - sy)**2, [sx, sy], k]
                flag = True

        if not flag:
            continue

        dist, san_x, san_y, dir = temp[0], temp[1][0], temp[1][1], temp[2]

        if graph[san_x][san_y] == -1:  ## 움직이는 칸에 루돌프
            score[num] += d

            dir = (dir + 2) % 4
            new_x = san_x + dx[dir] * d
            new_y = san_y + dy[dir] * d

            if not (0 <= new_x < n and 0 <= new_y < n):
                graph[x][y] = 0
                santa[num - 1] = (num, -1, -1)
                death[num] = True
                if death[1:] == [True] * p:
                    print(*score[1:])
                    exit()
            else:
                status[num] = 2
                santa.sort()
                temp_x, temp_y = new_x, new_y
                graph[x][y] = 0

                while True:
                    if graph[temp_x][temp_y]:
                        santa[num-1] = (num, temp_x, temp_y)

                        now_num = graph[temp_x][temp_y]
                        now_santa = santa[now_num-1]
                        temp_x = now_santa[1] + dx[dir]
                        temp_y = now_santa[2] + dy[dir]

                        num = now_num

                        if not (0 <= temp_x < n and 0 <= temp_y < n):
                            santa[num - 1] = (num, -1, -1)
                            death[num] = True
                            if death[1:] == [True] * p:
                                print(*score[1:])
                                exit()
                            break
                    if graph[temp_x][temp_y] == 0:
                        santa[num - 1] = (num, temp_x, temp_y)
                        break

                for num, xx, yy in santa:
                    if xx == -1 and yy == -1:
                        continue
                    graph[xx][yy] = num

        elif graph[san_x][san_y] == 0: ## 이동한 곳이 빈칸일 경우
            graph[x][y] = 0
            graph[san_x][san_y] = num
            santa[num-1] = (num, san_x, san_y)



for time in range(1, m+1):

    rudolph_move()
    santa_move()

    for nu, _x, _y in santa:
        if _x == -1 and _y == -1:
            continue

        score[nu] += 1
    for z in range(1, p+1):
        if status[z] > 0:
            status[z] -= 1


    #
    # print('------')
    # for line in graph:
    #     print(line)
    # print(death)
    # print(status)
    # print(f'score : {score}')
    # print(f'"----------: {time}턴 끝"')
print(*score[1:])