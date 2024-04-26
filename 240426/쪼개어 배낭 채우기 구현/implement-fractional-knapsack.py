n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key= lambda x: -(x[1] / x[0]) )

weight = m
value = 0
idx = 0
while idx < n:
    w,v = arr[idx]
    if weight >= w:
        value += v
        weight -= w
        idx += 1
    else:
        val = (v/w) * weight
        value += val
        break

print(f"{value:.3f}")