n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

lst.sort()

left = 1
right = 10 ** 9 + 1
answer = 0


def func(val):
    cnt = 0
    temp = -10**9 -1
    for a, b in lst:
        temp = max(a, temp + val)
        if a <= temp <= b:
            cnt += 1

    return cnt >= n


while left <= right:
    mid = (left + right) // 2

    if func(mid):
        answer = max(answer, left)
        left = mid + 1
    else:
        right = mid - 1

print(answer)