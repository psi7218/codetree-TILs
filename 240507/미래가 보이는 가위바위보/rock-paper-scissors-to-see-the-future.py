n = int(input())

arr = [input() for _ in range(n)]

p, h, s = 0, 0, 0
L, R = [0] * n, [0] * n

for i in range(n):
    if arr[i] == 'P':
        p += 1
    elif arr[i] == 'H':
        h += 1
    else:
        s += 1

    L[i] = max(p,h,s)

p, h, s = 0, 0, 0
for j in range(n-1, -1, -1):
    if arr[j] == 'P':
        p += 1
    elif arr[j] == 'H':
        h += 1
    else:
        s += 1

    R[j] = max(p,h,s)



answer = 0
for k in range(n-1):
    answer = max(answer, L[k] + R[k+1])

print(answer)