n, k, l = map(int, input().split())
c = list(map(int, input().split()))

c.sort(reverse=True)

start = 0
end = n
answer = 0

def ispossible(val):
    cnt = k * l
    total = 0
    for i in range(val):
        diff = c[i] - val
        if diff >= 0:
            total += 1
        else:
            if abs(diff) > cnt:
                return False
            else:
                cnt -= abs(diff)
                total += 1
    
    return total >= val


while start <= end:
    mid = (start + end) // 2

    if ispossible(mid):
        start = mid + 1
        answer = max(answer, mid)
    else:
        end = mid - 1

print(answer)