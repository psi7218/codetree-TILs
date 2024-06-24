n, c, g, h = map(int, input().split())

lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a,b))
answer = 0
start = 0
end = 1000000000

def func(val):
    cnt = 0
    for s, e in lst:
        if val < s:
            cnt += c
        elif s <= val <= e:
            cnt += g
        else:
            cnt += h
    
    return cnt

while start < end:
    mid = (start + end) / 2
    result = func(mid)
    # print(result)
    if result >= answer:
        end = mid -1
        answer = result 
    else:
        start = mid + 1

print(answer)