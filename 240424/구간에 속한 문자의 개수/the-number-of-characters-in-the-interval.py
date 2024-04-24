n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(str, input())))


for _ in range(k):
    i, j, k, l = map(int, input().split())

    a = 0
    b = 0
    c = 0
    for x in range(i-1, k):
        for y in range(j-1, l):
            if arr[x][y] == 'a':
                a += 1
            elif arr[x][y] == 'b':
                b += 1
            else:
                c += 1

    print(*[a, b, c])