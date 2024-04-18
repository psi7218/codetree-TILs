import copy
from collections import deque
import sys
sys.setrecursionlimit(10000)

def func4(list9):
    a = list9[:N//2][::-1]
    b = list9[N//2:]

    d = a[:len(a)//2][::-1]
    e = a[len(a)//2:]
    f = b[:len(b)//2][::-1]
    g = b[len(b)//2:]
    return [f,d,e,g]

def func3(list3):
    list1 = []
    for j in range(len(list3[-1])):
        for i in range(len(list3)-1,-1,-1):
            try:
                list1.append(list3[i][j])
            except:
                break
    return list1


def func2(new_arr):
    visited = copy.deepcopy(new_arr)
    ref = copy.deepcopy(new_arr)

    for i in range(len(new_arr)):
        for j in range(len(new_arr[i])):
            visited[i][j] *= 0
            ref[i][j] *= 0

    q = deque()
    q.append((0,0))
    while q:
        i, j = q.popleft()
        visited[i][j] = 1
        di = [0,1,0,-1]
        dj = [1,0,-1,0]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < len(new_arr) and 0 <= nj < len(new_arr[ni]):
                val = abs(new_arr[i][j] - new_arr[ni][nj]) // 5
                if val > 0:
                    if new_arr[i][j] > new_arr[ni][nj]:
                        ref[i][j] -= val
                        ref[ni][nj] += val
                    else:
                        ref[i][j] += val
                        ref[ni][nj] -= val
                if visited[ni][nj] == 0:
                    q.append((ni,nj))
                    visited[ni][nj] = 1

    for i in range(len(new_arr)):
        for j in range(len(new_arr[i])):
            new_arr[i][j] += ref[i][j] // 2

    return new_arr

def func(check,cnt):
    global count
    if len(check) == 1:
        pass
    else:
        if len(check) > len(check[-1]) - len(check[0]):
            a = func3(func2(func4(func3(func2(check))))) # func3 = list1
            b = sorted(a)
            if max(a)-b[0] <= K:
                count += 1

            else:
                count += 1
                func0(a)
            return
    list1 = check.pop()

    if cnt <= 1:
        idx = 1
    else:
        idx = cnt
    list2 = list1[:idx]
    list3 = list1[idx:]
    check.append(list2)
    check = list(map(list,zip(*check[::-1])))
    check.append(list3)
    func(check,len(check[0]))


def func0(f_list):
    min_val = 100001
    min_list = []
    for idx in range(N):
        if f_list[idx] < min_val:
            min_val = f_list[idx]
            min_list = [idx]
        elif f_list[idx] == min_val:
            min_list.append(idx)

    for min in min_list:
        f_list[min] += 1
    func([f_list],0)


N, K = map(int, input().split())
f_list = list(map(int, input().split()))
count = 0

func0(f_list)
print(count)