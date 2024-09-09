L, N, Q = map(int, input().split())
board = [[0] * (L+1)] + [[0] + list(map(int, input().split())) for _ in range(L)]
knights_board = [[0] * (L+1) for _ in range(L+1)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
lifes = [0]
knights = [[[] for _ in range(4)] for _ in range(N + 1)]
record_lst = [[]]
result_check = [0] * (N + 1)
for idx in range(1, N + 1):
    r, c, h, w, k = map(int, input().split())
    lifes.append(k)
    result_check[idx] = k
    record_lst.append((r, c, h, w))
    for i in range(r, r + h):
        for j in range(c, c + w):
            knights_board[i][j] = idx

            if i == r:
                knights[idx][0].append([i,j])
            if j == c + w - 1:
                knights[idx][1].append([i,j])
            if i == r + h - 1:
                knights[idx][2].append([i,j])
            if j == c:
                knights[idx][3].append([i,j])


def move_knights(k_idx, dir):
    global is_possible, move_lst
    if not is_possible:
        return

    for s, t in knights[k_idx][dir]:
        ns = s + dx[dir]
        nt = t + dy[dir]
        if not (1 <= ns <= L and 1 <= nt <= L) or board[ns][nt] == 2:
            ## 범위를 벗어나서 실패 또는 벽을 만나서
            is_possible = False
            return

        if knights_board[ns][nt]:
            move_lst.add(knights_board[ns][nt])
            move_knights(knights_board[ns][nt], dir)

def changeLocate(lst, dir, nomove):
    for a in range(1, L + 1):
        for b in range(1, L + 1):
            if knights_board[a][b] in lst:
                knights_board[a][b] = 0

    for num in lst:
        if lifes[num] < 1:
            continue

        rr, cc, hh, ww = record_lst[num]
        cnt = 0
        for a in range(rr, rr + hh):
            for b in range(cc, cc + ww):
                knights_board[a + dx[dir]][b + dy[dir]] = num
                if board[a + dx[dir]][b + dy[dir]] == 1:
                    cnt += 1
        for loc in range(4):
            for edge in knights[num][loc]:
                edge[0] += dx[dir]
                edge[1] += dy[dir]

        record_lst[num] = (rr + dx[dir], cc + dy[dir], hh, ww)
        if num == nomove:
            continue
            
        lifes[num] -= cnt
        if lifes[num] < 1:
            for e in range(1, L + 1):
                for f in range(1, L + 1):
                    if knights_board[e][f] == num:
                        knights_board[e][f] = 0
                        
                        
for _ in range(Q):
    a, b = map(int, input().split())
    is_possible = True
    move_lst = set()
    if not lifes[a]:
        continue

    move_lst.add(a)
    move_knights(a, b)

    if is_possible:
        changeLocate(move_lst, b, a)


answer = 0
for q in range(1, N+1):
    if lifes[q] == 0:
        continue
    answer += result_check[q] - lifes[q]

print(answer)