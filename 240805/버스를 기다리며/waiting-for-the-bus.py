n, m, c = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()

start = 0
end = 10**9
answer = 10**9

def ispossible(val):
    total = 0 
    newval = 0
    while True:
        temp = newval
        man_cnt = 1
        idx = temp + 1
        while man_cnt < c and idx < n:
            if lst[idx] - lst[temp] <= val:
                idx += 1
                man_cnt += 1
            else:
                break
        newval = idx
        total += 1

        if newval == n:
            break
    
    return total <= m 


while start <= end:
    mid = (start + end) // 2

    if ispossible(mid):
        end = mid - 1
        answer = min(answer, mid)
    else:
        start = mid + 1

print(answer)