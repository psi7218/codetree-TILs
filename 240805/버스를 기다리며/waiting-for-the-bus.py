n, m, c = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()

start = 0
end = 10**9
answer = 10**9

def ispossible(val):
    idx = 0
    buses = 0
    while buses < m:
        comp = lst[idx]
        temp = idx + 1
        man = 1
        flag = False
        while man < c:
            if lst[temp] - comp <= val:
                temp += 1
                man += 1
            else:
                flag = True
                break
        
        if flag:
            break
        idx = temp 
        buses += 1
    
    if idx == n:
        return True
    return False

while start <= end:
    mid = (start + end) // 2

    if ispossible(mid):
        end = mid - 1
        answer = min(answer, mid)
    else:
        start = mid + 1

print(answer)