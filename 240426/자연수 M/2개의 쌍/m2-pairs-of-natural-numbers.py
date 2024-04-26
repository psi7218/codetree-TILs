n = int(input())

arr =[] 

for _ in range(n):
    x,y = map(int, input().split())
    arr.append([y,x])

arr.sort()

left = 0
right = n-1
answer = 0
while left <= right:
    lval, lcnt = arr[left]
    rval, rcnt = arr[right]

    answer = max(answer, lval + rval)

    if lcnt > rcnt:
        arr[left][1] -= rcnt
        right -= 1
    
    elif lcnt < rcnt:
        arr[right][1] -= lcnt
        left += 1
    
    else:
        left += 1
        right -= 1

print(answer)