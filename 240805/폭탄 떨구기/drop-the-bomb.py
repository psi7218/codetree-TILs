n, k = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()

start = 0
end = 1000000000

answer = 1000000000

def find(t):
    left = 0
    right = n - 1
    middleval = n
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] > t:
            right = mid - 1
            middleval = min(middleval, mid)
        else:
            left = mid + 1

    return middleval

def ispossible(val):
    idx = 0
    cnt = 0
    flag = False
    while cnt < k:
        now = lst[idx] + 2*val
        location = find(now)

        if location == n:
            flag = True
            break
        else:
            idx = location

        cnt += 1

    return flag

while start <= end:
    mid = (start + end) // 2

    if ispossible(mid):
        end = mid - 1
        answer = min(answer, mid)
    else:
        start = mid + 1

print(answer)