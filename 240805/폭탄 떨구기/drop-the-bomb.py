n, k = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()

start = 0
end = 1000000000
answer = 1000000000

def ispossible(val):
    idx = 0
    cnt = 1
    for i in range(n):
        if lst[i] - lst[idx] <= 2 * val:
            continue
        else:
            cnt += 1
            idx = i
    
    return cnt <= k

while start <= end:
    mid = (start + end) // 2

    if ispossible(mid):
        end = mid - 1
        answer = min(answer, mid)
    else:
        start = mid + 1

print(answer)