n, m = map(int, input().split())
lst = list(map(int, input().split()))
maxval = max(lst)

def ispossible(val):
    global maxval
    if val < maxval:
        return False
    temp = 0
    cnt = 0

    for i in lst:
        if temp + i <= val:
            temp += i
        else:
            cnt += 1
            temp = i
    
    if temp > 0:
        cnt += 1
    return cnt <= m


start = 0
end = 1440
answer = 1441

while start <= end:
    mid = (start + end) // 2

    if ispossible(mid):
        end = mid - 1
        answer = min(answer, mid)
    else:
        start = mid + 1

print(answer)