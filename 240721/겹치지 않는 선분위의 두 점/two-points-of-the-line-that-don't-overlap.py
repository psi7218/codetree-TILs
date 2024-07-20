n, m = map(int, input().split())
maxval = 10 ** 18
lst = [list(map(int, input().split())) for _ in range(m)]

lst.sort()

def func(mid):
    cnt = 0
    temp = -maxval

    for a, b in lst:
        while temp + mid <= b:
            cnt += 1
            temp = max(a, temp + mid)

            if cnt >= n:
                break

    return cnt >= n


left = 1
right = maxval
answer = 0

while left <= right:
    mid = (left + right) // 2

    if func(mid):
        left = mid + 1
        answer = max(answer, mid)
    else:
        right = mid - 1

print(answer)