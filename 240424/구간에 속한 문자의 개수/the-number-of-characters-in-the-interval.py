n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(str, input())))


for _ in range(k):
    i, j, m, n = map(int, input().split())

    a = 0
    b = 0
    c = 0
    for x in range(i-1, m):
        for y in range(j-1, n):
            if arr[x][y] == 'a':
                a += 1
            elif arr[x][y] == 'b':
                b += 1
            else:
                c += 1

    print(*[a, b, c])